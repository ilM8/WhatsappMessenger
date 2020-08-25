from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("config.cfg", "r") as config:
    config = config.read()
    config = config.rstrip()
    config = config.split("*")
    print(config)

PATH = config[0]

print("[",PATH,"]")

if config[1] == "firefox":
    driver = webdriver.Firefox(PATH)

elif config[1] == "chrome":
    driver = webdriver.Chrome(PATH)

elif config[1] == "safari":
    driver = webdriver.Safari(PATH)




# Here we are opening the website and then waiting till the user scanned in the QR-Code and the Whatsapp Web has loaded. The user has 60 seconds to do this.
driver.get("https://web.whatsapp.com/")
_ = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div[2]/div"))
)

def send_message(chat, message):

    searchbar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")

    searchbar.send_keys(chat)
    searchbar.send_keys(Keys.RETURN)

    message_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"))
    )

    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)

# Always call this at the end of your program because this will close the driver
def close_driver():
    driver.close()

# /html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3] xpath of the div in wich all loaded messages are loaded
