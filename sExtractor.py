import sys
import urllib3
import argparse
import requests
import colorama
import datetime as dt
from art import sitemap_art
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write("Please update and make sure you use the command python3 link_extractor.py <url>\n\n")
    sys.exit(0)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disable warnings related to insecure requests
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}  # It will send the request like browser

internal_urls = set()
external_urls = set()

total_urls_visited = 0


def args():
    parser = argparse.ArgumentParser(description="------- sExtractor - Link Extractor Tool by Saher Muhamed "
                                                 "16/06/2024 -------")
    parser.add_argument("-u", "--url", dest="target_url", help="The URL to extract links from")
    parser.add_argument("-m", "--max-urls", dest="max_urls", help="Maximum number of URLs to crawl (default=7)", default=7, type=int)
    if not parser.parse_args().target_url:
        parser.error("[-] Please specify website url, or type it correctly, ex: http://target-website.com/")

    return parser.parse_args()


def print_details():
    print("══════════════════════════════════════════")
    print("🕰️  Start Time   : " + str(dt.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
    print("🎯 Target URL   : " + args().target_url)
    print("🚀 Maximum URLs : " + str(args().max_urls))
    print("══════════════════════════════════════════\n")


def is_url_valid(url):
    return bool(urlparse(url).scheme) and bool(urlparse(url).netloc)


def extract_website_links(url):
    urls = set()
    soup = BeautifulSoup(requests.get(url=url, headers=HEADERS).content, "html.parser", from_encoding="iso-8859-1")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_url_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                print(f"[!] External link: {href}")
                external_urls.add(href)
            continue
        print(f"[*] Internal link: {href}")
        urls.add(href)
        internal_urls.add(href)
    return urls


def crawl(url, max_urls=7):
    global total_urls_visited
    total_urls_visited += 1
    print(f"{colorama.Fore.YELLOW}    ==> Current URL: {url}{colorama.Fore.RESET}")
    links = extract_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)  # recursive mapping whole website


if __name__ == "__main__":
    options = args()
    print(sitemap_art)
    print_details()
    domain_name = urlparse(options.target_url).netloc
    crawl(url=options.target_url)

    print("\n╔═══════════════════════════════╗")
    print("║ [+] Total Internal links: " + str(len(internal_urls)) + "  ║")
    print("║ [+] Total External links: " + str(len(external_urls)) + "   ║")
    print("║ [+] Total URLs: " + str(len(external_urls)) + str(len(internal_urls)) + "            ║")
    print("╚═══════════════════════════════╝\n")

    # save the `internal links` to a text file
    with open(file=f"extracted_links/{domain_name}_internal_links.txt", mode="w") as file:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=file)

    # save the `external links` to a text file
    with open(file=f"extracted_links/{domain_name}_external_links.txt", mode="w") as file:
        for external_link in external_urls:
            print(external_link.strip(), file=file)
