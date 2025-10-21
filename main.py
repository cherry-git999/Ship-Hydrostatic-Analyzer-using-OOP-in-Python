# main.py
from ship import Ship
from analyzer import HydrostaticAnalyzer
from fleet import Fleet

def main():
    # Create individual ships
    ship1 = Ship("Cherry", 120, 20, 15, 8, 15000)
    ship2 = Ship("Neptune", 95, 16, 12, 6, 8000)
    ship3 = Ship("AquaStar", 60, 10, 8, 4.5, 2500)

    # Create analyzer for one ship
    analyzer = HydrostaticAnalyzer(ship1)
    ship1.show_details()
    print(f"\nMetacentric Height (GM): {analyzer.metacentric_height()} m")
    analyzer.stability_curve()

    # Manage fleet
    fleet = Fleet()
    fleet.add_ship(ship1)
    fleet.add_ship(ship2)
    fleet.add_ship(ship3)
    fleet.show_all()

    # Save and reload data
    fleet.save_to_csv()
    fleet.load_from_csv()

if __name__ == "__main__":
    main()
