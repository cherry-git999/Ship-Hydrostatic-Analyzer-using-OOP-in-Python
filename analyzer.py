import numpy as np

class HydroAnalyzer:
    def __init__(self, ship):
        self.ship = ship
        self.rho = 1025  # seawater density kg/m³
        self.g = 9.81

    def displacement(self):
        return self.ship.length * self.ship.breadth * self.ship.draft * self.rho / 1000

    def buoyant_force(self):
        return self.displacement() * self.g

    def block_coefficient(self):
        return self.displacement() / (
            self.ship.length * self.ship.breadth * self.ship.depth * self.rho / 1000
        )

    def is_floating(self):
        return self.displacement() >= self.ship.mass

    def gz_curve(self):
        angles = np.linspace(0, 60, 30)
        gm = 1.2  # assumed GM
        gz = gm * np.sin(np.radians(angles))
        return angles, gz
