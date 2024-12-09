import time

from selenium.webdriver.common.by import By
from utility.Baseclass import Basepage


class Buzz_newsfeed(Basepage):
    post_text = (By.CSS_SELECTOR, 'textarea[placeholder="What\'s on your mind?"]')
    submit = (By.CSS_SELECTOR, "button[type='submit']")

    share_photos = (By.XPATH, "//*[contains(text(),' Share Photos')]")
    post_text_share = (By.XPATH, "(//textarea[@class='oxd-buzz-post-input'])[2]")
    post_pic = (By.XPATH, "//input[@class='oxd-file-input']")
    share = (By.XPATH, "(//button[@type='submit'])[2]")

    share_video = (By.XPATH, "(//button[@class='oxd-glass-button'])[2]")
    post_text_share = (By.XPATH, "(//textarea[@class='oxd-buzz-post-input'])[2]")
    upload_link = (By.XPATH, "//textarea[@placeholder='Paste Video URL']")
    share = (By.XPATH, "(//button[@type='submit'])[2]")

    def buzz_post_text(self, text):
        self.hrm_send_keys(self.post_text, text)
        self.hrm_btn_click(self.submit)
        time.sleep(3)

    def buzz_share_post(self,text, pic: str):
        self.hrm_btn_click(self.share_photos)
        time.sleep(3)
        self.hrm_send_keys(self.post_text_share, text)
        time.sleep(3)
        self.hrm_send_keys(self.post_pic, pic)
        time.sleep(3)
        self.hrm_btn_click(self.share)

    def buzz_share_video(self, text,video):
        self.hrm_btn_click(self.share_video)
        time.sleep(3)
        self.hrm_send_keys(self.post_text_share, text)
        time.sleep(3)
        self.hrm_send_keys(self.upload_link, video)
        time.sleep(3)
        self.hrm_btn_click(self.share)
