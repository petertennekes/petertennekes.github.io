import urllib3
from urllib.parse import quote
from urllib3 import ProxyManager
import os
og_key = os.environ["OPENGRAPH_APIKEY"]
proxy = os.getenv("PROXY")

if proxy is not None:
    http = urllib3.ProxyManager(proxy)
else:
    http = urllib3.PoolManager()


def get_open_graph(target_url):
    url = "http://opengraph.io/api/1.1/site/" + quote(target_url) + "?app_id="+og_key
    print(url)
    r = http.request('GET', url)
    return r.data
