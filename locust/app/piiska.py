import time
from locust import HttpUser, task, between
class User(HttpUser):
    @task
    def index_page(self):
        self.client.get("/")