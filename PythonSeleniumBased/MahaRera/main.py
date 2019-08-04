import datetime
from src.paths import paths
from src.maharera_searchPage import searchPage
class start:

    def __init__(self):
        self.p1 = paths()
        try:
            self.chrome_driver_path = str(self.p1.get_project_path()) + "/chromedriver_win32/chromedriver.exe"
        except Exception as inst:
            print("Unknown Error !")
            print(type(inst), str(inst.args))


if __name__ == '__main__':
    State = "MAHARASHTRA"
    # id State
    Division = "Konkan"
    # str(input("Enter the Division (Amravati, Aurangabad, Konkan, Nagpur, Nashik, Pune) : "))
    # id Division
    District = "Thane"
    # str(input("Enter the District (Thane, Palghar, Raigarh, Mumbai City, Mumbai Suburban, Sindhudurg) : "))
    Taluka = "Thane"
    # id Taluka
    Village = "Mira-Bhayandar (M Corp.)"
    # id Village
    # YYYY, MM, DD >> CompletionDate_From = 2019101
    CompletionDate_From = {'Year':'2018', 'Month':'Oct', 'Day':'1'}
    # id CompletionDate_From >>> datetime.date(2020, 12, 31) >> CompletionDate_To = 20201231
    CompletionDate_To = {'Year':'2021', 'Month':'Dec', 'Day':'31'}
    # CompletionDate_To
    PropertyType = "Residential"
    # id PType
    program = start()
    searchPage1 = searchPage(str(program.chrome_driver_path))
    listOfProjects = searchPage1.find_result(str(program.chrome_driver_path), State, Division, District, Taluka, Village, CompletionDate_From, CompletionDate_To, PropertyType)










