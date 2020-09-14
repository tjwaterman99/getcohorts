from locust import HttpUser, task, between

import random
import os


class WebsiteTestUser(HttpUser):

    wait_time = between(0.25, 0.25)

    def on_start(self):
        """
        Called before any task is scheduled
        """

        pass

    def on_stop(self):
        """
        Called after all tasks have stopped
        """

        pass

    @task(1)
    def get_cohort(self):
        user_id = str(random.random())
        experiment = 'test'
        self.client.get("/v1/cohorts", json={
            'identifier': user_id,
            'experiment': experiment
        })

    @task(1)
    def get_seed(self):
        user_id = str(random.random())
        experiment = 'test'
        self.client.get("/v1/seeds", json={
            'identifier': user_id,
            'experiment': experiment
        })

    @task(1)
    def get_health(self):
        self.client.get("/v1/health")


if __name__ == "__main__":
    os.system("""locust -f scripts/loadtest.py \\
                 --host http://api.getcohorts.com \\
                 --users 200 \\
                 --spawn-rate 100 \\
                 --run-time 60s \\
                 --headless""")
