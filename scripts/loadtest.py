from locust import HttpUser, task, between

import random
import os


class WebsiteTestUser(HttpUser):
    
    wait_time = between(1, 1)
    
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
        self.client.get("/v1/cohorts", json={'identifier': user_id, 'experiment': experiment})


if __name__ == "__main__":
    os.system("locust -f scripts/loadtest.py --host http://api.getcohorts.com --users 500 --spawn-rate 100 --run-time 60s --headless")
