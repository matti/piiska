from locust import HttpUser, TaskSet, task
from locust.contrib.fasthttp import FastHttpUser

class MyTaskSet(TaskSet):
  @task
  def index(self):
    response = self.client.get("/")

class WebsiteUser(FastHttpUser):
  task_set = MyTaskSet
  min_wait = 1000
  max_wait = 1000
