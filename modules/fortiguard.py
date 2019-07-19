import urllib2
import urllib
import requests
import sys
import re
from urlparse import urlparse
from bs4 import BeautifulSoup
import json
import threading
import SocketServer
import SimpleHTTPServer
import time


class Fortiguard:
    def check_category(self, domain):
        print("[*] Checking category for " + domain)
        request = urllib2.Request("https://fortiguard.com/webfilter?q=" + domain)
        request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
        request.add_header("Origin", "https://fortiguard.com")
        request.add_header("Referer", "https://fortiguard.com/webfilter")
        response = urllib2.urlopen(request)
        try:
            resp = response.read()
            cat = re.findall('Category: (.*?)" />', resp, re.DOTALL)
            print("\033[1;32m[!] Site categorized as: " + cat[0] + "\033[0;0m")
        except Exception as e:
            print("[-] An error occurred")
            print(e)


if __name__ == "__main__":
    domain = sys.argv[1]
    b = Fortiguard()
    b.check_category(domain)
