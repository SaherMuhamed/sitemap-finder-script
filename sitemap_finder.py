import re
import sys
import urllib3
import requests
import datetime as dt
from art import sitemap_art
import urllib.parse

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write("Please update and make sure you use the command python3 sitemap_finder.py <url>\n\n")
    sys.exit(0)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disable warnings related to insecure requests
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}  # It will send the request like browser
target_links_list = []


def get_details():
    print("---------------------")
    print("Start time      : " + str(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")))
    print("Base URL        : " + sys.argv[1])
    print("Recursive       : yes")
    print("---------------------\n")


def extract_links(website_url):
    try:
        return re.findall('href="(.*?)"', requests.get(url=website_url, headers=HEADERS, timeout=7).text)
    except requests.exceptions.ConnectionError:
        pass


def crawl(url):
    href_links = extract_links(website_url=url)
    for link in href_links:
        link = urllib.parse.urljoin(base=url, url=link)

        if "#" in link:  # remove the part that loads different part in the same html page
            link = link.split("#")[0]
        if url in link and link not in target_links_list:  # remove external links <facebook, linkedin, youtube, etc..>
            target_links_list.append(link)
            print(link)
            crawl(url=link)  # recursive mapping whole website


def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s http://www.example-website.com" % sys.argv[0] + "\n")
        sys.exit(-1)
    print(sitemap_art)
    get_details()
    try:
        crawl(url=sys.argv[1])  # calling crawl function and passing args <second index> in terminal
    except KeyboardInterrupt:
        print("\n[*] Detected 'ctrl + c' pressed, program terminated.")
        sys.exit(0)


if __name__ == "__main__":
    main()
