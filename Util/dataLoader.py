import os


class DataLoader:
    def __init__(self):
        self.DataPath = os.getenv("DATA_PATH")
        print(self.DataPath)
