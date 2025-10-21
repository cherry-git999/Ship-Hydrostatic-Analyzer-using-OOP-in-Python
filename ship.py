# ship.py
import math

class Ship:
    def __init__(self, name, length, breadth, depth, draft, mass):
        self.name = name
        self.length = length
        self.breadth = breadth
        self.depth = depth
        self.draft = draft
        self.mass = mass  # in tonnes
        self.water_density = 1025  # kg/m³ (sea water)

    def displacement(self):
        """Return displacement volume in cubic meters."""
        volume = self.length * self.breadth * self.draft * self.block_coefficient()
        return round(volume, 2)

    def block_coefficient(self):
        """Approximate block coefficient based on ship geometry."""
        return round((self.mass * 1000) / (self.water_density * self.length * self.breadth * self.draft), 3)

    def buoyant_force(self):
        """Calculate buoyant force (in Newtons)."""
        g = 9.81
        return round(self.water_density * g * self.displacement(), 2)

    def weight_force(self):
        """Ship weight in Newtons."""
        g = 9.81
        return round(self.mass * 1000 * g, 2)

    def will_float(self):
        """Check if the ship floats."""
        return self.buoyant_force() >= self.weight_force()

    def show_details(self):
        print(f"\n🛳 Ship Name: {self.name}")
        print(f"Length: {self.length} m, Breadth: {self.breadth} m, Depth: {self.depth} m, Draft: {self.draft} m")
        print(f"Mass: {self.mass} tonnes")
        print(f"Block Coefficient (Cb): {self.block_coefficient()}")
        print(f"Displacement Volume: {self.displacement()} m³")
        print(f"Buoyant Force: {self.buoyant_force():,.2f} N")
        print(f"Weight Force: {self.weight_force():,.2f} N")
        print("Status:", "✅ Floats" if self.will_float() else "❌ Sinks")
