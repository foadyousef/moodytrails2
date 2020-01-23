# Proxy setting in case need to change proxy

my_proxy = Proxy({‘proxyType’: ProxyType.MANUAL,
‘httpProxy’: ’127.0.0.1:8118′,
‘sslProxy’: ’127.0.0.1:8118′,
‘noProxy’: ‘www.google-analytics.com, ajax.googleapis.com, apis.google.com’
})
browser = webdriver.Firefox(proxy=my_proxy)