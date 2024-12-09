import pytest
from selenium.webdriver.common.keys import Keys
from POM_Buzz_Mcp.Buzz_Mcp import Buzz_mcp

@pytest.mark.usefixtures("setup")
class Test_Buzz_Mcp:

    @pytest.mark.run(order=1)
    # @pytest.mark.first
    def test_mcp(self, setup):
        mlp = Buzz_mcp(self.driver)
        mlp.mostcommentedpost()

    def test_like_post(self, setup):
        q = Buzz_mcp(self.driver)
        q.mcplike()

    @pytest.mark.run(order=2)
    # @pytest.mark.second
    def test_comment_post(self, setup):
        w = Buzz_mcp(self.driver)
        w.mcpcomment("Hello Kannan"+ Keys.ENTER)

    def test_share_post(self, setup):
        e = Buzz_mcp(self.driver)
        e.mcpshare("Hello Sanjala")

    def test_delete_post(self, setup):
        r = Buzz_mcp(self.driver)
        r.mcpdelete()

    def test_edit_post(self, setup):
        t = Buzz_mcp(self.driver)
        # pic=r"C:\Users\senthamarai.kannan\PycharmProjects\page object model\testcases\frog.jpg"
        t.mcpeditpost("hi da gopal")

    @pytest.mark.run(order=3)
    # @pytest.mark.third
    def test_commentlike(self,setup):
        y = Buzz_mcp(self.driver)
        y.mcpcommentlike("commented"+ Keys.ENTER)