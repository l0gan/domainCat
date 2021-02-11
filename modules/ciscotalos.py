
import requests
import json

class CiscoTalos:
        def check_category(self, domain):
                print("[*] Checking category for " + domain)
                url = 'https://talosintelligence.com/sb_api/remote_lookup?hostname=SDSv3&query_string=/score/single/json?url=' + domain
                user_agent = 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01'
                referer = 'https://talosintelligence.com/reputation_center/lookup?search=google.com'
                s = requests.Session()
                s.headers.update({'user-agent': user_agent})
                s.headers.update({'referer': referer})
                r = s.get(url)
                try:
                        json_data = r.json()
                        categorydict = json_data["categories"]
                        shortdesc = categorydict[0]
                        cat = shortdesc["short_description"]
                        print("\033[1;32m[!] Site categorized as: " + cat + "\033[0;0m")
                except Exception as e:
                        print("[-] An error occurred")
                        print(e)

if __name__ == "__main__":
    domain = sys.argv[1]
    b = CiscoTalos()
    b.check_category(domain)
