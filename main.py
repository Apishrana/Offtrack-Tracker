from dotenv import load_dotenv
import pandas as pd

from Util.dataLoader import DataLoader


class Tracker:
    def __init__(self):
        self.dataLoader = DataLoader()
        self.trips = self.dataLoader.loadCsv()

    def run(self):
        pass


if __name__ == "__main__":
    load_dotenv()
    app = Tracker()
    app.run()
