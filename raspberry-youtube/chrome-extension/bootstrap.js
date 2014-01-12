// when the extension is first installed
chrome.runtime.onInstalled.addListener(function(details) {
    console.log('installed');
    // localStorage["be_a_buzzkill"] = true;
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

// show the popup when the user clicks on the page action.
chrome.pageAction.onClicked.addListener(function(tab) {
    var req = new XMLHttpRequest();
    req.open("GET", 'http://192.168.1.10:8080?v=kww0WXcH74o', true);
    req.send();

    //chrome.tabs.executeScript(tab.id, {"file": "raspberry-to-pi.js"}, function(){console.log('video sent')});
});


