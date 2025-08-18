from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_google_maps(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)

    data = {
        "name": None,
        "address": None,
        "contact": None,
        "website": None,
        "email": None
    }

    try:
        data["name"] = driver.find_element(By.CLASS_NAME, "DUwDvf").text
    except:
        pass

    try:
        data["address"] = driver.find_element(By.CLASS_NAME, "Io6YTe").text
    except:
        pass

    try:
        data["contact"] = driver.find_element(By.CSS_SELECTOR, "button[data-tooltip='Copy phone number']").text
    except:
        pass

    try:
        data["website"] = driver.find_element(By.CSS_SELECTOR, "a[data-tooltip='Open website']").get_attribute("href")
    except:
        pass

    driver.quit()
    return data
