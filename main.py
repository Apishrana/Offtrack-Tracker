import argcomplete
from dotenv import load_dotenv
import pandas as pd
from rich import print, box
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
import argparse
from pathlib import Path
import math
import sys
import os

from Util.dataLoader import DataLoader
from Util.conversion import usdRate


class Tracker:
    def __init__(self):
        self.dataLoader = DataLoader()
        self.trips = self.dataLoader.loadCsv()
        self.coin_rate = float(os.getenv("COIN_RATE", "0"))
        self.hour_rate = float(os.getenv("HOUR_RATE", "0"))
        self.usdRate = usdRate()

    def run(self, arg):
        match arg.com:
            case "new":
                self.newTrip()
            case "list":
                self.printTrip()
            case "itinerary":
                self.newItinerary(arg.tripName)

    def printTrip(self):
        print()
        console = Console()

        if self.trips.empty:
            console.print("[red]No trips found.[/red]")
            return

        table = Table(
            title="Trips",
            box=box.SIMPLE,
            header_style="bold cyan",
            expand=True,
        )

        table.add_column("Trip", style="bold white", no_wrap=True)
        table.add_column("From", style="green")
        table.add_column("To", style="cyan")
        table.add_column("Days", justify="right", style="yellow")
        table.add_column("Budget(Rs.)", justify="right", style="green")
        table.add_column("Coin Cost", justify="right", style="green")
        table.add_column("Hour Cost", justify="right", style="green")

        for _, row in self.trips.iterrows():
            days = int(row["days"]) if pd.notna(row["days"]) else 0
            budget = float(row["budget"]) if pd.notna(row["budget"]) else 0

            coinCost = budget / self.usdRate * self.coin_rate
            hourCost = coinCost / self.hour_rate

            table.add_row(
                str(row["tripName"]),
                str(row["from"]),
                str(row["to"]),
                str(int(days)),
                f"₹{math.ceil(budget)}" if budget else "-",
                f"{math.ceil(coinCost)}" if budget else "-",
                f"{math.ceil(hourCost)}" if budget else "-",
            )
        console.print(table)

    def newTrip(self):
        name = Prompt.ask("[blue]Trip name[/blue]")
        fromCity = Prompt.ask("[green]Where are you starting from[/green]")
        toCity = Prompt.ask("[green]Where are you going to[/green]")
        days = IntPrompt.ask("[green]How many days is the trip[/green]")

        self.trips.loc[len(self.trips)] = {
            "tripName": name,
            "from": fromCity,
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
        print("Trip name", tripName)
        print()
        print()
        print("Coming soon...")


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
