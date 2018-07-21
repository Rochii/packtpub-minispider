#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Web client extracting referral information
of free books available on "https://www.packtpub.com"
and print it on a bash terminal
@author: Roger Truchero

"""

import bs4
import urllib2


class Client(object):
    @staticmethod
    def get_web(url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    @staticmethod
    def parse(html):
        soup = bs4.BeautifulSoup(html, "lxml")
        activities = soup.find_all("div", "dotd-main-book-summary float-left")
        return activities

    @staticmethod
    def explore(activities):
        for act in activities:
            title = act.find("div", "dotd-title").text.strip()
            info = act.find("div", "").text.strip()
            result = ("\x1b[1;33m- Title:\x1b[1;31m " + title + "\x1b[1;37m\n\n\x1b[1;33m- Info:\x1b[1;37m " + info)
            html_info = act.find("ul", "")
            try:
                for features in html_info.find_all("li"):
                    feat = features.text.strip()
                    result += ("\n\t\t * " + feat)
            except AttributeError:
                pass
        return result

    def run(self, url = "https://www.packtpub.com/packt/offers/free-learning"):
        html = self.get_web(url)
        activities = self.parse(html)
        print(self.explore(activities) + "\n\n\x1b[1;33m- Link:\x1b[1;35m " + url)


if __name__ == "__main__":
    client = Client()
    client.run()
