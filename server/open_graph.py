import urllib3
from urllib.parse import quote
import os
og_key = os.environ["OPENGRAPH_APIKEY"]

http = urllib3.PoolManager()


def get_open_graph():
    url = "https://opengraph.io/api/1.1/site/" + quote("http://www.futurice.com") + "?app_id="+og_key
    print(url)
    r = http.request('GET', url)
    return r.data
