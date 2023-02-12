number = input("番号")
from os import environ
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


import mail as module
mail_data = module.get_mail(number)
if type(mail_data) != dict:
  print(mail_data)
  sleep(2)
  exit ()
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1675938175&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d686921c1-d52b-5d19-d63b-f5d4dfa2bb57&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys(environ["g-add"])
driver.find_element(By.ID, "idSIButton9").click()
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(environ["g-pass"])
wait.until(expected_conditions.visibility_of_element_located((By.ID, "idSIButton9")))
# wait.until(expected_conditions.element_to_be_clickable((By.ID, "idSIButton9")))
driver.find_element(By.ID, "idSIButton9").click()
driver.find_element(By.ID, "idSIButton9").click()

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='新規メール']")))
# wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='新規メール']")))
# sleep(3)
driver.find_element(By.CSS_SELECTOR, "div[aria-label='新規メール']").click()
driver.find_element(By.XPATH, "//*[@class='QHw8J PCB1B bzocG Viglg']/button[1]").click()

driver.find_element(By.CSS_SELECTOR, "div[class='VbY1P T6Va1 Z4n09 EditorClass']").send_keys(mail_data["atesaki"])
driver.find_element(By.CSS_SELECTOR, "div[aria-label='CC']").send_keys(mail_data["cc_atesaki"])
driver.find_element(By.XPATH, "//*[@class='P6mmz']/div/div/div/input").send_keys(mail_data["title"])
driver.find_element(By.CSS_SELECTOR, "div[class='dFCbN k1Ttj dPKNh DziEn']").send_keys(mail_data["mail"])


