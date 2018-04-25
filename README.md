```
                                            ooooo$oo
                                         oo$$$$$$$$$$$o
                           """"oooo    $$$$$$$$$$$$$$$$
                               " """$$$$$o$$$$$""$$$$$"
               ooo o      ooooo      "   o$$$   o$$$$$
               " ooo $oo$$$$$$$$$$$oo    ""    o$$$$"
        ooooooo$"" $$$""        """$$$o     $$$$$$$
    oo$$$$$""""ooo$""                ""       o$$$$
   $$$$$$$$  oo$$$"       ooo$ooo          o$$$$$$$
   ""$$$$oo"""""        o$$$$$$$$$$ooo   o$""""   "$
       ""              $$$$""      """"            $$
       o$$           o$$$                o o  o    $$$  o$"
        o$         $$$$               ooo "o$ $$oo$$$$$  o$"
        $ oooo$o$$$$$$"        oo$$$$$$$$$$oo$$$$$$o$" o$"
        $$$      "" "         $$$$""""$$$ "$$$        $  ooo$$$""""
       o$"                  o$$"       $"   "         ""   $"
        $$   oo       o    $$" oo """                       """oooo
         $oo$$$$oo    "  o$$$$$o " o                             o$$$o
         "$$$$"  "$$$$$$""""                                 "$o
         $$$"      ""$$o oo                 $ "                 "$o
     ooo   $"$o oo$ o$$$"""""""$$o      """$$$o              $o""""$$o
       """"$$ ""$"o$$""   oooo "$$o        "  "               "o
    "  oooo "    $$" ooo$$$$$$oo$$$       o        ooooo   oo  ""oo
    oo$"""       $$o$$$$$$$$$$$$$"       $"       $$$$$$$$o$ "$o  "
ooo$oooooo       "$$$$$$$$$$$$$""      o"      oo$$""""""""$o  "
 "     $$$"        "$$$$$$$$$""       o        "$$        o$$o
     oo"" o o    oo   """"        o ""        o o$o    o$$$$$$$
   o$$o"" "$"      $ooo       o$""           o$$$"   o$$$$$$$$$o
   "     oo            " """ "             o"$$$"  o$$$""""    $$o
        o$o$"  o                         o$  $$o  o$$"          $$
        ""    $" oo  o o o          oooo$$"    $  $"          oo$$$
             o$o$$$oo"oo ""$$$o$$$$$$$$"       $ ""        o$$$$$$$$o
             $$$$$$$$$$ooo  """""""""          $o$o     oo$$$$$$$$"$$o
             "$$$$$$$$$$$                     $"o$$   o$$$$$$$$""   $$o
              $     "$ $$o$ooo$$$$o           " $$"  "$$$$""         $$
             $"    oo$o$$$"""      "$$o          oo$   $             "$
             $"   o""" "$o            $o        "$ $oo$$$             $$
            o$$$$$       $$             "$o        $""" $$o$$$$$$$$$$$$$$o
            $$$$$$       $o               "$o      $oo  $$$$$$""$""$"$"$$$$
           "$$$" $$oooo$$"                  $$$o      ooo$$            $$$
            $"  $$ ""$$                    oo "$$$ooo$$$$$$$$$$$$$oo    $$
            $   $    $"      o          $$$  ""$$$$  $$$$$$$$oo """$$$$o$$$
           $$  $$   $$      $$         $$""$o  $$$$  "$$$  $$$$o   "$$$$$$$
           $$$$$$$$ $$     o$$       $$    "$$ "$"     $$$    "$$     "$$$$
           $$""   $$$$o     $$       $"     $$ $$      $$$$    "$$     $$$$
          """  oo$$$ "$    o$$o      $"     $$ o$"     $$$$     ""$    "$$$
          $    $$$$$o "$o o$""$o    $$     o"  $$oo    $$$$       $      $$"
          $   o$  "$$oo""""   ""$oo$"      "oo"""""""o$$$$o        o      ""
          $   $$   "$$$$oo$o            o o$$"         $" $$$oo    $      $
         o$   "$o    """"$$"""$"""""""""""""           $$$"""""" oo""  oo$"
         $$ o  $$o     o$$"   $                        """       ""  $"$$$
          "$$$o$$$$oooo""    o$                         $o"$            $$o
            "$o$""$" "       $$$                           ooo$oo$$$$$$$$$$
                               "                           """"""""$$$$$$$$
                              o                           o            ""$$
                              "                           "               "
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
python domainCat.py
[*] Enter Domain name to check Categorization on: <domain>
[*] Targeting McAfee Trustedsource
[-] Getting anti-automation tokens
[*] Checking category for <domain>
[!] Found category: - Business- Software/Hardware
[*] Targeting Bluecoat WebPulse
[*] Checking category for <domain>
[!] Your site is categorised as: Computer/Information Security
[*] Targeting IBM Xforce
[*] IBM xForce Check: <domain>
[!] Domain categorised as IT Security / IT Information
[*] Targeting Fortiguard
[*] Checking category for <domain>
[!] Your site is categorised as: Information Technology
[*] Targeting Websense
[-] Checking if you have any requests for the day.
[-] You have 1 requests left for the day.
[*] Checking category for <domain>
[!] Your site is categorised as: Information Technology
```

## Roadmap
- Add in support for Google Safebrowsing, PhishTank
- Update to python3

### Some code borrowed from these awesome projects:
Domain Hunter: https://github.com/threatexpress/domainhunter

CatMyPhish: https://github.com/Mr-Un1k0d3r/CatMyFish 

Chameleon: https://github.com/mdsecactivebreach/Chameleon
