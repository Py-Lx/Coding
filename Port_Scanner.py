import os
import socket
import subprocess
import sys
import time
from datetime import datetime

os.system('cls')

def main():

  print("""
  Help Menu = > 

            For Use Program Need :

            Set IP And Site Address in >

            Host IP Or Site Add >   

            And Wait For Test Port To Open And Close.

                 $ Coded By : Don'tName!
                 $ For : BlackHatsIR
                 $ Telegram Channel : BlackHatsIR
                 $ Join US :)

  """)
main()
#---------------------------------------------------------------
RemoteServer = input("[?] Host IP Or Site Addr ► ")
RemoteServerIP = socket.gethostbyname(RemoteServer)
#Banner Of Script  -->
print("""
    
        [version: 1.0] [Port Scanner]
  #    #   ##   #####  #    # # #    #  ####  
  #    #  #  #  #    # ##   # # ##   # #    # 
  #    # #    # #    # # #  # # # #  # #      
  # ## # ###### #####  #  # # # #  # # #  ### 
  ##  ## #    # #   #  #   ## # #   ## #    # 
  #    # #    # #    # #    # # #    #  ####  

Coded By: @Ac3ess | Channel Telegram: BLACKHATSIR

             * We are anonymuse *
               * We are Free *
              * We are legion *
            * We do not forget *
            * We do not forgive *
                 *(Except US)*

""")
#Threading Count...
print("\n[+]► Please Wait Scanning IP : ► "+RemoteServerIP)
time.sleep(3)

print("\n[+]► Testing IP : ► "+RemoteServerIP)
time.sleep(3)

print("\n[+]► Testing Host : ► "+RemoteServer)
time.sleep(3)

print("\n[+]► Wait Testing... : ► "+RemoteServer)
time.sleep(3)
Time1 = datetime.now()

print("\n[+]► Testing... IP : ► "+RemoteServerIP)
time.sleep(5)
print("\n[+]► Range Port ►► [21,1000] [UDP/TCP/THCP/FTP] Scanning...")
print("\n",Time1)

time.sleep(3)
print("""

[Developer : PyDev] [Telegram ID : Ac3ess] [Telegram Channel : BlackHatsIR] [Telegram Group : DeltaSecurityTM]
                                  ______
    |-----  ||          /\       |        |  /    |     |       /\      _________    /    __ __   ||------
    |    |  ||         /  \      |        | /     |     |      /  \        ---      /       |     ||     |
    | ---|  ||        /----\     |        |/      |-----|     /----\        |       \       |     ||------
    |    |  ||       /------\    |        |\      |-----|    /------\       |        \      |     ||\   
    |-----  ||____  /        \   |______  | \     |     |   /        \      |         \     |     || \  
                                          |  \    |     |  /          \     |         /   __|__   ||  \ 
                                                                                     /    
                                     ** We Are Coders & We Are Programmers **
                                         ** Just Python And BlackHatsIR **
                                                  ** Expect US **

""")
#Get Port Search Opens!
try:

  for port in range(21,1000):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Result = s.connect_ex((RemoteServerIP,port))

    if Result == 0:
      print("[+]►► Port {} :   Is Open ".format(port)+" [DETECTED!]")
    else:
      print("[" + RemoteServerIP+ "]" + " [!] Closed Ports Found!►► ",port)


except KeyboardInterrupt:

 print("[-] Shutting Down...")
 time.sleep(1)
 sys.exit()

except socket.gaierror:

 print("[-] Host Not Found! Please Retry .")
 sys.exit()

except socket.error:

 print("[-] Server Is Offline.")
#Show Times To Finished
Time2 = datetime.now()

Time3 = Time2 - Time1

print("[+] Scan Finished In Time: ►► ",Time3)
#Reshow Banner
print("""

        ►[version: 1.0] [Port Scanner]
  #    #   ##   #####  #    # # #    #  ####  
  #    #  #  #  #    # ##   # # ##   # #    # 
  #    # #    # #    # # #  # # # #  # #      
  # ## # ###### #####  #  # # # #  # # #  ### 
  ##  ## #    # #   #  #   ## # #   ## #    # 
  #    # #    # #    # #    # # #    #  ####  

►Coded By: @Ac3ess  Channel Telegram: BLACKHATSIR

      * We are anonymuse *
         * We are Free *
       * We are legion *
      * We do not forget *
      * We do not forgive *
          *(Except US)*

""")
#GoodLuck To End Of Port_Scanner
print("[†]►► GoodLuck :-) ►►")

time.sleep(5)
sys.exit(0)