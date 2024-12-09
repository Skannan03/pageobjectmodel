import pytest
from selenium.webdriver.common.keys import Keys
from POM_Buzz_mrp.Buzz_Mrp import Buzz_mrp
@pytest.mark.usefixtures("setup")
class Test_Buzz_Mrp:
    def test_like_post(self, setup):
        q = Buzz_mrp(self.driver)
        q.mrplike()

    def test_comment_post(self,setup):
        w = Buzz_mrp(self.driver)
        w.mrpcomment("Hello kannan"+ Keys.ENTER)

    def test_share_post(self, setup):
        e = Buzz_mrp(self.driver)
        e.mrpshare("Hello Sanjala")

    def test_delete_post(self, setup):
        r = Buzz_mrp(self.driver)
        r.mrpdelete()


    def test_edit_post(self, setup):
        t = Buzz_mrp(self.driver)
        # pic=r"C:\Users\senthamarai.kannan\PycharmProjects\page object model\testcases\frog.jpg"
        t.mrpeditpost("This post has been edited")

    def test_commentlike(self,setup):
        y = Buzz_mrp(self.driver)
        y.mrpcommentlike("wowwwww naaiceeee"+ Keys.ENTER)


    @pytest.mark.skip
    def test_commentedit(self,setup):
        u = Buzz_mrp(self.driver)
        newcomment="Hows life goin !!!!"+Keys.ENTER
        editedcomment="Chill brother "+ Keys.ENTER
        u.mrpcommentedit(newcomment,editedcomment)