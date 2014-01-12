document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('sendButton').addEventListener('click', submitSettings);
});

function submitSettings (e) {
	var ip = document.getElementById('raspIp').value;
    var port = document.getElementById('raspPort').value;

    localStorage['raspIp'] = ip;
    localStorage['raspPort'] = port;

	chrome.tabs.getCurrent(function(tab) {
		chrome.tabs.remove(tab.id);
	});
}