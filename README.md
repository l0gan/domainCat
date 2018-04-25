```
   _
  ( \                ..-----..__
   \.'.        _.--'`  [   '  ' ```'-._
    `. `'-..-'' `    '  ' '   .  ;   ; `-'''-.,__/|/_
      `'-.;..-''`|'  `.  '.    ;     '  `    '   `'  `,
                 \ '   .    ' .     '   ;   .`   . ' 7 \
                  '.' . '- . \    .`   .`  .   .\     `Y
                    '-.' .   ].  '   ,    '    /'`""';:'
                      /Y   '.] '-._ /    ' _.-'
                      \'\_   ; (`'.'.'  ."/
                       ' )` /  `.'   .-'.'
                        '\  \).'  .-'--"
                          `. `,_'`
                            `.__)  

```
# domainCat
Domain Categorization Checking

## Use
Help:
```
usage: domainCat.py [-h] [--domain DOMAIN] [--service SERVICE]

Domain Categorization Checking

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN, -d DOMAIN
                        Domain name to lookup
  --service SERVICE, -s SERVICE
                        Service to check Categorization against (Defaults to
                        ALL) (a (ALL), b (Bluecoat), f (Fortiguard), i (IBM
                        xForce), m (McAfee TrustedForce), w (WebSense), g
                        (Google SafeBrowsing), p (PhishTank), c (Cisco Talos))
```
Running:
```
python domainCat.py --domain example.com

   _
  ( \                ..-----..__
   \.'.        _.--'`  [   '  ' ```'-._
    `. `'-..-'' `    '  ' '   .  ;   ; `-'''-.,__/|/_
      `'-.;..-''`|'  `.  '.    ;     '  `    '   `'  `,
                 \ '   .    ' .     '   ;   .`   . ' 7 \
                  '.' . '- . \    .`   .`  .   .\     `Y
                    '-.' .   ].  '   ,    '    /'`""';:'
                      /Y   '.] '-._ /    ' _.-'
                      \'\_   ; (`'.'.'  ."/
                       ' )` /  `.'   .-'.'
                        '\  \).'  .-'--"
                          `. `,_'`
                            `.__)  
     domainCat - Domain Categorization Discovery at it's finest
     written by: l0gan
[*] Targeting Bluecoat WebPulse
[*] Checking category for example.com
[!] Site categorized as: Technology/Internet
[*] Targeting Fortiguard
[*] Checking category for example.com
[!] Site categorized as: Information Technology
[*] Targeting IBM Xforce
[*] IBM xForce Check: example.com
[!] Site categorized as: 
[*] Targeting McAfee Trustedsource
[-] Getting anti-automation tokens
[*] Checking category for example.com
[!] Site categorized as: - Technical Information
[*] Targeting Websense
[-] Checking if you have any requests for the day.
[-] You have 2 requests left for the day.
[*] Checking category for example.com
[!] Site categorized as: Information Technology
[*] Targeting Cisco Talos
[*] Checking category for example.com
[!] Site categorized as: Reference

```

## Roadmap
- Add in support for Google Safebrowsing, PhishTank
- Update to python3

### Some code borrowed from these awesome projects:
Domain Hunter: https://github.com/threatexpress/domainhunter

CatMyPhish: https://github.com/Mr-Un1k0d3r/CatMyFish 

Chameleon: https://github.com/mdsecactivebreach/Chameleon
