from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import glob
from datetime import datetime
import time
from os import path
import os


login_auth=' login '
password_auth=' password '
#chromedriver_path=r'/Users/miroslavbabkov/Documents/selenium/chromedriver'


def main():
    
    url = 'https://pinterest.com/login/'

    lenght_directory = len(glob.glob(url_img + '/*'))

    print(f"In the directory {lenght_directory} files")

    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='  CHROMEDRIVER  ', options=option)
    try:
        driver.get(url=url)

        sleep(1)

        email_input = driver.find_element('id','email')
        email_input.clear()
        email_input.send_keys(login_auth)

        password_input = driver.find_element('id', 'password')
        password_input.clear()
        password_input.send_keys(password_auth)

        password_input.send_keys(Keys.ENTER)
        sleep(5)

        for i in glob.glob(url_img + '/*'):
            print(i)

            driver.get(url='https://pinterest.com/pin-builder/')

            full_name = os.path.basename(i)
            name = path.splitext(full_name)[0]

            sleep(5)

            name_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/textarea')
            name_input.clear()
            name_input.send_keys(name)

            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/input').send_keys(i)
            sleep(5)
            while True:
                try:
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div')
                    sleep(10)
                    
                except:
                    sleep(5)
                    break
            driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]').click()
            sleep(2)
            while True:
                try:
                    driver.find_element(By.CSS_SELECTOR, '.jzS.mQ8.un8.C9i.TB_')
                    sleep(2)
                except:
                    sleep(5)
                    break

    except Exception as ex:
        print(" Error ")

    finally:
        time.sleep(15)
        driver.close()

url_img = str(input('Insert the path to the folder -> '))

wasd = str(input("When do you want to run the code? Now or later -> "))

if 'now' in wasd.lower():
    main()
else:
    while True:
        try:
            date = input("Input time in this format: mon/day/hour/min -> ")
            timer = datetime.strptime(date, "%m/%d/%H/%M").strftime('%m/%d/%H/%M')
            break
        except:
            print('Incorrect type of input!')
            continue

    while True:
        sleep(30)
        t = time.localtime()
        now_time = time.strftime("%m/%d/%H/%M", t)
        if now_time == timer:
            break
    main()
    print('Data was successfully posted!')
