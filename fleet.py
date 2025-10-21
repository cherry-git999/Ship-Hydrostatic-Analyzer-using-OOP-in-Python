# fleet.py
import csv
from ship import Ship

class Fleet:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def show_all(self):
        print("\n⚓ Fleet Summary:")
        for ship in self.ships:
            ship.show_details()

    def save_to_csv(self, filename="fleet_data.csv"):
        """Save fleet data to CSV file."""
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Length", "Breadth", "Depth", "Draft", "Mass", "Floats"])
            for s in self.ships:
                writer.writerow([s.name, s.length, s.breadth, s.depth, s.draft, s.mass, "Yes" if s.will_float() else "No"])
        print(f"\n✅ Fleet data saved to {filename}")

    def load_from_csv(self, filename="fleet_data.csv"):
        """Load fleet data from CSV file."""
        self.ships.clear()
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ship = Ship(row["Name"], float(row["Length"]), float(row["Breadth"]),
                                float(row["Depth"]), float(row["Draft"]), float(row["Mass"]))
                    self.ships.append(ship)
            print(f"\n📂 Loaded {len(self.ships)} ships from {filename}")
        except FileNotFoundError:
            print(f"⚠️ File {filename} not found!")
