import urllib2
import sys
import json


class Bluecoat:
    def check_category(self, domain):
        # Category checking lifted from CatMyFish
        # https://github.com/Mr-Un1k0d3r/CatMyFish/blob/master/CatMyFish.py
        print("[*] Checking category for " + domain)
        data = json.dumps({'url':domain,'captcha':''})
        request = urllib2.Request("https://sitereview.bluecoat.com/resource/lookup", data=data)
        request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
        request.add_header("Origin", "https://sitereview.bluecoat.com")
        request.add_header("Referer", "https://sitereview.bluecoat.com/lookup")
        request.add_header("X-Requested-With", "XMLHttpRequest")
        request.add_header("Content-Type", "application/json; charset=utf-8")
        response = urllib2.urlopen(request, data)
        try:
            json_data = json.loads(response.read())
            if json_data.has_key("errorType"):
                if json_data["errorType"] == "captcha":
                    print("[-] BlueCoat blocked us :(")
                    sys.exit(0)
            cat = json_data["categorization"][0]["name"]
            print("\033[1;32m[!] Site categorized as: " + cat + "\033[0;0m")
        except Exception as e:
            print("[-] An error occurred")
            print(e)


if __name__ == "__main__":
    domain = sys.argv[1]
    b = Bluecoat()
    b.check_category(domain)
