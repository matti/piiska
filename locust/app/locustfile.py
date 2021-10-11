from locust import HttpUser, task, between


class User(HttpUser):
    @task
    def root(self):
        self.client.get("/")
