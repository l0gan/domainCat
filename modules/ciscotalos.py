
import urllib
import requests
import sys
import re
from bs4 import BeautifulSoup
import json
import threading
import time
import pprint

class CiscoTalos:
    def check_category(self, domain):
            print("[*] Checking category for " + domain)
            request = urllib.request.Request("https://talosintelligence.com/sb_api/query_lookup?query=%2Fapi%2Fv2%2Fdetails%2Fdomain%2F&query_entry=" + domain + "&offset=0&order=ip+asc")
            request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
            request.add_header("Referer", "https://www.talosintelligence.com/reputation_center/lookup?search=" + domain)
            response = urllib.request.urlopen(request)
            try:
                jsonChk = json.loads(response.read())
                categorydict = jsonChk.get("category")
                cat = categorydict.get("description")
                print("\033[1;32m[!] Site categorized as: " + cat + "\033[0;0m")
                return cat
            except Exception as e:
                print("[-] An error occurred")
                print(e)

if __name__ == "__main__":
    domain = sys.argv[1]
    b = CiscoTalos()
    b.check_category(domain)
