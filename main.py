from config import credential_dict
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    tinder_login = driver.find_element(By.XPATH, '//a(contains[@href, '"https://tinder.onelink.me/9K8a/3d4abb81"']')
    tinder_login.click()
    driver.implicitly_wait(2)
    
    fb_button = driver.find_element(By.XPATH, '//button(contains[@aria-label, "Log in with Facebook"]')
    fb_button.click()
    
    email = driver.find_element(By.NAME, value='email').send_keys(credential_dict.get('username'))
    password = driver.find_element(By.NAME, value='password').send_keys(credential_dict.get('password'))
    login = driver.find_element(By.NAME, value='login').click()
    
    driver.implicitly_wait(2)
    
    
    btn2 = driver.find_element(By.XPATH, value='//button(contains[@draggable, false])[1]').click()
    btn1 = driver.find_element(By.XPATH, "//button(contains[@data-testid, onboarding_dismiss])").click()
    
    
    tinder_buttons = driver.find_elements(By.CLASS_NAME, value='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s')
    skip = tinder_buttons[0]
    skip_button = skip.find_element(By.TAG_NAME, value='button')
    like = tinder_buttons[1]
    like_button = like.find_element(By.TAG_NAME, value='button')
    
    try:
        like_button.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        #click back to tinder button
        #driver.find_elements()
        pass

if __name__ == '__main__':
    main()