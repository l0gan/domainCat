#!/usr/bin/env python3

from argparse import ArgumentParser
import sys
from modules import *

parser = ArgumentParser(description='Domain Categorization Checking')
parser.add_argument('--domain', '-d', required=True, help='Domain name to lookup')
parser.add_argument('--service', '-s', nargs='?', const='a', help='Service to check Categorization against \
                    (Defaults to ALL) (a (ALL), b (Bluecoat), f (Fortiguard), i (IBM xForce), m (McAfee TrustedForce), \
                    w (WebSense), g (Google SafeBrowsing), p (PhishTank), c (Cisco Talos))')


class domainCat:

    def run(self, domain, service):
        if service == 'b':
            self.bluecoatCheck(domain)
        elif service == 'f':
            self.fortiguardCheck(domain)
        elif service == 'i':
            self.ibmCheck(domain)
        elif service == 'm':
            self.trustedsourceCheck(domain)
        elif service == 'w':
            self.websenseCheck(domain)
        # elif service == 'g':
            # self.googleCheck(domain)
        # elif service == 'p':
            # self.phishtankCheck(domain)
        elif service == 'c':
            self.ciscoCheck(domain)
        elif service == 'a':
            self.bluecoatCheck(domain)
            self.fortiguardCheck(domain)
            self.ibmCheck(domain)
            self.trustedsourceCheck(domain)
            self.websenseCheck(domain)
            # self.googleCheck(domain)
            # self.phishtankCheck(domain)
            self.ciscoCheck(domain)


    def trustedsourceCheck(self, domain):
        print("\033[1;34m[*] Targeting McAfee Trustedsource\033[0;0m")
        ts = trustedsource.TrustedSource()
        ts.check_category(domain)


    def bluecoatCheck(self, domain):
        print("\033[1;34m[*] Targeting Bluecoat WebPulse\033[0;0m")
        b = bluecoat.Bluecoat()
        b.check_category(domain)


    def ibmCheck(self, domain):
        print("\033[1;34m[*] Targeting IBM Xforce\033[0;0m")
        xf = ibmxforce.IBMXforce()
        xf.checkIBMxForce(domain)


    def fortiguardCheck(self, domain):
        print("\033[1;34m[*] Targeting Fortiguard\033[0;0m")
        xf = fortiguard.Fortiguard()
        xf.check_category(domain)


    def websenseCheck(self, domain):
        print("\033[1;34m[*] Targeting Websense\033[0;0m")
        xf = websense.Websense()
        xf.check_category(domain)


    # def googleCheck(self, domain):
        # print("Coming Soon")


    # def phishtankCheck(self, domain):
        # print("Coming Soon")


    def ciscoCheck(self, domain):
        print("\033[1;34m[*] Targeting Cisco Talos\033[0;0m")
        xf = ciscotalos.CiscoTalos()
        xf.check_category(domain)


    def asciiArt(self):
        print("""
   _
  ( \                ..-----..__
   \.'.        _.--'`  [   '  ' ```'-._
    `. `'-..-'' `    '  ' '   .  ;   ; `-'''-.,__/|/_
      `'-.;..-''`|'  `.  '.    ;     '  `    '   `'  `,
                 \ '   .    ' .     '   ;   .`   . ' 7 \\
                  '.' . '- . \    .`   .`  .   .\     `Y
                    '-.' .   ].  '   ,    '    /'`""';:'
                      /Y   '.] '-._ /    ' _.-'
                      \\'\_   ; (`'.'.'  ."/
                       ' )` /  `.'   .-'.'
                        '\  \).'  .-'--"
                          `. `,_'`
                            `.__)
     domainCat - Domain Categorization Discovery at it's finest
     written by: l0gan""")


if __name__ == "__main__":
    args = parser.parse_args()
    domainCat().asciiArt()
    domain = args.domain
    service = args.service
    if not service:
        service = 'a'
    dc = domainCat()
    dc.run(domain, service)

