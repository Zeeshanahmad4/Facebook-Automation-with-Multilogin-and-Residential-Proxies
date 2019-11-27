#driver.execute_script("arguments[0].click();", comm)
#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[348]:


#----------------------------------Likes----------------


# In[349]:



def do_like():
    try:
        top_feed = driver.find_element_by_id("m_newsfeed_stream")
        newsfeed = top_feed.find_element_by_id("MNewsFeed")
        Sections = newsfeed.find_elements_by_tag_name("section")
        print("No of Sections found:",len(Sections))

        articles=[]
        for section in Sections:
            try:
                if(section.find_elements_by_tag_name("article")!=[]):
                    articles.extend(section.find_elements_by_tag_name("article"))
            except:
                pass
        print("No of Articles found: ",len(articles))
        runns=random.randint(3,4)
        print("No of likes to be done:",runns)
        Done=[]
        for _ in range(runns):
            while(1):
                a_index=random.randint(0,(len(articles)-1))
                if a_index not in Done:
                    break
            Done.append(a_index)
            like_obj=articles[a_index].find_elements_by_class_name("_52jj")[0]
            like_object=like_obj.find_element_by_tag_name('div')

            #like_object.click()
            driver.execute_script("arguments[0].click();", like_object)
            sleep(1.5)
            uah=driver.find_elements_by_class_name("_uah")
            uah_selector=random.randint(0,1)
            to_click=uah[uah_selector].find_element_by_tag_name("i")
            driver.execute_script("arguments[0].click();", to_click)
            print(_+1," like done")
            sleep(2)

    except:
        pass




# In[350]:


#-----------------------------------------------------------------------


# In[ ]:





# In[351]:


#-----------------------------Comments----------------------------------


# In[373]:


def do_comment():
    Done=[]
    runns=random.randint(3,4)
    print("No of comments to be done=",runns)
    for _ in range(runns):
        try:
            if _==0:
                driver.get("https://www.facebook.com/")
                sleep(2)
            scrooling_dowon(9,13)
            sleep(2)
            top_feed = driver.find_element_by_id("m_newsfeed_stream")
            newsfeed = top_feed.find_element_by_id("MNewsFeed")
            Sections = newsfeed.find_elements_by_tag_name("section")

            articles=[]
            for section in Sections:
                try:
                    if(section.find_elements_by_tag_name("article")!=[]):
                        articles.extend(section.find_elements_by_tag_name("article"))
                except:
                    pass

            commentable=[]
            for article in articles:
                try:
                    if(int(article.find_element_by_class_name("_1j-c").text.split(" ")[0])>20):
                        commentable.append(article)
                except:
                    pass



            while(1):
                c_index=random.randint(0,len(commentable)-1)
                if c_index not in Done:
                    break
            Done.append(c_index)
            comm=commentable[c_index].find_element_by_class_name("_15kq")
            driver.execute_script("arguments[0].click();", comm)

            sleep(5)

            scrooling_dowon(4,6)
            sleep(1)

            comments=[]
            ff=driver.find_elements_by_class_name("_14v5")
            for div in ff:
                try:
                    comments.append(div.find_element_by_class_name("_2b06").find_elements_by_tag_name("div")[1].text)
                except:
                    pass
            for ___ in range(0,(len(comments)-1)):

                comment=comments[random.randint(0,len(comments)-1)] 
                if comment.isascii():
                    break

            comment+=" :)"

            comment_box=driver.find_element_by_id("composerInput")
            comment_box.send_keys(comment)
            sleep(2)
            submitt=driver.find_element_by_xpath('//button[@type="submit"]')
            submitt.send_keys(Keys.ENTER)
            sleep(3)
            print(_+1,"Comment done")
            driver.get("https://www.facebook.com/")
            sleep(2)
        except:
            pass


# In[353]:


#----------------------------------------------------------------------------------------------


# In[ ]:





# In[374]:


from selenium import webdriver
from selenium.webdriver.firefox import options
import requests
import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

rows=[]
# Scrooling fun
def scrooling_dowon(a,b):
    number = random.randint(a,b)
    body = driver.find_element_by_tag_name("body")
    for j in range(number):
        body.send_keys(Keys.PAGE_DOWN)
        sleep(.5)
    


def wait(c,d):
    timewait = random.randint(c,d)
    sleep(timewait)



#TODO replace with existing profile ID. Define the ID of the browser profile, where the code will be executed.
with open("profiles.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append(row)
    for row in rows:
        print("{}  {}".format(row[1],row[0]))
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

        scrooling_dowon(20,25)

        
        # Comments and likes
        do_like()
        do_comment()

        driver.close()


