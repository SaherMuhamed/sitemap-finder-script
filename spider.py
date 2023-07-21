#!/usr/bin/env python3

import re
import requests
import urllib.parse
from colorama import Fore
from optparse import OptionParser


def get_argument():
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="target_url",
                      help="Specify the url for your target website. Example: --url https://target.com/")
    (option, arguments) = parser.parse_args()
    if not option.target_url:
        parser.error("[-] Please specify the target url, or type it correctly, ex: -u target.com")
    return option


def extract_links(url):
    response = requests.get(url=url)
    return re.findall(pattern=b'(?:href=")(.*?)"', string=response.content)


def scan_target(url):
    href_links = extract_links(url=url)
    for link in href_links:
        link = urllib.parse.urljoin(base=url, url=link.decode("utf-8"))
        if "#" in link:
            link = link.split("#")[0]
        if url in link and link not in target_links:
            target_links.append(link)
            print(Fore.GREEN + f"[+] {link}")
            scan_target(url=link)  # recursive function


print("")
target_links = []
options = get_argument()

try:
    scan_target(options.target_url)
    print("")
except requests.exceptions.InvalidURL:
    pass
except requests.exceptions.ConnectionError:
    pass
except KeyboardInterrupt:
    print("\n[*] Detected 'ctrl + c' pressed, program terminated.\n")
