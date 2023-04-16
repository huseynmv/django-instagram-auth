# # tasks.py
# from celery import shared_task
# from selenium import webdriver
# from time import sleep
# from django.contrib.auth.models import User
# from selenium.webdriver.common.by import By

# @shared_task
# def update_instagram_counts(user_email):
#     user = User.objects.get(email=user_email)
#     print(user)
#     # browser = webdriver.Chrome()
#     # browser.get('https://www.instagram.com/')
#     # sleep(1)

#     # # Log in to Instagram
#     # username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
#     # password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

#     # username_input.send_keys(user.instagram_username)
#     # password_input.send_keys(user.instagram_password)

#     # login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     # login_button.click()

#     # sleep(10)
#     # browser.get(f'https://www.instagram.com/{user.instagram_username}')
#     # sleep(10)

#     # # Get follower and following counts
#     # follower_count = int(browser.find_element(By.XPATH, ".//*[contains(text(), 'followers')]/span").text)
#     # following_count = int(browser.find_element(By.XPATH, ".//*[contains(text(), 'following')]/span").text)

#     # # Update user's follower and following counts
#     # user.followers = follower_count
#     # user.following = following_count
#     # user.save()

#     # browser.close()


# import time
# from celery import shared_task
# @shared_task

# def print_something():
#     while True:
#         print("Something")
#         time.sleep(1)


from celery import shared_task
from datetime import datetime

from celery import shared_task
from datetime import datetime, timedelta
from core.celery import app
# from .views import home
@shared_task
def print_something():
    return "Something at ", datetime.now()
# @shared_task
# def hhome(self):
#     home(self.request)
# @shared_task
# def run_print_something():
#     print_something.delay()
#     run_print_something.apply_async(countdown=1) # reschedule the task to run again in 60 seconds
