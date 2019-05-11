from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class searchPage:

    def __init__(self, chrome_driver_path):
        self.datefield = None
        self.Srno = ""
        self.Project = ""
        self.PromoterName = ""
        self.counter = ""
        self.TotalRecords = ""
        self.table = ""
        self.link = ""
        self.listOfLinks = ""

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

    def find_result(self, chrome_driver_path, State, Division, District, Taluka, Village, CompletionDate_From, CompletionDate_To, PropertyType):
        try:
            # Select the Radio Box
            self.driver.find_element_by_id("Promoter").click()
            self.driver.find_element_by_name("btnAdvance").click()
            self.driver.find_element_by_id("State").send_keys(State)
            self.driver.find_element_by_id("Division").send_keys(Division)
            self.driver.find_element_by_id("District").send_keys(District)
            self.driver.find_element_by_id("Taluka").send_keys(Taluka)
            self.driver.find_element_by_id("Village").send_keys(Village)
            self.driver.find_element_by_id("CompletionDate_From").click()
            time.sleep(2)
            # Skip this year in from date, it is not working as expected
            # self.driver.find_element_by_class_name("ui-datepicker-year").send_keys(CompletionDate_From['Year'])
            self.driver.find_element_by_class_name("ui-datepicker-month").send_keys(CompletionDate_From['Month'])
            self.driver.find_element_by_class_name("ui-state-default").click()
            time.sleep(2)
            self.driver.find_element_by_id("CompletionDate_To").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("ui-datepicker-month").send_keys(CompletionDate_To['Month'])
            self.driver.find_element_by_class_name("ui-datepicker-year").send_keys(CompletionDate_To['Year'])
            time.sleep(2)
            self.driver.find_element_by_class_name("ui-state-default").click()
            time.sleep(2)
            self.driver.find_element_by_id("PType").send_keys(PropertyType)
            self.driver.find_element_by_id("btnSearch").click()
            time.sleep(5)
            self.TotalRecords = int(self.driver.find_element_by_id("TotalRecords").get_attribute("value"))
            self.table = self.driver.find_elements_by_tag_name("a")
            self.driver.find_elements_by_link_text("View")
            print("ThiRD \n", str(self.table))

            self.counter = 1
            self.link = []

            for self.i in self.table:
                if "https://maharerait.mahaonline.gov.in/PrintPreview/PrintPreview?" in (str(self.i.get_attribute("href"))):
                    self.link = str(self.i.get_attribute("href"))
                    self.driver1 = webdriver.Chrome(chrome_driver_path)

                    # # enable browser logging
                    # self.d = DesiredCapabilities.CHROME
                    # self.d['loggingPrefs'] = {'browser': 'ALL'}
                    # self.driver1 = webdriver.Chrome(desired_capabilities=self.d)

                    self.driver1.get(self.link)
                    self.driver1.maximize_window()

                    # self.driver1.get_log("Preview")
                    # print("HI >>", str(self.driver1))
                    #

                    time.sleep(5)
                    # print messages
                    for entry in self.driver1.get_log('browser'):
                        print(entry)
                    self.driver1.quit()
                    if self.counter == 1:
                        return ""
                self.counter = self.counter + 1

        except Exception as inst:
            print("Unknown Error !")
            print(type(inst), str(inst.args))
        finally:
            time.sleep(5)
            self.driver.quit()
