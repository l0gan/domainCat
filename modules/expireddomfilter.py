import urllib
import re


class ExpiredDom:
    def check_filter(self, filename, argfilter):
        print('[+] Checking domains on expireddomains.net for ' + argfilter)
        # https://www.expireddomains.net/domain-name-search/?q=$filter
        request = urllib.request.Request('https://www.expireddomains.net/domain-name-search/?q=' + argfilter)
        request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)")
        request.add_header("Origin", "www.expireddomains.net")
        response = urllib.request.urlopen(request)
        try:
            resp = response.read().decode('utf-8')
            #store results in filename
            doms = re.findall('<td class="field_statustld_registered"><a href="/domain/(.*?)#namestatus" rel="nofollow"', resp, re.DOTALL)
            f = open(filename, "w")
            for i in doms:
                f.write(i + '\n')
        except Exception as e:
            print("[-] An error occurred")
            print(e)



if __name__ == "__main__":
    argfilter = sys.argv[1]
    filename = argfilter + '.txt'
    e = ExpiredDom()
    e.check_filter(filename, argfilter)