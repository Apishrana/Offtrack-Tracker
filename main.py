import argcomplete
from dotenv import load_dotenv
import pandas as pd
from rich import print
from rich.prompt import Prompt, IntPrompt, Confirm
import argparse
from pathlib import Path
import sys

from Util.dataLoader import DataLoader


class Tracker:
    def __init__(self):
        self.dataLoader = DataLoader()
        self.trips = self.dataLoader.loadCsv()

    def run(self, arg):
        match arg.com:
            case "new":
                self.newTrip()
            case "list":
                self.printTrip()
            case "itinerary":
                self.newItinerary(arg.tripName)

    def printTrip(self):
        pass

    def newTrip(self):
        name = Prompt.ask("[blue]Trip name[/blue]")
        fromCity = Prompt.ask("[green]Where are you starting from[/green]")
        toCity = Prompt.ask("[green]Where are you going to[/green]")
        days = IntPrompt.ask("[green]How many days is the trip[/green]")

        self.trips.loc[len(self.trips)] = {
            "tripName": name,
            "fromCity": fromCity,
            "to": toCity,
            "days": days,
            "budget": None,
        }
        self.dataLoader.saveCsv(self.trips, "trips")

        print("[blue bold]Trip created successfully[/blue bold]")

        if Confirm.ask("[green]Proceed to create itinerary?[/green]"):
            self.newItinerary(name)
        else:
            path = Path(sys.argv[0]).resolve().relative_to(Path.cwd())
            print(
                f"[yellow]Okay, you can create the itinerary later using:[/yellow] \n[cyan]{path if path == path.stem else 'python '+str(path)} itinerary {name}[/cyan]"
            )

    def newItinerary(self, tripName):
        print(tripName)
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Offtrack")
    subParser = parser.add_subparsers(dest="com", required=True)
    subParser.add_parser("new")
    subParser.add_parser("list")
    itinerary = subParser.add_parser("itinerary")
    itinerary.add_argument("tripName")

    argcomplete.autocomplete(parser)
    load_dotenv()
    app = Tracker()
    try:
        arg = parser.parse_args()
    except:
        print(
            "[red bold] invalid argument [green]try using -h or --help for use guide[green /] [red bold/]"
        )
    finally:
        app.run(arg)
