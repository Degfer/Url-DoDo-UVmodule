def create_webview(thelistitem):
	webview = WebView(activity)
	webview.getSettings().setJavaScriptEnabled(True)
	wvc = WebViewClient()
	webview.setWebViewClient(wvc)
	activity.setContentView(webview)
	webview.loadUrl(thelistitem)