from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(100, 5)  # Time between 100 requests in 5 seconds

    @task
    def my_task(self):
        self.client.get("https://example.com")