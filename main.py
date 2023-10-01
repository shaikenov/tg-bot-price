from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.amazon.it/dp/B01J24H2K0?ref_=cm_sw_r_apan_dp_7S991H09GEQMNRBD20V1"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

print(driver.find_element(By.CLASS_NAME, "a-price").text)

# gotovo
