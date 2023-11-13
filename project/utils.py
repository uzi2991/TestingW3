from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

def twitter_login(driver, username, password):
    # navigate to the login page
        driver.get("https://twitter.com/i/flow/login")

        # username input
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        username_input.clear()
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)
        
        # password input
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        
        # wait a few seconds so the login process is completed
        time.sleep(10)
        
def generate_random_tweet():
    # Define the maximum length of the tweet
    max_length = 50

    # Define the characters allowed in the tweet
    allowed_characters = string.ascii_letters + string.digits + ' .,?!@#$%^&*()'

    # Generate a random length for the tweet (up to the maximum length)
    tweet_length = random.randint(1, max_length)

    # Generate a random tweet by selecting random characters from the allowed set
    tweet = ''.join(random.choice(allowed_characters) for _ in range(tweet_length))

    return tweet