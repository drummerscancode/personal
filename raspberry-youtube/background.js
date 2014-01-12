
1	// Copyright (c) 2011 The Chromium Authors. All rights reserved.
2	// Use of this source code is governed by a BSD-style license that can be
3	// found in the LICENSE file.
4	
5	// When the extension is installed or upgraded ...
6	chrome.runtime.onInstalled.addListener(function() {
7	  // Replace all rules ...
8	  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
9	    // With a new rule ...
10	    chrome.declarativeContent.onPageChanged.addRules([
11	      {
12	        // That fires when a page's URL contains a 'g' ...
13	        conditions: [
14	          new chrome.declarativeContent.PageStateMatcher({
15	            pageUrl: { urlContains: 'g' },
16	          })
17	        ],
18	        // And shows the extension's page action.
19	        actions: [ new chrome.declarativeContent.ShowPageAction() ]
20	      }
21	    ]);
22	  });
23	});
