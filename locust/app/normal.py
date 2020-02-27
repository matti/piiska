from locust import HttpLocust, TaskSet, between

def get(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {get: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0.925, 0.925)
