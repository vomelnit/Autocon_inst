from selenium import webdriver
import pickle
import time



def Get_cookies(driver,filename):

    cookies = pickle.load(open(filename, "rb"))
    print(len(cookies))
    print(cookies)


    for cookie in cookies:  # session cookies
        # Setting domain to None automatically instructs most webdrivers to use the domain of the current window
        # handle
        cookie_dict = {'domain': cookie.get('domain'), 'name': cookie.get('name'), 'value': cookie.get('value'), 'secure': cookie.get('secure')}
        if cookie.get('expires')!=None:
            cookie_dict['expiry'] = cookie.get('expires')
        if cookie.get('path')!=None:
            cookie_dict['path'] = cookie.get('path')
        if cookie.get('httpOnly')!=None:
            cookie_dict['httpOnly'] = cookie.get('httpOnly')
        print(cookie_dict)

        driver.add_cookie(cookie_dict)



    # cook1={'domain': '.instagram.com', 'name':'csrftoken' , 'value':'4fdmEXYBxeZgcI6vNgmRzjgFhzY2R9zC' , 'secure': True,'expires':'2019-11-26T12:56:39.287Z' ,'path': "/",'httpOnly':False }
    # cook2 = {'domain':'.instagram.com', 'name':'datr', 'value':'7Bz7W48RVtow_XkBsTfVa3v3', 'secure':True, 'expires':'2020-11-24T22:19:18.263Z', 'path':"/", 'httpOnly':True}
    # cook3 = {'domain':'.instagram.com', 'name':'ds_user_id', 'value':'8720080482', 'secure':True, 'expires':'2019-02-25T12:56:39.287Z', 'path':"/", 'httpOnly':False}
    # cook4 = {'domain':'.instagram.com', 'name':'mcd', 'value':'3', 'secure':True, 'expires':'2028-11-19T16:57:13.135Z', 'path':"/", 'httpOnly':False}
    # cook5 = {'domain':'.instagram.com', 'name':'mid', 'value':'W_bf6AAEAAGUfmKskkgWhtW6x6kq', 'secure':True, 'expires':'2028-11-19T16:57:13.135Z', 'path':"/", 'httpOnly':False}
    # cook6 = {'domain':'.instagram.com', 'name':'rur', 'value':'FTW', 'secure':True, 'expires':'1969-12-31T23:59:59.000Z', 'path':"/", 'httpOnly':True}
    # cook7 = {'domain':'.instagram.com', 'name':'sessionid', 'value':'8720080482%3AV0LFRCSu2Sz9pC%3A3', 'secure':True, 'expires':'2019-11-27T12:51:07.996Z', 'path':"/", 'httpOnly':True}
    # cook8 = {'domain':'.instagram.com', 'name':'shbid', 'value':'15251', 'secure':True, 'expires':'2018-12-02T22:41:40.138Z', 'path':"/", 'httpOnly':True}
    # cook9 = {'domain':'.instagram.com', 'name':'shbts', 'value':'1543185699.9681044', 'secure':True, 'expires':'2018-12-02T22:41:40.138Z', 'path':"/", 'httpOnly':True}
    # cook10 = {'domain':'.instagram.com', 'name':'urlgen', 'value':'"{}:1gRcut:d_E8Qhd-2itBRbY6d14miKIed48"', 'secure':True, 'expires':'1969-12-31T23:59:59.000Z', 'path':"/", 'httpOnly':True}
    #
    # driver.add_cookie(cook1)
    # driver.add_cookie(cook2)
    # driver.add_cookie(cook3)
    # driver.add_cookie(cook4)
    # driver.add_cookie(cook5)
    # driver.add_cookie(cook6)
    # driver.add_cookie(cook7)
    # driver.add_cookie(cook8)
    # driver.add_cookie(cook9)
    # driver.add_cookie(cook10)
    # print('get cookies')
    # pickle.dump(driver.get_cookies(), open(filename, "wb"))

    return driver