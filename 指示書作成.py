from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.library.chiyoda.tokyo.jp/")
# hardware_el = driver.find_elements(By.CLASS_NAME,"schedule-list01__text")
service_el = driver.find_elements(By.CSS_SELECTOR,"span[class^='schedule-list01__']")

service = []
[service.append(s.text) for s in service_el]
service = "\n".join(service)

hardware_el = driver.find_elements(By.CSS_SELECTOR,"span[class^='schedule-list01__']")

hardware = []
[hardware.append(s.text) for s in hardware_el]
hardware = "\n".join(hardware)

with open("memo.txt", "w") as f:
  f.write(service + "\n\n")
  f.write(hardware)    
    
subprocess.Popen(["notepad","memo.txt"])
subprocess.Popen(["start","memo.txt"], shell=True)
subprocess.Popen(["start","メモ.xls"], shell = True)


