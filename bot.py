from selenium import webdriver
from selenium.webdriver.firefox import options
import requests
import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random


# Scrooling fun
def scrooling_dowon(a,b):
    number = random.randint(a,b)
    body = driver.find_element_by_tag_name("body")
    for j in range(number):
        body.send_keys(Keys.PAGE_DOWN)
        sleep(.3)
    
def wait(c,d):
    timewait = random.randint(c,d)
    sleep(timewait)


#TODO replace with existing profile ID. Define the ID of the browser profile, where the code will be executed.
with open("profiles.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mla_profile_id = row[0]
        mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id
        """
        Send GET request to start the browser profile by profileId. Returns response in the following format: '{"status":"OK","value":"http://127.0.0.1:XXXXX"}', where XXXXX is the localhost port on which browser profile is launched. Please make sure that you have Multilogin listening port set to 35000. Otherwise please change the port value in the url string
        """
        resp = requests.get(mla_url)
        json = resp.json()
        print (json)
        #Define DesiredCapabilities
        opts = options.DesiredCapabilities()
        #Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
        driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})
        #Perform automation
        driver.get('https://www.facebook.com/')
        sleep(2)

        #clicking on comments

        # top_feed = driver.find_element_by_id("m_newsfeed_stream")
        # newsfeed = top_feed.find_element_by_id("MNewsFeed")
        # Sections = newsfeed.find_elements_by_tag_name("section")
        # article = Sections[0].find_elements_by_tag_name("article")
        # # tag = article[0].find_element_by_class_name("_7ab_")
        # comment = article[0].find_elements_by_class_name("_52jj")
        # comment[1].click()
        # wait = random.randint(1,3)
        # sleep(wait)
        # scrooling_dowon(30)
        # wait = random.randint(2,5)
        # sleep(wait)
        # driver.quit()
    
    
    #stories seeing

        # try:
        #     driver.find_element_by_xpath("//*[@id='story_tray']/div[2]").click()
        # # stories[2].click()
        #     sleep(10)
        # except:
        #     pass

    # Scrooling

        # body = driver.find_element_by_tag_name("body")
        # for j in range(30):
        #     body.send_keys(Keys.PAGE_DOWN)
        #     sleep(.5)
        # driver.find_element_by_xpath("//*[@id='m-top-of-feed']/section/article/div/div[2]/div[1]/a/div/div").click()

    #Top feed has two element one is photo and one is ad.i completed the photo ad is remaining. 


        # try:
        #     top_feed = driver.find_element_by_id("m_newsfeed_stream")
        #     top_feed_section = top_feed.find_element_by_tag_name("section")
        #     top_article = top_feed_section.find_element_by_tag_name("article")
        #     itag = top_article.find_element_by_class_name("_7ab_")
        #     itag.click()
        #     wait = random.randint(1,3)
        #     sleep(wait)
        # except:
        #     pass
        

        #opening ads



        # top_feed = driver.find_element_by_id("m_newsfeed_stream")
        # adarticle = top_feed.find_elements_by_tag_name("article")
        # print(len(adarticle))
        # scrooling_dowon(6)
        # for ar in adarticle:
        #     try:
        #         ar.find_element_by_tag_name("iframe")
        #         print("done")
        #         ar.find_element_by_class_name("_2rea").click()
        #         driver.switch_to_window(driver.window_handles[1])
        #         sleep(5)
        #         driver.close()
        #         break
        #     except:
        #         print("unable")
        # driver.switch_to_window(driver.window_handles[0])
        # driver.quit()

        
        
        #Profile clicking


        # top_feed = driver.find_element_by_id("m_newsfeed_stream")
        # Profileid = top_feed.find_elements_by_tag_name("article")
        # slector = random.randint(0,5)
        # Profileid[slector].find_element_by_tag_name("strong").click()
        # wait(1,3)
        # scrooling_dowon(2,10)
        # driver.quit()


        