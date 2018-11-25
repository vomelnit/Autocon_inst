# -*- coding: utf-8 -*-
from selenium import webdriver
# import selenium.webdriver.common.action_chains
# from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import urllib.request
import Image_formalization
import Conf_features
import hashtag_creator



mobile_emulation = { "deviceName": "iPhone 6" }
#img_link=''
name_of_article=''
text_of_article=''
hashtag_category=''
article_number=0
article_link=''
successful_post=False
attempt=0
username=Conf_features.username
psw=Conf_features.password
#probably_posted=False
#counter_of_posts=0



def define_variables(name,text,hashtag,number,link):
            global name_of_article
            global text_of_article
            global hashtag_category
            global article_number
            global article_link
            name_of_article = name
            text_of_article = text
            hashtag_category = hashtag
            article_number = number
            article_link = link


def put_img_to_folder(image_link,number,name,high_text):
        print(image_link)
        urllib.request.urlretrieve(image_link,'autocon_images/'+'img_of_article'+str(number)+'.jpg')
        Image_formalization.Image_change('autocon_images/'+'img_of_article'+str(number)+'.jpg',name,high_text)



def enter_to_instagram(driver):
        global probably_posted
        #global counter_of_posts
        global successful_post
        #d=[]
        try:
                print("parse"+article_link)
                driver.get('http://'+article_link)
                time.sleep(4)
                WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located)
                description = driver.find_element_by_xpath("//body / div / div[6] / div / div[1] / div[3] / div / p[1]").text
                print(description)
                d=driver.find_element_by_xpath("//body / div / div[6] / div / div[1] / div[3] / div / p[2]").text

                print("getted")
                #print(str(d))
                print(len(d))
                time_of_reading=len(d)//700+1
                # for m in re.finditer("\n",d):
                #         if m.start()>=1000:
                #                 d=d[:m.start()]
                #                 print(len(d))
                #                 break
                #         print(len(d))



        except:
                pass
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        # driver.implicitly_wait(10)
        #time.sleep(1)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Log in']")))
        #try:
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/article/div/div/div/button")))
        # button_login = driver.find_element_by_xpath("//*[text()='Log in']")
        # button_login.click()
            #WebDriverWait(driver, 10).until(EC.)

            #user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
            #assert user_mail.text == "au"
        # except selenium.common.exceptions.NoSuchElementException:
        #     link_entry = driver.find_element_by_link_text("/accounts/login/?source=auth_switcher")
        #     link_entry.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Phone number, username, or email']")))
        login_field = driver.find_element_by_name("username")
        login_field.send_keys(username)
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Password']")))
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(psw)
        # button_entry = driver.find_element_by_xpath("//*[text()='Войти']")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Log in']")))
        time.sleep(1)
        entry_form = driver.find_element_by_xpath("//form[@method='post']")
        entry_form.submit()
        #button_entry = driver.find_element_by_xpath("//*[text()='Log in']")
        #button_entry.click()
        print("Log in")
        #time.sleep(5)
        #driver.implicitly_wait(10)
        #WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located)
        try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']")))
                #driver.implicitly_wait(10)
                button_not_now = driver.find_element_by_xpath("//*[text()='Not Now']")
                button_not_now.click()
                print("Not now")
        except:
                pass
        # driver.get("https://www.instagram.com/" + username)
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Profile']")))
        driver.get("https://www.instagram.com/"+username)
        #time.sleep(1)
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
        # amount_of_posts = int(driver.find_element_by_xpath("//ul/li/span/span").text)
        # print(amount_of_posts)
        post=[]
        for j in range(9):
                xpath_str="// section / main / div / div[3] / article / div[1] / div / div[{0}] / div[{1}] / a / div / div[1] / img".format(str((j)//3+1),str((j)%3+1))
                post.append(driver.find_element_by_xpath(xpath_str).get_attribute("alt"))#[:driver.find_element_by_xpath(xpath_str).get_attribute("alt").find("\n")])
                print(post[j])
                if post[j].find(description)!=-1: successful_post=True
        print(len(post))
        # post1=driver.find_element_by_xpath("// section / main / div / div[3] / article / div[1] / div / div[1] / div[1] / a / div / div[1] / img")
        # post2=driver.find_element_by_xpath("//section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div/div[1]/img")
        # post3 = driver.find_element_by_xpath("//section/main/div/div[3]/article/div[1]/div/div[1]/div[3]/a/div/div[1]/img")
        # print(post1.get_attribute("alt"))
        # print(post2.get_attribute("alt"))
        # print(post3.get_attribute("alt"))
        # print(name_of_article)
        # if (post1.get_attribute("alt").find(name_of_article)!=-1)|(post2.get_attribute("alt").find(name_of_article)!=-1)|(post3.get_attribute("alt").find(name_of_article)!=-1):
        #         successful_post=True

        # if (probably_posted==True)&(counter_of_posts<amount_of_posts):
        #         successful_post=True
        #         counter_of_posts = amount_of_posts

        if successful_post==False:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem']")))
                button_new_post = driver.find_element_by_xpath("//div[@role='menuitem']")
                button_new_post.click()
                print("Menuitem_add_post")
                #driver.refresh()
                send_img=driver.find_element_by_xpath("//input[@accept='image/jpeg']")
                #send_form=driver.find_elements_by_xpath("//form[@enctype='multipart/form-data']")
                #print(send_img)
                #time.sleep(2)
                #print(send_form)
                #send_img.click()
                Imagepath = os.path.abspath('autocon_images/'+'img_of_article'+str(article_number)+'.jpg')
                #
                send_img.send_keys(Imagepath)
                print("Sent keys of img")
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Expand']")))
                # spire_button = driver.find_element_by_xpath("//*[text()='Expand']")
                # spire_button.click()
                # print("Expand")
                #
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Rotate']")))
                # rotate_button=driver.find_element_by_xpath("//*[text()='Rotate']")
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # time.sleep(0.5)
                # rotate_button.click()
                # print("Rotated")

                #time.sleep(2)
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Filter']")))
                #print("wait")
                #spire_button = driver.find_element_by_xpath("//*[text()='Filter']")
                # spire_button =driver.find_element_by_xpath("//button[@tabindex='0']")
                # print("find button")
                # spire_button.click()
                # print("Click")
                # print("Filter button")
                # #time.sleep()
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Lark']")))
                # spire_button = driver.find_element_by_xpath("//*[text()='Lark']")
                # # action = selenium.webdriver.common.action_chains.ActionChains(driver)
                # # action.drag_and_drop_by_offset(spire_button, -25, 0).perform()
                # #
                # # time.sleep(1)
                # # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Ludwig']")))
                # # spire_button = driver.find_element_by_xpath("//*[text()='Ludwig']")
                # spire_button.click()
                # print("Pressed on (Lark)")
                # time.sleep(3)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']")))
                button_next = driver.find_element_by_xpath("//*[text()='Next']")
                button_next.click()
                print("Next")

                time.sleep(2)
                #driver.implicitly_wait(10)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
                #time.sleep(5)
                text_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
                #text_field = driver.find_element_by_name("Введите подпись...")
                text_field.clear()
                text_field.send_keys(description+' . .\n_________________________________\n\nПодробнее по ссылке в профиле\nВремя прочтения: ~'+str(time_of_reading)+' мин'+'\n'+hashtag_category+' '+hashtag_creator.Create_hashtags(name_of_article)+' #автоконсалтинг #autoconsulting')
                print("Added text")
                # send_img[1].send_keys(Imagepath)
                time.sleep(1)
                button_share = driver.find_element_by_xpath("//*[text()='Share']")
                button_share.click()
                print("Share")
                # probably_posted=True

                time.sleep(2)
                try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Retry']")))
                        button_retry=driver.find_element_by_xpath("//*[text()='Retry']")
                        button_retry.click()
                        print("Retry")
                except:
                        pass
                time.sleep(4)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Profile']")))
                driver.get("https://www.instagram.com/"+username)
                time.sleep(2)
                # print("on profile")
                # new_amount_of_posts=int(driver.find_element_by_xpath("//ul/li/span/span").text)
                # print("get new amount of posts")
                # print(str(amount_of_posts)+'->'+str(new_amount_of_posts))

                for j in range(9):
                        xpath_str = "// section / main / div / div[3] / article / div[1] / div / div[{0}] / div[{1}] / a / div / div[1] / img".format(
                                str((j) // 3 + 1), str((j) % 3 + 1))
                        post.append(driver.find_element_by_xpath(xpath_str).get_attribute("alt")) #[
                                   # :driver.find_element_by_xpath(xpath_str).get_attribute("alt").find("\n")])
                        print(post[j+9])
                        if post[j+9].find(description) != -1: successful_post = True

                if (post[9].find(description)==-1)|(len(post[9])==0):
                        for l in range(8):
                                if post[l+10]==post[l]: successful_post=True
                                else:
                                        successful_post=False
                                        break



# class LoginMailBox(unittest.TestCase):


def setUp():


        chrome_options = webdriver.ChromeOptions()
        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("prefs", {"intl.accept_languages": "en-US"})
        #chrome_options.add_argument('headless')
        #self.driver\

        driv = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
        return driv




def test_user_login_in_mail_box(dr):
        driver = dr
        global successful_post
        global attempt
        #WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
        print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
        try:
                enter_to_instagram(driver)
        except:
            print("Error_of instagram")
            attempt+=1
        print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
        #driver.close()
        driver.quit()

def tear_down(self):
        self.driver.quit()

def begin_of_driver(image_link, name, text, hashtag, number,high_text,link):
        print("begin of driver")
        global successful_post
        global attempt
        #global probably_posted
        put_img_to_folder(image_link, number,name,high_text)
        define_variables(name, text, hashtag, number,link)
        attempt=1
        while(successful_post!=True):
            test_user_login_in_mail_box(setUp())
            print("Attempt #"+str(attempt))
            print(str(successful_post))
            #attempt+=1
            if (attempt>=8): break
        if_post=successful_post
        successful_post=False
        return if_post

#if __name__ == "__main__":



# print("1")
# begin_of_driver('http://www.autoconsulting.com.ua/pictures/Nissan/2017/Nissan_Qashqai_28.jpg',"Blablabla","Some text","#hash",0)
# print("2")




# class LoginMailBox(unittest.TestCase):
#     def setUp(self):
#
#
#         chrome_options = webdriver.ChromeOptions()
#         # Add the mobile emulation to the chrome options variable
#         chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#         chrome_options.add_experimental_option("prefs", {"intl.accept_languages": "en-US"})
#         #chrome_options.add_argument('headless')
#         self.driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
#         self.driver.implicitly_wait(10)
#
#
#
#     def test_user_login_in_mail_box(self):
#         driver = self.driver
#         #WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
#         print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
#         enter_to_instagram(driver)
#         print(time.strftime("%H:%M:%S", time.gmtime(time.time())))
#
#
#     def tear_down(self):
#         self.driver.quit()
#
#
#     def begin_of_driver(image_link, name, text, hashtag, number):
#         put_img_to_folder(image_link, number)
#         define_variables(name, text, hashtag, number)
#         unittest.main()
#         global successful_post
#         if_post=successful_post
#         successful_post=False
#         return if_post
#
# #if __name__ == "__main__":
#
#
#
#
#     begin_of_driver('http://www.autoconsulting.com.ua/pictures/Nissan/2017/Nissan_Qashqai_28.jpg',"Blablabla","Some text","#hash",0)
