from time import sleep
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def get_instagram_data(username, password):
    browser = webdriver.Chrome()

    browser.implicitly_wait(1)

    browser.get('https://www.instagram.com/')

    sleep(1)

    username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']" )
    password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']" )

    username_input.send_keys(username)
    password_input.send_keys(password)


    login_button = browser.find_element(By.XPATH , "//button[@type='submit']")
    login_button.click()

    sleep(10)
    browser.get(f'https://www.instagram.com/{username}')
    sleep(10)

        # browser.find_element(By.XPATH,"//*[@id='mount_0_0_xl']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        # print('not now clikced')
        # browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()


    sleep(10)
    follower_count = int(browser.find_element(By.XPATH,".//*[contains(text(), 'followers')]/span").text)
    following_count = int(browser.find_element(By.XPATH, ".//*[contains(text(), 'following')]/span").text)
        
    print(follower_count, '-----------------------', following_count)



        # print('fiolll;', follower_count)
    sleep(10)

    browser.close()