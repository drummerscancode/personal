
/**
 * Run when the extension is first installed
 */
chrome.runtime.onInstalled.addListener(function(details) {
    chrome.tabs.create({url: 'initSettings.html', active: true}, function(tab){ document.sub});
});

// Listen for any changes to the URL of any tab.
// see: http://developer.chrome.com/extensions/tabs.html#event-onUpdated
chrome.tabs.onUpdated.addListener(function(id, info, tab){
    // decide if we're ready to inject content script
    if (tab.status !== "complete"){
        return;
    }
    if (tab.url.toLowerCase().indexOf("youtube.com") === -1){
        return;
    }

    if ( !(localStorage.raspIp && localStorage.raspPort) ) {
        // it's not yet setup - f** dat shit
        // chrome.pageAction.setPopup({tabId: tab.id, popup: 'reSettings.html'});
    }

    // show the page action
    chrome.pageAction.show(tab.id);
});

var searching_images = ['logo.png',
                        'love.png'];
var image_index = 1;
var keep_switching_icon = true;

function rotateIcon(tab) {   
    if ( keep_switching_icon ) {
        chrome.pageAction.setIcon({tabId: tab.id, path: searching_images[image_index]}, null);
        image_index = (image_index + 1) % searching_images.length;
        window.setTimeout(function() { rotateIcon(tab);}, 100);
    }
    else {
        chrome.pageAction.setIcon({tabId: tab.id, path: searching_images[0]}, null);
    }
}


// will be called if no popup attached
chrome.pageAction.onClicked.addListener(function(tab) {
    sendVideo(tab);
});

// actual sending of the vid    
function sendVideo(tab) {
    var findPropertyFromString = function(url, key) {
        var key = key + "=";
        var index = url.indexOf('?');
        var video_url = url.substring(index + 1);

        // TODO: for the time being there is no & in the url
        return video_url.split(key)[1];
    }

    var raspIp = localStorage.raspIp;
    var raspPort = localStorage.raspPort;

    // TODO check again
    console.log(tab.url);
    var v_param = findPropertyFromString(tab.url, 'v');
    var req = new XMLHttpRequest();
    req.open("GET", 'http://' + raspIp + ':' + raspPort + '?v=' + v_param , true); // kww0WXcH74o
    // req.onload = function (e){
    //     chrome.pageAction.setIcon({tabId: tab.id, path: 'love.png'}, null);
    //     console.log('success');
    // }
    keep_switching_icon = true;
    rotateIcon(tab);

    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            keep_switching_icon = false;
            if ( req.status != 200 ) {
                console.log('oupsie');
            }
            else {
                console.log('alles guet');
            }
        };
    }    
    req.send();
}