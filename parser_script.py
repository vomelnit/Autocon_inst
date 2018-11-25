# -*- coding: utf-8 -*-
import feedparser
import time
import main_instagram
from w3lib.html import replace_entities
import facebook_post

counter_of_articles=0
list_of_articles = []
list_of_links= []
if_need_to_post = False
if_list_refreshed = False
image_error = False
rss_link = 'http://autoconsulting.com.ua/rss.html'
img_counter = 0
amount_of_img = 0
i=1




def parse_autocon(list_arti,list_link,rss_link):
    try:
        feed = feedparser.parse(rss_link)
        for entry in feed.entries:
            time.sleep(5)
            article_title = search_for_quots(entry.title)
            article_link=entry.link
            article_link = article_link[7:]
            list_arti.append(article_title)
            list_link.append(article_link)

    except Exception as msg:
        print(msg)
        print(time.strftime("%H:%M", time.localtime()) + "  Error parse")

def search_for_quots(title_text):
    while (title_text.find('&quot;')!=-1):
        title_text_copy=title_text
        title_text=title_text_copy[:title_text.find('&quot;')]+'"'+title_text[title_text.find('&quot;')+6:]
    return title_text


if __name__ == '__main__':
    print("Begin")
    #parse_autocon(list_of_articles,list_of_links,rss_link)
    print("Parsed")
    while True:

            try:
                feed = feedparser.parse(rss_link)
                print("feed")
                for entry in feed.entries:
                    img_counter = 0
                    i=1
                    time.sleep(10)
                    article_title = search_for_quots(entry.title)
                    article_title=replace_entities(article_title)

                    article_link = entry.link
                    article_link = article_link[7:]
                    if (list_of_articles.count(article_title) == 0)&(list_of_links.count(article_link) == 0):
                        amount_of_img = len(entry.enclosures)
                        print(time.strftime("%H:%M", time.localtime()) + "  New article:"+article_title+'\n'+article_link)
                        if_need_to_post = True
                        if if_need_to_post == True:

                            #article_link = article_link[7:]
                            article_category = entry.category
                            if_need_to_post = False
                            category = article_category.split('/')
                            high_text=category[0]
                            print(high_text)
                            print(high_text)
                            hashtag1 = '#' + category[0].lower()
                            h1 = hashtag1
                            if (hashtag1.find(' ') != -1):
                                hashtag_symbol_num = hashtag1.find(' ')
                                hashtag2 = hashtag1
                                h1 = hashtag1[:hashtag_symbol_num] + hashtag2[hashtag_symbol_num + 1:]
                                hashtag1 = h1
                                hashtag2 = h1
                            if (hashtag1.find(' ') != -1):
                                hashtag_symbol_num = hashtag1.find(' ')
                                hashtag2 = hashtag1
                                h1 = hashtag1[:hashtag_symbol_num] + hashtag2[hashtag_symbol_num + 1:]
                                hashtag1 = h1
                                hashtag2 = h1
                            if (hashtag1.find(',') != -1):
                                hashtag_symbol_num = hashtag1.find(',')
                                hashtag2 = hashtag1
                                h1 = hashtag1[:hashtag_symbol_num] + hashtag2[hashtag_symbol_num + 1:]
                                hashtag1 = h1
                                hashtag2 = h1
                            if (hashtag1.find(',') != -1):
                                hashtag_symbol_num = hashtag1.find(',')
                                hashtag2 = hashtag1
                                h1 = hashtag1[:hashtag_symbol_num] + hashtag2[hashtag_symbol_num + 1:]
                                hashtag1 = h1
                                hashtag2 = h1
                            if (hashtag1.find('-') != -1):
                                hashtag_symbol_num = hashtag1.find('-')
                                hashtag2 = hashtag1
                                h1 = hashtag1[:hashtag_symbol_num] + hashtag2[hashtag_symbol_num + 1:]

                            if_made_post_ins=False
                            #if_made_post_fb = False
                            if_made_post=False
                            while (if_made_post!=True):
                                    #try:
                                        article_img_link = entry.enclosures[img_counter]

                                        sentences =entry.description.split('. ')
                                        text=sentences[0]+'. '+sentences[1]+'.'
                                        print(text)
                                        print("enter to file.py")
                                        # if if_made_post_ins!=True:
                                        #     if_made_post_ins=main_instagram.begin_of_driver(article_img_link.url,article_title.upper(),text,h1,counter_of_articles,high_text,article_link)
                                        
                                        if_made_post=main_instagram.begin_of_driver(article_img_link.url,article_title.upper(),text,h1,counter_of_articles,high_text,article_link)
                                        print("end")

                                        #if (if_made_post_fb==True)&(if_made_post_ins==True): if_made_post=True
                                        if (if_made_post==True):
                                            list_of_articles.append(article_title)
                                            list_of_links.append(article_link)

                                            counter_of_articles+=1
                                            if (counter_of_articles==25): counter_of_articles=0

                                        else:
                                            #if (i == 0): img_counter += 1
                                            i += 1
                                            if (i >= 4):
                                                i = 0
                                                time.sleep(60)

                                            time.sleep(10)

                                    # except Exception:
                                    #     if (i==0): img_counter+=1
                                    #     if (img_counter >= amount_of_img): break
                                    #     i+=1
                                    #     if(i>=4):
                                    #         i=0
                                    #         break
                                    #         time.sleep(60)
                                    #
                                    #     time.sleep(30)





                            img_counter = 0
                            i=1

                time.sleep(600)

            except Exception as msg:
                 print(msg)
                 print(time.strftime("%H:%M", time.localtime()) + "  Error loop")
                 time.sleep(600)
