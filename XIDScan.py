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
  m    m mmmmm  mmmm         m     m m    m  mmmm  mmmmm   mmmm
   #  #    #    #   "m       #  #  # #    # m"  "m   #    #"   "
    ##     #    #    #       " #"# # #mmmm# #    #   #    "#mmm
   m""m    #    #    #        ## ##" #    # #    #   #        "#
  m"  "m mm#mm  #mmm"         #   #  #    #  #mm#  mm#mm  "mmm#"                               
        """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 2:
      d3 = raw_input('Masukan Ip atau Domain : ')
      os.system("clear")
      print("""
    mmmmmmm mmmmm    mm     mmm  mmmmmm.     mmmmm   mmmm  m    mmmmmmmm mmmmmm
       #    #   "#   ##   m"   " #          #   "# m"  "m #    #   #    #
       #    #mmmm"  #  #  #      #mmmmm.   #mmmm" #    # #    #   #    #mmmmm
       #    #   "m  #mm#  #      #        #   "m #    # #    #   #    #
       #    #    " #    #  "mmm" #mmmmm  #    "m #mm#  "mmmm"   #    #mmmmm
  """)
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Masukan Domain : ')
      os.system("clear")
      print("""
         mmmm   mm   m  mmmm      m       mmmm   mmmm    mmm  m    m m    m mmmmm
        #   "m #"m  # #"   "     #      m"  "m m"  "m m"   " #  m"  #    # #   "#
        #    # # #m # "#mmm     #      #    # #    # #      #m#    #    # #mmm#"
        #    # #  # #     "#   #      #    # #    # #      #  #m  #    # #
        #mmm"  #   ## "mmm#"  #mmmmm  #mm#   #mm#   "mmm" #   "m "mmmm" #
 """)
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 4:
	  d3 = raw_input('Masukan IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
 mmmmm  mmmmmm m    m mmmmmm mmmmm   mmmm  mmmmmm        mmmm   mm   m  mmmm
 #   "# #      "m  m" #      #   "# #"   " #            #   "m #"m  # #"   "
 #mmmm" #mmmmm  #  #  #mmmmm #mmmm" "#mmm  #mmmmm      #    # # #m # "#mmm
 #   "m #       "mm"  #      #   "m     "# #          #    # #  # #     "#
 #    " #mmmmm   ##   #mmmmm #    " "mmm#" #mmmmm    #mmm"  #   ## "mmm#" 
 """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Masukan Ip atau Domain : ')
	  os.system("clear")
	  print("""
   mmm  mmmmmm  mmmm      mmmmm  mmmmm
 m"   " #      m"  "m      #    #   "#
 #   mm #mmmmm #    #     #    #mmm#"
 #    # #      #    #    #    #
  "mmm" #mmmmm  #mm#  mm#mm  #
         """)
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Masukan Ip atau Domain: ')
      os.system("clear")
      print("""
      mm   m m    m   mm   mmmmm     mmmm    mmm    mm   mm   m
      #"m  # ##  ##   ##   #   "#  #"   " m"   "   ##   #"m  #
      # #m # # ## #  #  #  #mmm#" "#mmm  #       #  #  # #m #
      #  # # # "" #  #mm#  #         "# #       #mm#  #  # #
      #   ## #    # #    # #    "mmm#"  "mmm" #    # #   ##                                        "
""")
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Masukan Ip atau Domain : ')
	  os.system("clear")
	  print("""
 mmmmm  m    m  mmmmm  mmmmm    m       mmmm   mmmm    mmm  m    m m    m mmmmm
 #   "# "m  m"    #    #   "#  #      m"  "m m"  "m m"   " #  m"  #    # #   "#
 #mmmm"  #  #     #    #mmm#" #      #    # #    # #      #m#    #    # #mmm#"
 #   "m  "mm"     #    #     #      #    # #    # #      #  #m  #    # #
 #     #   #    mm#mm  #    #mmmmm  #mm#   #mm#   "mmm" #   "m "mmmm" #
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
