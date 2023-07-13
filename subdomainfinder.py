# Import relevant modules
import requests
import sys

#Checking for zero arguements
if len(sys.argv) < 2:
    print(" Usage: "+ sys.argv[0]+ " <url>")
    sys.exit(1)

#open, read and format the text file
sublist_ = open("subdomains-10000.txt").read()
subs = sublist_.splitlines()

print("Printing Found Subdomains....")

#Get valid subdomains
for sub in subs:
    url_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_check)
    
    except requests.ConnectionError:
        pass
    else:
        print("Valid domain: ", url_check)


