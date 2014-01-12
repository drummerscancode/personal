// document.addEventListener('DOMContentLoaded', function () {
//   raspToPi.send();
// });



var raspToPi = {
    /*
     * Extract the GET parameters from the string
     */
    findPropertyFromString : function(url, key) {
        var key = key + "=";
        var index = url.indexOf('?');
        var video_url = url.substring(index + 1);

        // TODO: for the time being there is no & in the url
        return video_url;
    },

    getUrl: function() {
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            return tabs[0].id;
        });
    },
    
    send : function () {
        //var url = this.getUrl();         
        // console.log(url);   
        var url2 = chrome.tabs.getSelected(null, function(tab){
            return tab;
        });
        console.log(url2);   

        // console.log(this.findPropertyFromString(url, 'v')); 
    }
}

function sendToPi() {
    var req = new XMLHttpRequest();
    req.open("GET", '192.168.1.10:8080?v=kww0WXcH74o', true);
}

console.log(raspToPi.send());


