syomei ="""
〇〇〇
""" 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

def send_by_outlook(mail_data):
  driver = webdriver.Chrome("./chromedriver", options=options)
  driver.implicitly_wait(3)
  wait = WebDriverWait(driver, 5)
  try:
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='新規メール']").click()
  except:
    pass

  driver.find_element(By.CSS_SELECTOR, "div[class='VbY1P T6Va1 Z4n09 EditorClass']").send_keys(mail_data["atesaki"])
  # driver.find_element(By.CSS_SELECTOR, "div[aria-label='CC']").send_keys(mail_data["cc_atesaki"])
  driver.find_element(By.XPATH, "//*[@class='P6mmz']/div/div/div/input").send_keys(mail_data["mail_title"])
  driver.find_element(By.CSS_SELECTOR, "div[class='dFCbN k1Ttj dPKNh DziEn']").clear()
  driver.find_element(By.CSS_SELECTOR, "div[aria-label='メッセージ本文、Alt+F10を押して終了します']").send_keys(mail_data["mail_main"]+syomei)

  #ウェイト用パーツ
  # wait.until(expected_conditions.visibility_of_element_located((By.ID, "idSIButton9")))
  # # wait.until(expected_conditions.element_to_be_clickable((By.ID, "idSIButton9")))
  # sleep(3)