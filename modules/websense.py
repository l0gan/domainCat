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


class Websense:
    def req_check(self):
        request = urllib2.Request("https://csi.forcepoint.com")
        request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
        response = urllib2.urlopen(request)
        resp = response.read()
        num_remaining = re.findall('reports">(.*?) report', resp, re.DOTALL)[0]
        return num_remaining


    def check_category(self, domain):
        print("[-] Checking if you have any requests for the day.")
        num_remaining = self.req_check()
        print("[-] You have " + num_remaining + " requests left for the day.")
        if int(num_remaining) > 0:
            print("[*] Checking category for " + domain)
            request = urllib2.Request("https://csi.forcepoint.com")
            data = urllib.urlencode({"LookupUrl":domain})
            request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
            response = urllib2.urlopen(request, data=data)
            try:
                resp = response.read()
                location = re.findall('<td class="classAction">(.*?)</td>',resp,re.DOTALL)
                cat = location[2]
                print("\033[1;32m[!] Site categorized as: " + cat + "\033[0;0m")
            except Exception as e:
                print("[-] An error occurred")
                print(e)
        else:
            print("[-] No requests remaining for this IP.")


if __name__ == "__main__":
    domain = sys.argv[1]
    b = Websense()
    b.check_category(domain)
