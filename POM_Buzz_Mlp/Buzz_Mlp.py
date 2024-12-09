import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utility.Baseclass import Basepage


class Buzz_mlp(Basepage):
    mlp = (By.XPATH, "//button[normalize-space()='Most Liked Posts']")
    like1 = (By.XPATH, "(//*[name()='svg'][@id='heart-svg'])[1]")
    comment_click =(By.XPATH,"(//i[@class='oxd-icon bi-chat-text-fill'])[1]")
    comment =(By.CSS_SELECTOR,"input[placeholder='Write your comment...']")

    share_click = (By.XPATH, "(//i[@class='oxd-icon bi-share-fill'])[1]")
    text_enter = (By.XPATH, "(//textarea[@class='oxd-buzz-post-input'])[2]")
    share_text = (By.XPATH, "(//button[@type='submit'])[2]")

    click_option = (By.XPATH, "//i[@class='oxd-icon bi-three-dots']")
    delete = (By.XPATH, "(//li[@class='orangehrm-buzz-post-header-config-item'])[1]")
    click_yes = (
    By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")

    edit_post = (By.XPATH, "(//li[@class='orangehrm-buzz-post-header-config-item'])[2]")
    edit_text = (By.XPATH, "(//textarea[@class='oxd-buzz-post-input'])[2]")
    # upload_pic=(By.CSS_SELECTOR,".oxd-file-div.oxd-file-div--active")
    click_post = (By.CSS_SELECTOR, "div[class='oxd-form-actions orangehrm-buzz-post-modal-actions'] button[type='submit']")


    comment_like = (By.XPATH, "(//p[@class='oxd-text oxd-text--p orangehrm-post-comment-action'])[1]")
    comment_edit = (By.XPATH, "(//p[@class='oxd-text oxd-text--p orangehrm-post-comment-action'])[2]")
    comment_del = (By.XPATH, "(//p[@class='oxd-text oxd-text--p orangehrm-post-comment-action'])[3]")

    def __init__(self, driver):
        super().__init__(driver)

#clicking on the most liked post
    def mostlikedpost(self):
        self.hrm_btn_click(self.mlp)

# liking the post
    def mlplike(self):
        self.hrm_btn_click(self.like1)
        self.driver.execute_script("window.scrollTo(0,300);")
        time.sleep(3)

# commenting on the post
    def mlpcomment(self,text):
        self.hrm_btn_click(self.comment_click)
        self.hrm_send_keys(self.comment,text)
        self.driver.execute_script("window.scrollTo(0,300);")
        time.sleep(3)

# sharing the post
    def mlpshare(self, text):
        self.hrm_btn_click(self.share_click)
        self.hrm_send_keys(self.text_enter, text)
        self.hrm_btn_click(self.share_text)
        time.sleep(3)

# deleting the post
    def mlpdelete(self):
        self.hrm_btn_click(self.click_option)
        self.hrm_btn_click(self.delete)
        self.hrm_btn_click(self.click_yes)

# editing the post
    def mlpeditpost(self, text):
        self.driver.refresh()
        self.hrm_btn_click(self.click_option)
        self.hrm_btn_click(self.edit_post)
        time.sleep(3)

        a = self.driver.find_element(*self.edit_text)
        a.click()
        # a.send_keys(Keys.BACKSPACE * 50)
        a.send_keys(Keys.CONTROL, 'a')  # Select all text
        a.send_keys(Keys.BACKSPACE)
        time.sleep(3)
        self.hrm_send_keys(self.edit_text, text)
        time.sleep(3)

        # self.hrm_send_keys(self.upload_pic,pic)
        self.hrm_btn_click(self.click_post)

# liking the comment
    def mlpcommentlike(self,text):
        self.driver.refresh()
        self.hrm_btn_click(self.comment_click)
        self.hrm_send_keys(self.comment,text)
        self.driver.execute_script("window.scrollTo(0,300);")
        self.hrm_btn_click(self.comment_like)
        time.sleep(3)