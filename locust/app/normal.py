import os
from pprint import pprint

from locust import HttpLocust, TaskSet, between
from bs4 import BeautifulSoup
import urllib.parse as urlparse

import redis
r = redis.Redis(host='redis', port=6379, db=0)

def get(l):
    while True:
        random_path = r.srandmember('paths')

        if random_path == None:
            path = "/"
            break

        path = random_path.decode('utf-8')
        break
        # if path.startswith('/'):
        #     break

    with l.client.get(path, catch_response=True) as response:
        if response.headers.get('content-type', None) == None:
            return

        if response.headers['content-type'].find("html") > 0:
            if response.status_code == 404:
                if not r.sismember("404:set", path):
                    r.sadd("404:set", path)
                    r.lpush("404:queue", path)

                return response.success()

            try:
                bs = BeautifulSoup(response.content, features='html.parser')
            except:
                return response.success()

            base_elem = bs.find('base')
            if base_elem:
                base_url = base_elem.get("href")
                base_path = urlparse.urlsplit(base_url).path
            else:
                base_path = None

            a_elems = bs.findAll('a')
            area_elems = bs.findAll('area')
            link_elems = bs.findAll('link')

            iframe_elems = bs.findAll('iframe')
            frame_elems = bs.findAll('frame')
            img_elems = bs.findAll('img')
            script_elems = bs.findAll('script')

            links = []
            for e in link_elems:
                if e.get('rel') == "alternate":
                    continue
                links.append(e.get('href'))

            for e in a_elems+area_elems:
                links.append(e.get('href'))
            for e in iframe_elems+frame_elems+img_elems+script_elems:
                links.append(e.get('src'))

            for link in links:
                if link == None:
                    continue

                if link.find("mailto:") > 0:
                    continue
                if link.find("@") > 0:
                    continue
                if link.startswith("//"):
                    continue
                if link.find("()") > 0:
                    continue
                if link.find(";base64,") > 0:
                    continue

                parts = urlparse.urlsplit(link)
                new_path = parts.path
                hostname = parts.hostname

                if hostname == None:
                    pass
                else:
                    if hostname != l.hostname:
                        continue

                if new_path == None:
                    continue
                elif new_path == "":
                    continue
                else:
                    if not new_path.startswith("/"):
                        if base_path:
                            new_path = base_path + new_path
                        else:
                            net_path = path + "/" + new_path

                    r.sadd('paths', new_path)

class UserBehavior(TaskSet):
    tasks = {get: 1}

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = urlparse.urlsplit(self.locust.host).hostname

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0.925, 0.925)
