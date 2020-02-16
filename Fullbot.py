from selenium import webdriver
from selenium.webdriver.firefox import options
import requests
import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random


flagg=False
counter=0
def wait(c,d):
    timewait = random.randint(c,d)
    sleep(timewait)
def set_read_to_zero():
    with open("continue.txt",'w') as txt:
        txt.write(str(0))
def file_check():
    try:
        with open('continue.txt','r') as txt:
            print("continue.txt present")
    
    except FileNotFoundError:
        set_read_to_zero()
        print('continue.txt created')
    
def read_continue():
    with open("continue.txt",'r') as txt:
        read=txt.read()
    return int(read)


# In[13]:


def scrooling_dowon(a,b,up=True):
    number = random.randint(a,b)
    body = driver.find_element_by_tag_name("body")
    for j in range(number):
        body.send_keys(Keys.PAGE_DOWN)
        sleep(.5)
    if(up):
        number=random.randint(int(a/2),int(b/2))
        for i in range(number):
            body.send_keys(Keys.PAGE_UP)
            sleep(1.5)
        check=random.randint(0,1)
        number=random.randint(a-1,b-1)
        if(check):
            for i in range(number):
                body.send_keys(Keys.PAGE_DOWN)
                sleep(0.5)


# In[14]:


def story_seeing():
          #stories seeing
            try:

                driver.find_element_by_xpath("//*[@id='story_tray']/div[2]").click()
                low=random.randint(35,42)
                high=random.randint(48,52)
                wait(low,high)
                flag=False
                try:
                    driver.find_element_by_xpath("//*[@id='story_bucket_viewer_content']/div/div[3]/span[2]/i").click()
                except:
                    driver.get("https://m.facebook.com/")
                    wait(1,3)
            except:
                global counter
                counter+=1
                print("Story seeing error")
                driver.get("https://www.facebook.com/")
                wait(5,10)

                #driver.find_element_by_xpath("//*[@id='RFMSacredModalCard_0_0']/form/div[1]/div/header/div/a/i").click()


# In[15]:


def clicking_on_pics():
    try:
        wait(4,6)
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        top_feed_section = top_feed.find_element_by_tag_name("section")
        top_article = top_feed_section.find_element_by_tag_name("article")
        itag = top_article.find_element_by_class_name("_7ab_")
        itag.click()
        wait(8,12) #would be 7,10
        driver.execute_script("window.history.go(-1)")
    except:
        global counter
        global counter
        counter+=1
        print("error while clicking on pics")


# In[16]:


def opening_ad():
    try:
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        adarticle = top_feed.find_elements_by_tag_name("article")
        scrooling_dowon(1,3,up=False)
        for ar in adarticle:
            try:
                ar.find_element_by_tag_name("iframe")
                ar.find_element_by_class_name("_2rea").click()
                sleep(1.5)
                driver.switch_to_window(driver.window_handles[1])
                if(random.randint(0,1)):
                    wait(10,20)
                    scrooling_dowon(1,3,up=False)
                wait(15,25)
                driver.close()
                break
            except:
                pass
        driver.switch_to_window(driver.window_handles[0])
        sleep(5)
                # profile clicking
    except:
        global counter
        counter+=1
        print("error while opening ads")
        pass


# In[17]:


def clicking_on_profile():
    try:
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        Profileid = top_feed.find_elements_by_tag_name("article")
        slector = random.randint(0,5)
        Profileid[slector].find_element_by_tag_name("strong").click()
        wait(10,12)
        scrooling_dowon(2,10,up=False)
        wait(4,6)
        driver.execute_script("window.history.go(-1)")
        driver.get("https://m.facebook.com/")
        sleep(5)

    except:
        global counter
        counter+=1
        print("Error while opening other's profile")
        pass


# In[18]:


def clicking_on_comments():
    try:
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        newsfeed = top_feed.find_element_by_id("MNewsFeed")
        Sections = newsfeed.find_elements_by_tag_name("section")
        article = Sections[0].find_elements_by_tag_name("article")
        # tag = article[0].find_element_by_class_name("_7ab_")
        comment = article[0].find_elements_by_class_name("_52jj")
        comment[1].click()
        wait(5,7)
        scrooling_dowon(5,10)
        driver.execute_script("window.history.go(-1)")
        sleep(5)
    except:
        global counter
        counter+=1
        print("error while checking comments")
        


# In[19]:


def playing_video():
    try:
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        videoid = top_feed.find_element_by_class_name("_53mw")
        videoid.click()
        wait(30,60)
    except:
        global counter
        counter+=1
        print("error while playing video")
        


# In[31]:

admin = input("Please input name of wifi : ")
password = input("Please input password of wifi : ")




funcs=[scrooling_dowon,story_seeing,clicking_on_pics,opening_ad,clicking_on_profile,clicking_on_comments,playing_video]
n_funcs=len(funcs)
rows=[]
file_check()
with open("profiles.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append(row)
    start=read_continue()
    start=start+1 if start!=0 else start
    for row in rows[start:]: 
        flagg=False
        counter=0
        print("{}  {}".format(row[1],row[0]))
        # try:
        mla_profile_id = row[0]
        mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id
        """
        Send GET request to start the browser profile by profileId. Returns response in the following format: '{"status":"OK","value":"http://127.0.0.1:XXXXX"}', where XXXXX is the localhost port on which browser profile is launched. Please make sure that you have Multilogin listening port set to 35000. Otherwise please change the port value in the url string
        """
        resp = requests.get(mla_url)
        json = resp.json()
        print(json)
        #Define DesiredCapabilities
        opts = options.DesiredCapabilities()
        #Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
        driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})

        #Perform automation
        driver.get('https://www.facebook.com/')
        sleep(2)
        
        #
        done=[]
        runs=random.randint(2,n_funcs-1)
        for _ in range(runs):
            
            while(1):
                index=random.randint(0,n_funcs-1)
                if index not in done:
                    break
            if(funcs[index]==scrooling_dowon):
                flagg=True
                funcs[index](4,6)

            else:
                funcs[index]()
            done.append(index)
            wait(5,10)
        if(flagg):
            if(counter==(runs-1)):
                print("\n\n------------------------------\nWarning! This account has been Blocked.\n------------------------------\n")

        elif(counter==runs):
            print("\n\n------------------------------\nWarning! This account has been Blocked.\n------------------------------\n")
        with open('continue.txt','w') as txt:
            txt.write(str(rows.index(row)))
        if(rows[-1]==row):
            set_read_to_zero()
        wait(5,10)

        driver.close()




        


