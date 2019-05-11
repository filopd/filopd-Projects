import os
from pathlib import Path

class paths:
    def __init__(self):
        self.path = ""
        self.found = ""
        self.t = ""

    def get_project_path(self):
        self.path = Path(os.path.dirname(__file__))
        # print("Project > ", str(self.path))
        return self.path

