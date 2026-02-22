import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import config

WHATSAPP_URL = "https://web.whatsapp.com/"

class WhatsAppBot:

    def __init__(self):
        options = Options()
        options.add_argument("--user-data-dir=chrome_profile")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(WHATSAPP_URL)

        print("Scan QR if required...")
        time.sleep(15)

    def get_active_chat_name(self):
        try:
            header = self.driver.find_element(
                By.XPATH,
                '//header//span[@dir="auto"]'
            )
            curr_profile = header.text
            if curr_profile in config.ALLOWED_CONTACTS:
                return header.text
            else:
                print("Unknow encounter!")
                return "UNKNOWN"

        except:
            return None

    def get_last_incoming_message(self):
        messages = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class,"message-in")]//span[@dir="ltr"]'
        )

        if messages:
            return messages[-1].text

        return None

    def send_message(self, text):
        print("sending reply.....")
        box = self.driver.find_element(
            By.XPATH,
            '//div[@contenteditable="true"][@data-tab="10"]'
        )
        box.send_keys(text + Keys.ENTER)
