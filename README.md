# Offtrack Tracker

This is a small command-line tracker for offtrack. It lets you create trips and tells coin, and hour costs.

## Features

- Create trips with name, origin, destination, duration, and budget.
- Store trip data locally as CSV.
- List saved trips with the coin and hour cost.

## Setup

Run the setup script:

```bash
sh ./setup.sh
```

This creates a virtual environment, installs dependencies, and patches `.env`

## Configuration

The app have its configuration in `.env`:

```env
DATA_PATH=./Data/
USD=94.53
COIN_RATE=2.5
HOUR_RATE=20
```

- `DATA_PATH`: Path to the data folder.
- `USD`: USD to INR Fallback
- `COIN_RATE`: Coin cost per USD.
- `HOUR_RATE`: Number of coins earned per hour.

## Usage

Activate the virtual environment using:

```bash
source venv/bin/activate
```

Create a new trip:

```bash
python main.py new
```

List all trips:

```bash
python main.py list
```

Create an itinerary for an existing trip:

```bash
python main.py itinerary "Trip Name"
```

\*itinerary creation is currently not fuctional.

## Build

Run the build script:

```bash
./build.sh
```

The executable is generated in the `dist/` directory.

## Project Structure

```text
.
├── README.md
├── Util
│   ├── conversion.py
│   └── dataLoader.py
├── build.sh
├── main.py
├── requirements.txt
└── setup.sh

2 directories, 7 files
```

## Data

Data is saved to:

```text
Data/trips.csv
```

The data folder location can be changed with `DATA_PATH` variable in `.env`.
