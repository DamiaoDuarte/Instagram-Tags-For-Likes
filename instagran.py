from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\GREEN-PC\Desktop\pythonvscode\assets\chromedriver.exe")

    #//ahref="/accounts/emailsignup/">
    #//input[@name = 'username']
    # //input[@name = 'password']
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]')
        login_button.click()
        time.sleep(3)
        driver.maximize_window()
        button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        button.click()
        self.curtir_fotos('memesBR')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        #button = driver.find_element_by_xpath("/html/body/div[1]/section/main/header/div[2]/div[1]/button").click()
        for i in range(1, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
        hrefs = driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href and href] 
        #.index("https://www.instagram.com/p") != -1]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))

         
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
                button.click()
                time.sleep(3)
            except Exception as e:
                time.sleep(5)

        
        
         

Bot = InstagramBot("your account", "your password")
Bot.login()
#instagramBot = curtir_fotos()
