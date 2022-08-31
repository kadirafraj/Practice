import pytest

from pageobjects.LoginPage import LoginPage
from testdata.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_login(self, getdata):
        log = self.getlogger()
        login= LoginPage(self.driver)
        login.getemail().send_keys(getdata["Username"])
        login.getpassword().send_keys(getdata["Password"])
        login.clickloginbutton().click()
        value= login.Home().is_displayed()
        assert "True"==str(value)
        log.info("Logged in successfully")
        #changes for git hub
        #new changes

    @pytest.fixture(params=LoginPageData.gettestdata("test_case1"))
    def getdata(self, request):
        return request.param
