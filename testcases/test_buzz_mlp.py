import pytest
from selenium.webdriver.common.keys import Keys

from POM_Buzz_Mlp.Buzz_Mlp import Buzz_mlp


@pytest.mark.usefixtures("setup")
class Test_Buzz_Mlp:

    @pytest.mark.dependency()
    def test_mlp(self, setup):
        mlp = Buzz_mlp(self.driver)
        mlp.mostlikedpost()
        assert True

    @pytest.mark.dependency(depends=['Test_Buzz_Mlp::test_mlp'])
    def test_like_post(self, setup):
        q = Buzz_mlp(self.driver)
        q.mlplike()
        assert True

    @pytest.mark.dependency(depends=['Test_Buzz_Mlp::test_like_post'])
    def test_comment_post(self, setup):
        w = Buzz_mlp(self.driver)
        w.mlpcomment("hello kannan" + Keys.ENTER)
        assert True

    def test_share_post(self, setup):
        e = Buzz_mlp(self.driver)
        e.mlpshare("Hello sanjala")

    def test_delete_post(self, setup):
        r = Buzz_mlp(self.driver)
        r.mlpdelete()

    def test_edit_post(self, setup):
        t = Buzz_mlp(self.driver)
        # pic=r"C:\Users\senthamarai.kannan\PycharmProjects\page object model\testcases\frog.jpg"
        t.mlpeditpost("Vanakam da mapla")

    @pytest.mark.dependency(depends=['Test_Buzz_Mlp::test_comment_post'])
    def test_commentlike(self, setup):
        y = Buzz_mlp(self.driver)
        y.mlpcommentlike("new comment" + Keys.ENTER)
        assert True
