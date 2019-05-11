from selenium import webdriver

class searchPage:

    def __init__(self, chrome_driver_path):
        try:
            self.driver = webdriver.Chrome(chrome_driver_path)
            # print(" Run: ", str(self.driver))
            self.driver.get("https://maharerait.mahaonline.gov.in/SearchList/Search")
            self.driver.maximize_window()
        except Exception as inst:
            print("Unknown Error !")
            print(type(inst), str(inst.args))
        finally:
            pass
            # self.driver.quit()

    def find_result(self):
        try:
            # Select the Radio Box
            element = self.driver.find_element_by_id("Promoter").click()
            print("element >> ", str(element))
        except Exception as inst:
            print("Unknown Error !")
            print(type(inst), str(inst.args))
