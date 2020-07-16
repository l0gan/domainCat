#! /usr/bin/python3

from argparse import ArgumentParser
import argparse
import sys
import os
from modules import *
import urllib
import re

parser = ArgumentParser(description='Domain Categorization Checking')
parser.add_argument('--domain', '-d', required=False, help='Domain name to lookup')
parser.add_argument('--service', '-s', nargs='?', const='a', help='Service to check Categorization against (Defaults to ALL) (a (ALL), b (Bluecoat), f (Fortiguard), i (IBM xForce), m (McAfee TrustedForce), w (WebSense), g (Google SafeBrowsing), p (PhishTank), c (Cisco Talos))')
parser.add_argument('--domain-list', '-l', required=False, help='List of domains')
parser.add_argument('--quiet', '-q', required=False, action='store_true', help='Suppress domainCat logo')
parser.add_argument('--expired_domain', '-e', required=False, action='store_true', help='Check category on top domains on expireddomains.net (use with -f)')
parser.add_argument('--filters', '-f', required=False, help='Domain Keyword to search on expireddomains.net')
parser.add_argument('--set_cat', required=False, action='store_true', help='Show how to set categorization for each service.')
parser.add_argument('--output', '-o', required=False, help='Output file as CSV')

class domainCat:

    def run(self, domain, service, fname):
        if service == 'b':
            if len(fname) > 0:
              dc.writeOutput(fname, "bluecoat", domain, self.bluecoatCheck(domain))
            else:
              self.bluecoatCheck(domain)
        elif service == 'f':
            if len(fname) > 0:
              dc.writeOutput(fname, "fortiguard", domain, self.fortiguardCheck(domain))
            else:
              self.fortiguardCheck(domain)
        elif service == 'i':
            if len(fname) > 0:
              dc.writeOutput(fname, "ibm xforce", domain, self.ibmCheck(domain))
            else:
              self.ibmCheck(domain)
        elif service == 'm':
            if len(fname) > 0:
              dc.writeOutput(fname, "mcafee", domain, self.trustedsourceCheck(domain))
            else:
              self.trustedsourceCheck(domain)
        elif service == 'w':
            if len(fname) > 0:
              dc.writeOutput(fname, "websense", domain, self.websenseCheck(domain))
            else:
              self.websenseCheck(domain)
        elif service == 'g':
            if len(fname) > 0:
              dc.writeOutput(fname, "google safebrowsing", domain, self.googleCheck(domain))
            else:
              self.googleCheck(domain)
        elif service == 'p':
            if len(fname) > 0:
              dc.writeOutput(fname, "phishtank", domain, self.phishtankCheck(domain))
            else:
              self.phishtankCheck(domain)
        #elif service == 'c':
            #self.ciscoCheck(domain)
        elif service == 'a':
            if len(fname) > 0:
              dc.writeOutput(fname, "bluecoat", domain, self.bluecoatCheck(domain))
              dc.writeOutput(fname, "fortiguard", domain, self.fortiguardCheck(domain))
              dc.writeOutput(fname, "ibm xforce", domain, self.ibmCheck(domain))
              dc.writeOutput(fname, "mcafee", domain, self.trustedsourceCheck(domain))
              dc.writeOutput(fname, "websense", domain, self.websenseCheck(domain))
              #dc.writeOutput(fname, "google safebrowsing", domain, self.googleCheck(domain))
              #dc.writeOutput(fname, "phishtank", domain, self.phishtankCheck(domain))
            else:
              self.bluecoatCheck(domain)
              self.fortiguardCheck(domain)
              self.ibmCheck(domain)
              self.trustedsourceCheck(domain)
              self.websenseCheck(domain)
              #self.googleCheck(domain)
              #self.phishtankCheck(domain)

    def writeOutput(self, fname, service, domain, category):
      if ".csv" not in fname:
        fname = fname + ".csv"

      if os.path.isfile(fname):
        f = open(fname, 'a')
      else:
        f = open(fname, 'w')
        f.write("provider,domain,categorization\r\n")
      f.write("{},{},{}\r\n".format(service, domain, category))

    def trustedsourceCheck(self, domain):
        print("\033[1;34m[*] Targeting McAfee Trustedsource\033[0;0m")
        ts = trustedsource.TrustedSource()
        return ts.check_category(domain)

    def bluecoatCheck(self, domain):
        print("\033[1;34m[*] Targeting Bluecoat WebPulse\033[0;0m")
        b = bluecoat.Bluecoat()
        return b.check_category(domain)

    def ibmCheck(self, domain):
        print("\033[1;34m[*] Targeting IBM Xforce\033[0;0m")
        xf = ibmxforce.IBMXforce()
        return xf.checkIBMxForce(domain)

    def fortiguardCheck(self, domain):
        print("\033[1;34m[*] Targeting Fortiguard\033[0;0m")
        xf = fortiguard.Fortiguard()
        return xf.check_category(domain)

    def websenseCheck(self, domain):            
        print("\033[1;34m[*] Targeting Websense\033[0;0m")
        xf = websense.Websense()
        return xf.check_category(domain)

    def googleCheck(self, domain):
        print("Coming Soon")

    def phishtankCheck(self, domain):
        print("Coming Soon")

    def ciscoCheck(self, domain):
        print("\033[1;34m[*] Targeting Cisco Talos\033[0;0m")
        xf = ciscotalos.CiscoTalos()
        xf.check_category(domain)
        
    def expired_search(self, filename, argfilter):
        es = expireddomfilter.ExpiredDom()
        es.check_filter(filename, argfilter)
        
    def set_cat(self):
        sc = setcat.SetCategories()
        sc.set_cat()
        return xf.check_category(domain)

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
    dc = domainCat()
    args = parser.parse_args()

    quiet = args.quiet
    if not quiet:
        domainCat().asciiArt()
        
        
    if args.set_cat:
        dc.set_cat()
        exit()
    
    if args.expired_domain:
        if not args.filters:
            print('[-] Missing -f option')
        else:
            filename = args.filters + '.txt'
            dList = filename
            dc.expired_search(filename, args.filters)
    else:
        dList = args.domain_list
    
    service = args.service
    if not service:
        service = 'a'
    
    dList = args.domain_list
    if not dList:
        domain = args.domain
        if args.output != None:
          dc.run(domain, service, args.output)
        else:
          dc.run(domain, service, "")
    else:
        f = open(dList, 'r')
        if args.output != None:
          for domain in f:
            dc.run(domain.rstrip(), service, args.output)
        else:
          print("[-] Please specify an output file...")
