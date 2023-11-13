from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import DRIVER_PATH, TWITTER_PASSWORD, TWITTER_USERNAME
import time
import unittest
from utils import twitter_login, generate_random_tweet

class TwitterTest(unittest.TestCase):
    

    @classmethod
    def setUpClass(inst):
        # Init driver
        o = webdriver.ChromeOptions()
        o.add_experimental_option("detach", True)
        s = webdriver.ChromeService(DRIVER_PATH)
        inst.driver = webdriver.Chrome(service=s, options=o)
        inst.driver.maximize_window()
    

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
        
    def test_1_login_incorrect_password(self):
        print("TEST 1: LOGIN INCORRECT PASSWORD")
        
        # login with incorrect password
        twitter_login(self.driver, TWITTER_USERNAME, "INCORRECT PASSWORD")
        
        # check if still at login page
        self.assertEqual(self.driver.current_url, "https://twitter.com/i/flow/login")
    
    def test_2_login_success(self):
        print("TEST 2: LOGIN SUCCESS")
        
        # login with correct password
        twitter_login(self.driver, TWITTER_USERNAME, TWITTER_PASSWORD)
        
        # check if redirected to home page
        self.assertEqual(self.driver.current_url, "https://twitter.com/home")
  
    def test_3_create_tweet(self):
        print("TEST 3: CREATE NEW TWEET")
        
        # generate random tweet
        TWEET_CONTENT = generate_random_tweet()
        
        # new tweet input
        tweet_text_box = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
        tweet_text_box.send_keys(TWEET_CONTENT)
        
        #submit tweet
        tweet_submit_btn = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
        tweet_submit_btn.click()
        time.sleep(10)
        
        # go to profile page
        self.driver.get("https://twitter.com/" + TWITTER_USERNAME)
        
        # get the latest tweet
        latest_tweet = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//article[@data-testid='tweet']//div[@data-testid='tweetText']")))
        ActionChains(self.driver).move_to_element(latest_tweet).perform()
        time.sleep(10)

        # check the content of the latest tweet
        self.assertEqual(latest_tweet.get_attribute("textContent"), TWEET_CONTENT)
     
        
    

if __name__ == '__main__':
    unittest.main()
        
        







