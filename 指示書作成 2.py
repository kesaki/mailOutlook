
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.amazon.co.jp/s?i=instant-video&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss")

select = driver.find_element(By.ID,"searchDropdownBox")
select = Select(select)
selected_option = select.first_selected_option.text
print(selected_option)