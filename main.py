from Util.dataLoader import DataLoader
from dotenv import load_dotenv


class Tracker:
    def __init__(self):
        load_dotenv()
        DataLoader()
