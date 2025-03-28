# bot_functions.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests

class FacebookBot:
    def __init__(self):
        self.driver = None
        self.mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='
    
    def start_profile(self, profile_id):
        """Start browser profile using Multilogin"""
        resp = requests.get(self.mla_url + profile_id)
        json = resp.json()
        self.driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})
        self.driver.get('https://www.facebook.com/')
        time.sleep(random.uniform(2, 5))
    
    def close_profile(self):
        """Close current browser profile"""
        if self.driver:
            self.driver.quit()
    
    def random_delay(self, min_sec=1, max_sec=10):
        """Random delay between actions"""
        time.sleep(random.uniform(min_sec, max_sec))
    
    def scroll_randomly(self, min_scrolls=3, max_scrolls=10):
        """Dynamic scrolling with random page up/down"""
        scrolls = random.randint(min_scrolls, max_scrolls)
        body = self.driver.find_element(By.TAG_NAME, "body")
        
        for _ in range(scrolls):
            if random.choice([True, False]):
                body.send_keys(Keys.PAGE_DOWN)
            else:
                body.send_keys(Keys.PAGE_UP)
            self.random_delay(0.5, 1.5)
    
    def watch_stories(self):
        """Watch Facebook stories"""
        try:
            story_tray = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='story_tray']/div[2]"))
            )
            story_tray.click()
            self.random_delay(35, 50)  # Watch time
            
            # Try to close story viewer
            try:
                close_btn = self.driver.find_element(By.XPATH, "//*[@id='story_bucket_viewer_content']/div/div[3]/span[2]/i")
                close_btn.click()
            except:
                self.driver.get("https://m.facebook.com/")
                
        except Exception as e:
            print(f"Error watching stories: {e}")
            self.driver.get("https://www.facebook.com/")
    
    def click_random_posts(self):
        """Click on random posts in newsfeed"""
        try:
            articles = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
            )
            
            if articles:
                random.choice(articles).click()
                self.random_delay(8, 15)
                self.driver.execute_script("window.history.go(-1)")
                
        except Exception as e:
            print(f"Error clicking random posts: {e}")
    
    def click_sponsored_ads(self):
        """Click on sponsored ads"""
        try:
            articles = self.driver.find_elements(By.TAG_NAME, "article")
            for article in articles:
                try:
                    # Check if article contains an ad
                    article.find_element(By.TAG_NAME, "iframe")
                    ad_link = article.find_element(By.CLASS_NAME, "_2rea")
                    ad_link.click()
                    
                    # Switch to new tab
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.random_delay(10, 25)
                    
                    # Close ad tab and switch back
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    break
                    
                except:
                    continue
                    
        except Exception as e:
            print(f"Error clicking ads: {e}")
    
    def check_user_profiles(self):
        """Click on random user profiles"""
        try:
            articles = self.driver.find_elements(By.TAG_NAME, "article")
            if articles:
                profile = random.choice(articles).find_element(By.TAG_NAME, "strong")
                profile.click()
                self.random_delay(10, 15)
                self.scroll_randomly(2, 5)
                self.driver.execute_script("window.history.go(-1)")
                
        except Exception as e:
            print(f"Error checking user profiles: {e}")
    
    def read_comments(self):
        """Open and read comments"""
        try:
            articles = self.driver.find_elements(By.TAG_NAME, "article")
            if articles:
                comment_btn = articles[0].find_elements(By.CLASS_NAME, "_52jj")[1]
                comment_btn.click()
                self.random_delay(5, 8)
                self.scroll_randomly(5, 10)
                self.driver.execute_script("window.history.go(-1)")
                
        except Exception as e:
            print(f"Error reading comments: {e}")
    
    def watch_videos(self):
        """Watch random videos"""
        try:
            video = self.driver.find_element(By.CLASS_NAME, "_53mw")
            video.click()
            self.random_delay(30, 60)  # Watch time
            
        except Exception as e:
            print(f"Error watching videos: {e}")
    
    def do_likes(self):
        """Like random posts"""
        try:
            articles = self.driver.find_elements(By.TAG_NAME, "article")
            likes_to_do = random.randint(3, 5)
            
            for _ in range(likes_to_do):
                if articles:
                    article = random.choice(articles)
                    like_btn = article.find_elements(By.CLASS_NAME, "_52jj")[0]
                    like_btn.find_element(By.TAG_NAME, "div").click()
                    self.random_delay(1, 3)
                    
                    # Select reaction if available
                    try:
                        reactions = self.driver.find_elements(By.CLASS_NAME, "_uah")
                        if reactions:
                            random.choice(reactions).find_element(By.TAG_NAME, "i").click()
                    except:
                        pass
                    
                    self.random_delay(2, 4)
                    
        except Exception as e:
            print(f"Error doing likes: {e}")
    
    def do_comments(self):
        """Comment on random posts"""
        try:
            articles = self.driver.find_elements(By.TAG_NAME, "article")
            comments_to_do = random.randint(2, 4)
            sample_comments = [
                "Nice post!", "Great content!", "Interesting!", 
                "Thanks for sharing!", "Awesome!", "Love this!"
            ]
            
            for _ in range(comments_to_do):
                if articles:
                    article = random.choice(articles)
                    
                    # Open comment section
                    comment_btn = article.find_element(By.CLASS_NAME, "_15kq")
                    comment_btn.click()
                    self.random_delay(3, 5)
                    
                    # Type and submit comment
                    comment_box = self.driver.find_element(By.ID, "composerInput")
                    comment = random.choice(sample_comments)
                    comment_box.send_keys(comment)
                    self.random_delay(1, 2)
                    
                    submit_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
                    submit_btn.click()
                    self.random_delay(3, 5)
                    
                    self.driver.get("https://www.facebook.com/")
                    
        except Exception as e:
            print(f"Error doing comments: {e}")
