import os
import pandas as pd
from rich import print
from pathlib import Path


class DataLoader:
    def __init__(self):
        self.DataPath = os.getenv("DATA_PATH")

    def loadCsv(self):
        try:
            if not Path(self.DataPath + "trips.csv").exists():
                raise "err"
            trip = pd.read_csv(self.DataPath + "trips.csv")
            return trip
        except:
            print("[italic bold blue]Initializing Data[italic bold blue/]")
            self.createCsv()

    def createCsv(self):
        trip = pd.DataFrame(
            columns=["tripName", "source", "destination", "days", "budget"]
        )
        trip.to_csv(self.DataPath + "trips.csv", index=False)
        self.loadCsv()
