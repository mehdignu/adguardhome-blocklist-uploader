from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import requests
import json
 
## CHANGE HERE ##
# ip address of AdGuard Home
# "http(s)://<adguardHomeIp:<port>"
host = "" 
# user name
userName = ""
# password
password = ""
 
# block list 
# taken from Wally3K's Firebog https://firebog.net/
urls = [
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
"https://v.firebog.net/hosts/static/w3kbl.txt",
"https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt",
"https://someonewhocares.org/hosts/zero/hosts",
"https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts",
"https://winhelp2002.mvps.org/hosts.txt",
"https://v.firebog.net/hosts/neohostsbasic.txt",
"https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt",
"https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt",
"https://adaway.org/hosts.txt",
"https://v.firebog.net/hosts/AdguardDNS.txt",
"https://v.firebog.net/hosts/Admiral.txt",
"https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
"https://v.firebog.net/hosts/Easylist.txt",
"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts",
"https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts",
"https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts",
"https://v.firebog.net/hosts/Easyprivacy.txt",
"https://v.firebog.net/hosts/Prigent-Ads.txt",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts",
"https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
"https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt",
"https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt",
"https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt",
"https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt",
"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt",
"https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt",
"https://v.firebog.net/hosts/Prigent-Crypto.txt",
"https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts",
"https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt",
"https://phishing.army/download/phishing_army_blocklist_extended.txt",
"https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt",
"https://v.firebog.net/hosts/RPiList-Malware.txt",
"https://v.firebog.net/hosts/RPiList-Phishing.txt",
"https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
"https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts",
"https://urlhaus.abuse.ch/downloads/hostfile/",
"https://malware-filter.gitlab.io/malware-filter/phishing-filter-hosts.txt",
"https://v.firebog.net/hosts/Prigent-Malware.txt",
"https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser",
"https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list",
"https://v.firebog.net/hosts/Prigent-Adult.txt",
"https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt",
]
 
# Create a session object to maintain cookies across requests
session = requests.Session()

# Set headers for JSON content
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Login
login_response = session.post(f"{host}/control/login", json={"name": userName, "password": password}, headers=headers)

# Check if login is successful
if login_response.status_code == 200:
    print("Logged in successfully.")
else:
    print(f"Login failed with status code {login_response.status_code} and message {login_response.text}")
    exit()  # Exit if login fails

# Add URLs
for url in urls:
    # Construct the payload for each URL
    filter_payload = {"url": url, "name": url, "whitelist": False}

    # Send the request to add the URL
    add_url_response = session.post(f"{host}/control/filtering/add_url", json=filter_payload, headers=headers)

    # Check response status
    if add_url_response.status_code == 200:
        print(f"Successfully added URL: {url}")
    else:
        print(f"Failed to add URL: {url}. Status code: {add_url_response.status_code} Response: {add_url_response.text}")