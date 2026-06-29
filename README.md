# Offtrack Tracker

This is a small command-line tracker for offtrack. It lets you create trips and tells coin, and hour costs.

## Features

- Create trips with name, origin, destination, duration, and budget.
- Data stored locally in CSV file(s).
- List the trips with the coin and hour cost.

## Setup

Run the setup script:

```bash
sh ./setup.sh
```

This will create a python virtual environment, install all pip packages, and patches `.env`

## Configuration

The app configuration are stored in `.env`:

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

Create an itinerary for a trip:

```bash
python main.py itinerary "Trip Name"
```

\*itinerary creation is currently not functional.

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

## Author

Created by [ApishRana](https://github.com/ApishRana)
