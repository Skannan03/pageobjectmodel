import pytest

from POM_Login.Login import Login
@pytest.mark.usefixtures("setup")

class Testlogin:
    def test_Login(self,setup):
        obj = Login(setup)
        obj.login("Admin","admin123")
        obj.logout()
        expected="OrangeHRM"
        actual= obj.get_title(expected)
        print(f"Expected{expected} Actual : {actual}")
