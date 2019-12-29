import requests
import os

o = open ("others.txt", "a+") #sorted list of non-wp sites
wp = open ("wp.txt", 'a+') #sorted list of wp-sites
wl = open ("list.txt").read().split("\n") #a list of websites to scan

#make it pretty
class tcolor:
    yellow = '\33[33m'
    red    = '\33[31m'
    green  = '\33[32m'

def splitter(host):
        host = host
        print (tcolor.green+"Running.. "+tcolor.yellow+"")
        
        try:
            test_response = requests.get(host+'/').text
        except requests.exceptions.HTTPError:
            o.write(host+'#notWP\n')
            print (tcolor.red+"[ERROR] "+tcolor.yellow+"Connection Error")
            pass
        except requests.exceptions.ConnectionError:
            o.write(host+'#notWP\n')
            print(tcolor.red+"[ERROR] "+tcolor.yellow+"Connection Error")
            pass
        else:
            if "wp-content" in test_response:
                wp.write(host+'\n')
                print(tcolor.yellow+"[OK] "+host+ tcolor.green + " is a WordPress site")
            else:
                o.write(host+'#NotWP\n')
                print(tcolor.yellow+"[ERROR] "+host +tcolor.red+" is not a WordPress site")

def banner():
    os.system("clear")
    
    print("###########################################################")
    print("#        Tool: WordPress Site Detector                    #")
    print("#        Detect if a website is using WordPress    	  	  #")
    print("###########################################################")

def s():
    banner()
    for item in wl:
        if (item == ""):
            continue
        splitter(item)

s()
