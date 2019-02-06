#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[0m 
 m    m mmmmm  mmmm      mmmm   mmm    mm   mm   m
  #  #    #    #   "m  #"   " m"   "   ##   #"m  #
   ##     #    #    # "#mmm  #       #  #  # #m #
  m""m    #    #    #    "# #       #mm#  #  # #
 m"  "m mm#mm  #mmm" "mmm#" "mmm" #    # #   ## \033[0m  \033[91m    \033[1m 
	   
	   [/> Coded By: MR_XID <\]
         {/>THANKS TO: D35TROY SQUAD<\}                               
     '''
menu = '''\033[0m
    {1 X-Whois lookup
    {2 X-Traceroute
    {3 X-DNS Lookup
    {4 X-Reverse DNS Lookup
    {5 X-GeoIP Lookup
    {6 X-Port Scan
    {7 X-Reverse IP Lookup
   {99 X-Exit                                                                                                                   
 '''
print logo
print menu
def quit():
            con = raw_input('Lanjutkan[Y/n]/> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("MR_XID/> ")
    if choice == 1:
      d3 = raw_input('Masukan Ip atau Domain : ')
      os.system("clear")
      print("""
   _    _ __ ___    _         _ _   _  ___ ___ ____-
   \ \/ /_ _|  _ \  \ \      / / | | |/ _ \_ _/ ___|
    \  / | || | | |  \ \ /\ / /| |_| | | | | |\___ \
    /  \ | || |_| |   \ V  V / |  _  | |_| | | ___) |
   /_/\_\___|____/     \_/\_/  |_| |_|\___/___|____/                               
        """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 2:
      d3 = raw_input('Masukan Ip atau Domain : ')
      os.system("clear")
      print("""
   __  _____ ____    _____ ____      _    ____ _____ ____             _
   \ \/ /_ _|  _ \  |_   _|  _ \    / \  / ___| ____|  _ \ ___  _   _| |_ ___
    \  / | || | | |   | | | |_) |  / _ \| |   |  _| | |_) / _ \| | | | __/ _ \
    /  \ | || |_| |   | | |  _ <  / ___ \ |___| |___|  _ < (_) | |_| | ||  __/
   /_/\_\___|____/    |_| |_| \_\/_/   \_\____|_____|_| \_\___/ \__,_|\__\___|
  """)
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Masukan Domain : ')
      os.system("clear")
      print("""
  __  _____ ____    ____  _   _ ____    _     ___   ___   ____ _  ___   _ ____
  \ \/ /_ _|  _ \  |  _ \| \ | / ___|  | |   / _ \ / _ \ / ___| |/ / | | |  _ \
   \  / | || | | | | | | |  \| \___ \  | |  | | | | | | | |   | ' /| | | | |_) |
   /  \ | || |_| | | |_| | |\  |___) | | |__| |_| | |_| | |___| . \| |_| |  __/
  /_/\_\___|____/  |____/|_| \_|____/  |_____\___/ \___/ \____|_|\_\\___/|_|
 """)
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 4:
	  d3 = raw_input('Masukan IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
__  _____ ____                                       ____  _   _ ____
\ \/ /_ _|  _ \   _ __ _____   _____ _ __ ___  ___  |  _ \| \ | / ___|
 \  / | || | | | | '__/ _ \ \ / / _ \ '__/ __|/ _ \ | | | |  \| \___ \
 /  \ | || |_| | | | |  __/\ V /  __/ |  \__ \  __/ | |_| | |\  |___) |
/_/\_\___|____/  |_|  \___| \_/ \___|_|  |___/\___| |____/|_| \_|____/
 """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Masukan Ip atau Domain : ')
	  os.system("clear")
	  print("""
__  _____ ____     ____       ___  _ ____
\ \/ /_ _|  _ \   / ___| ___ / _ \(_)  _ \
 \  / | || | | | | |  _ / _ \ | | | | |_) |
 /  \ | || |_| | | |_| |  __/ |_| | |  __/
/_/\_\___|____/   \____|\___|\___/|_|_|
         """)
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Masukan Ip atau Domain: ')
      os.system("clear")
      print("""
  __  _____ ____    _   _                      ____
 \ \/ /_ _|  _ \  | \ | |_ __ ___   __ _ _ __/ ___|  ___ __ _ _ __
  \  / | || | | | |  \| | '_ ` _ \ / _` | '_ \___ \ / __/ _` | '_ \
  /  \ | || |_| | | |\  | | | | | | (_| | |_) |__) | (_| (_| | | | |
 /_/\_\___|____/  |_| \_|_| |_| |_|\__,_| .__/____/ \___\__,_|_| |_|
                                        |_|
""")
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Masukan Ip atau Domain : ')
	  os.system("clear")
	  print("""
__  _____ ____    ______     ___       _                     _
\ \/ /_ _|  _ \  |  _ \ \   / (_)_ __ | |    ___   ___   ___| | ___   _ _ __
 \  / | || | | | | |_) \ \ / /| | '_ \| |   / _ \ / _ \ / __| |/ / | | | '_ \
 /  \ | || |_| | |  _ < \ V / | | |_) | |__| (_) | (_) | (__|   <| |_| | |_) |
/_/\_\___|____/  |_| \_\ \_/  |_| .__/|_____\___/ \___/ \___|_|\_\\__,_| .__/
                                |_|                                    |_|
  """)
	  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  os.system("clear")
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  print("")
	  print("\033[91m\033[1mFile Saved On : ")
	  os.system("pwd")
	  print("File : index.html?q=" +d3)
	  print("\033[0m")
	  quit()
  except(KeyboardInterrupt):
    print ""
select()
