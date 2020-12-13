import requests
import argparse
from bs4 import BeautifulSoup, SoupStrainer
import sys
import re


def scraper(url):
    #  Scrapes website for all urls, email addresses and phone numbers
    res = requests.get(url)
    for phone_number in BeautifulSoup(res.text, 'html.parser'):
        digits = re.search(r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?", str(phone_number))
        if digits:
            print('Phone Number: ' + digits.group())
    for email_addy in BeautifulSoup(res.text, 'html.parser'):
        email = re.search(r"([a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.][a-zA-Z]+)", str(email_addy))
        if email:
            print('Email Address: ' + email.group())
    for url in BeautifulSoup(res.text, 'html.parser', parse_only=SoupStrainer('a')):
        if url.has_attr('href'):
            address = url.get('href')
            url = re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                str(address))
            if url:
                print('URL: ' + url.group())

   


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url of page to scrape')
    return parser


def main(args):
    parser = create_parser()
    args = parser.parse_args(args)
    url = args.url
    return scraper(url)


if __name__ == '__main__':
    main(sys.argv[1:])

 
