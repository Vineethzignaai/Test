from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        # open home page
        #self.open("https://practice.automationbro.com/")
        ## please add the rev max url
        self.open("https://zignaai-dev.outsystemsenterprise.com/Revmax_CS/Login")

        # assert page title
        #self.assert_title("Practice E-Commerce Site – Automation Bro")

        #assert logo
        self.assert_element(".login-logo")

        # login page
        self.assert_text("Username")
        self.assert_text("Password")
        self.type("#Input_UsernameVal", "Sample@sample.com")
        self.type("#Input_PasswordVal", "000000")
        self.click('button[type="submit"]')
        #self.go_forward()




    #def Landing_Screen(self): create different class like this

        self.open("https://zignaai-dev.outsystemsenterprise.com/Revmax_Pat/LandingScreen")
        self.assert_title("LandingScreen")
        #self.click("class="icon fa fa-angle-right fa-3x"")

        self.open("https://zignaai-dev.outsystemsenterprise.com/Revmax_Pat/AuditClaimScreen")

