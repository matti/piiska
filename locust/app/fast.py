from locust import HttpLocust, TaskSet, task
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):
  @task
  def index(self):
    response = self.client.get("/")

class WebsiteUser(FastHttpLocust):
  task_set = MyTaskSet
  min_wait = 1000
  max_wait = 1000
