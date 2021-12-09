

browser.contextMenus.create({
    id: "run-in-streamlink",
    title: "Run in Streamlink",
    contexts: ["link"]
});


nativeName = "streamlinklink";


browser.contextMenus.onClicked.addListener((info, tab) => {
  switch (info.menuItemId) {
    case "run-in-streamlink":
      url = info.linkUrl;
      break;
  }
  if(url !== undefined && url !== null){
    console.log(url);
    s = browser.runtime.sendNativeMessage(nativeName, url);
  }
});