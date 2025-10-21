# analyzer.py
import math
import matplotlib.pyplot as plt

class HydrostaticAnalyzer:
    def __init__(self, ship):
        self.ship = ship

    def metacentric_height(self):
        """Approximate GM (metacentric height)."""
        KB = 0.53 * self.ship.draft        # center of buoyancy
        BM = (self.ship.breadth ** 2) / (12 * self.ship.draft)
        KG = 0.6 * self.ship.depth         # center of gravity
        GM = KB + BM - KG
        return round(GM, 3)

    def stability_curve(self):
        """Plot Righting Arm (GZ) vs Heel Angle."""
        GM = self.metacentric_height()
        angles = list(range(0, 65, 5))
        GZ = [round(GM * math.sin(math.radians(a)), 3) for a in angles]

        plt.figure(figsize=(7, 4))
        plt.plot(angles, GZ, marker='o', color='navy', label=f'{self.ship.name}')
        plt.title(f'Stability Curve - {self.ship.name}', fontsize=14)
        plt.xlabel("Heel Angle (°)")
        plt.ylabel("Righting Arm (m)")
        plt.grid(True)
        plt.legend()
        plt.show()
