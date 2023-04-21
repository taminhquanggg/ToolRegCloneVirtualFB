from selenium import webdriver
from selenium.webdriver.common import keys
import time
import threading
import numpy as np





# def seleLoginFb(userAcc, passwdAcc, driver):
#     driver.find_element_by_id("email").send_keys(userAcc)
#     driver.find_element_by_id("pass").send_keys(passwdAcc)
#     driver.find_element_by_name("login").click()
#     time.sleep(5)
#
#
# def seleAddClone(self):
#     # self.driver.find_element_by_xpath("//body/div[1]/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
#     self.driver.find_element_by_link_text("Thêm").click()
#     time.sleep(2)
#     self.driver.find_element_by_link_text("1").click()
#     # self.driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[2]/i[1]").click()
#     time.sleep(1)
#     # self.driver.find_element_by_xpath("//body/div[6]/div[1]/div[1]/div[1]/ul[1]/li[4]").click()
#     self.driver.find_element_by_link_text("4").click()
#     time.sleep(1)
#     self.driver.find_element_by_xpath("//button[contains(text(),'Tạo người dùng thử nghiệm')]").click()
#     time.sleep(10)
#
# def seleChangePasswd(self):
#     # change passwd
#     listXpathBtn = ["/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[6]/div[1]/button[1]","/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[6]/div[1]/button[1]","/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[6]/div[1]/button[1]","/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[6]/div[1]/button[1]"]
#     for xpathBtn in listXpathBtn:
#         self.driver.find_element_by_xpath(xpathBtn).click()
#         time.sleep(1)
#         self.driver.find_element_by_link_text("Đổi tên hoặc mật khẩu của người dùng thử nghiệm này").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("password").send_keys("taminhquanga99")
#         self.driver.find_element_by_name("confirm_password").send_keys("taminhquanga99")
#         self.driver.find_element_by_xpath("//button[contains(text(),'Lưu')]").click()
#         time.sleep(5)
#
#         # add info to notepad
#     listXpathID = ["//tbody/tr[2]/td[3]", "//tbody/tr[3]/td[3]", "//tbody/tr[4]/td[3]", "//tbody/tr[5]/td[3]"]
#     try:
#         with open('cloneInfo.txt', 'a') as f:
#             for xpathID in listXpathID:
#                 f.writelines(str(self.driver.find_element_by_xpath(xpathID).text) + '\n')
#                 time.sleep(1)
#     finally:
#         f.close()
#     time.sleep(5)

def runtest(thread):
    f = open('goc.txt', encoding='utf8').readlines()
    dataThread = np.array_split(f, 15)
    for id in dataThread[thread]:
        id = id.split('|')
        Options = webdriver.ChromeOptions()
        Options.add_argument('--app=https://mbasic.facebook.com/Tessstt-105732885188696')
        driver = webdriver.Chrome(options=Options)
        x = (thread+1) * 200
        y = 10
        driver.set_window_rect(x, y, 200, 400)
        driver.find_element_by_name('email').send_keys(id[0])
        driver.find_element_by_name('pass').send_keys(id[1])

        time.sleep(1)
        driver.find_element_by_xpath('//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/a[1]').click()
        time.sleep(1)
        driver.quit()




def runThreads():
    threads = []
    for thread in range(15):
        threads += [threading.Thread(target=runtest,args={thread},)]
    for t in threads:
        t.start()


# main



runThreads()






# newDevice = seleToolReg()

# user = "0362280319"
# passwd = "quang021102"

# newDevice.seleLoginFb(user, passwd)
# newDevice.seleAddClone()
# newDevice.seleChangePasswd()



# "https://developers.facebook.com/apps/2738525826294154/roles/test-users/"

# /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]