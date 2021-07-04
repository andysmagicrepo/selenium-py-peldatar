from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
try:
    driver.get("https://www.python.org/")
    if bool(driver.find_element_by_id("nemletezik")):
        pass

#except NoSuchElementException as exc:
#    print("Except branch!")
#    print(exc)

except:
    print("Nem létező id")
finally:
    driver.close()
