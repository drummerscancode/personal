// when the extension is first installed
chrome.runtime.onInstalled.addListener(function(details) {
    chrome.tabs.create({url: 'settings.html', active: true}, function(tab){ document.sub});
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

    if ( !localStorage['chrome-to-pi'] ) {
        // it's not yet setup
        // chrome.pageAction.setPopup({tabId: tab.id, popup: 'popup.html'});
    }

    // show the page action
    chrome.pageAction.show(tab.id);
});

var findPropertyFromString = function(url, key) {
        var key = key + "=";
        var index = url.indexOf('?');
        var video_url = url.substring(index + 1);

        // TODO: for the time being there is no & in the url
        return video_url.split(key)[1];
    }

chrome.pageAction.onClicked.addListener(function(tab) {
    // chrome.pageAction.getPopup({tabId: tab.id}, function () {console.log('returned')});
    var raspIp = localStorage.raspIp;
    var raspPort = localStorage.raspPort;
    if (!(raspIp && raspPort)) {
        console.log('Please set it!');   
        chrome.pageAction.setPopup({tabId: tab.id, popup: 'settings.html'});
        return;
    }

    console.log(tab.url);
    var v_param = findPropertyFromString(tab.url, 'v');
    var req = new XMLHttpRequest();
    req.open("GET", 'http://' + raspIp + ':' + raspPort + '?v=' + v_param , true); // kww0WXcH74o
    req.onload = function (e){
        chrome.pageAction.setPopup({tabId: tab.id, popup: 'success.html'});
        console.log('success');
    }
    req.send();

    //chrome.tabs.executeScript(tab.id, {"file": "raspberry-to-pi.js"}, function(){console.log('video sent')});
});




