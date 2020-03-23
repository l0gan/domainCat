import sys
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class IBMXforce:
    def checkIBMxForce(self, domain):
        print('[*] IBM xForce Check: {}'.format(domain))
        s = requests.Session()
        # Hack to prevent cert warnings
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
        try:
            url = 'https://exchange.xforce.ibmcloud.com/api/url/{}'.format(domain)
            headers = {
                'User-Agent': useragent,
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-GB,en;q=0.5',
                'x-ui': 'XFE',
                'Referer': "https://exchange.xforce.ibmcloud.com/url/{}".format(domain),
                'Connection': 'close'
            }
            response = s.get(url, headers=headers, verify=False)

            if response.status_code == 404:
                print('[-] IBM x-Force does not have entries for the domain!')
                return "-"

            responseJson = json.loads(response.text)

            print("\033[1;32m[!] Site categorized as: {}\033[0;0m"\
                .format(" | ".join(responseJson["result"].get('cats', {}).keys())))
            return " | ".join(responseJson["result"].get('cats', {}).keys())

        except Exception as e:            
            print('[-] Error retrieving IBM x-Force reputation!')
            return "-"

if __name__ == "__main__":
    domain = sys.argv[1]
    xf = IBMXforce(domain)
    xf.checkIBMxForce()
