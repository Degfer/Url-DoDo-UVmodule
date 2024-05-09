from jnius import autoclass
from android.runnable import run_on_ui_thread

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

def create_webview(thelistitem):
	webview = WebView(activity)
	webview.getSettings().setJavaScriptEnabled(True)
	wvc = WebViewClient()
	webview.setWebViewClient(wvc)
	activity.setContentView(webview)
	webview.loadUrl(thelistitem)
