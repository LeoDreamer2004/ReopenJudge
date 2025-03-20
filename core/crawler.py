"""
A crawler for OpenJudge.cn
NOTE: This script is not used in the project, but it is a good example of how to use Django ORM in a standalone script.
NOTE: The script will DELETE all existing data in the tables, so be careful when running it.
"""


import os
import random
import time
from typing import List
from datetime import datetime
import requests
import django
from django.utils import timezone
from bs4 import BeautifulSoup, Tag

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reopenjudge.settings')
django.setup()


def raw_to_datetime(raw_time: str):
    naive_datetime = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S")
    return timezone.make_aware(naive_datetime)


class Crawler:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching URL {self.url}: {e}")

        if response.status_code == 200:
            response.close()
            soup = BeautifulSoup(response.text, "html.parser")
            return soup
        raise ConnectionError(
            f"Error fetching URL {self.url} with status code {response.status_code}")


def create_super_admin():
    from oiproblems.models import User
    User.objects.create(id=1, username="admin", password="admin", email="123456789@qq.com")


def crawl_announcements():
    crawler = Crawler("http://openjudge.cn/")
    soup = crawler.fetch()
    ann: List[Tag] = soup.find("div", class_="announcements").find_all("li")

    from oiproblems.models import Announcement

    Announcement.objects.all().delete()
    # for a in ann:
    #     date_span = a.find("span", class_="date")
    #     date = raw_to_datetime(date_span.find("abbr")["title"])
    #     content = date_span.find_next_sibling()
    #     if content is None:  # raw text
    #         content = date_span.next_sibling.strip()
    #     else:
    #         content = content.text
    #     Announcement.objects.create(date=date, content=content)
    # print("INDEX: Done on announcements, inserted", len(ann), "announcements")


def crawl_groups():
    crawler = Crawler("http://openjudge.cn/groups")
    soup = crawler.fetch()
    main_div = soup.find("div", id="main")

    from oiproblems.models import Group

    Group.objects.all().delete()
    group_type_map = {
        "college-teaching": "A",
        "college-competition": "B",
        "high-school-teaching": "C",
        "high-school-competition": "D",
        "interest-group": "E"
    }

    for c in main_div.children:
        if c.name == "h2":
            group_type = group_type_map[c["id"]]
        if c.name != "ul":
            continue

        # group list with the given type
        for i, group in enumerate(c.find_all("li")):
            small_logo = group.find("img", class_="group-logo")["src"]
            logo_id = Group.get_logo_id(small_logo)
            a = group.find_all("a")[-1]
            url = a["href"]
            name = a["title"]

            # go to the href and crawl
            crawler = Crawler(url)
            try:
                soup = crawler.fetch()
            except ConnectionError as e:
                print(f"GROUPS: {e}")
                continue

            description = soup.find("div", class_="group-description").text.strip()

            Group.objects.create(name=name, url=url, logo_id=logo_id,
                                 description=description, group_type=group_type)
            time.sleep(0.5)
            print(f"GROUPS: Done {i + 1} groups in type {group_type}")
    print("GROUPS: Done on all groups")


if __name__ == "__main__":
    # create_super_admin()
    # crawl_announcements()
    crawl_groups()
