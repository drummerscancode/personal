// when the extension is first installed
chrome.runtime.onInstalled.addListener(function(details) {
    console.log('installed');
    if ( !localStorage['chrome-to-pi'] ) {
        // it's not yet setup

    } 
});

// Listen for any changes to the URL of any tab.
// see: http://developer.chrome.com/extensions/tabs.html#event-onUpdated
chrome.tabs.onUpdated.addListener(function(id, info, tab){
    console.log('updated');
    // decide if we're ready to inject content script
    if (tab.status !== "complete"){
        console.log("not yet");
        return;
    }
    if (tab.url.toLowerCase().indexOf("youtube.com") === -1){
        console.log("not here");
        return;
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
    console.log(tab.url);
    var v_param = findPropertyFromString(tab.url, 'v');
    var req = new XMLHttpRequest();
    req.open("GET", 'http://192.168.1.10:8080?v=' + v_param , true); // kww0WXcH74o
    req.onload = function (e){
        console.log('success');
        document.body.appendChild('Success');
    }
    req.send();

    //chrome.tabs.executeScript(tab.id, {"file": "raspberry-to-pi.js"}, function(){console.log('video sent')});
});


