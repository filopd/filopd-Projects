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
    print("HEllo")
    program = start()
    searchPage1 = searchPage(str(program.chrome_driver_path))
    searchPage1.find_result()








