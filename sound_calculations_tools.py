"""
the goal of this program is to calculate the amount of time in
seconds it takes for a sound to travel from one point to another
accounting for temperature, refer to:
http://www.sengpielaudio.com/calculator-speedsound.htm and
 https://www.sfu.ca/sonic-studio-webdav/handbook/Speed__Of_Sound.html for
mathematical reference

// the website recommends 331.3 as the speed of sound through air
before it interacts with temperature, i changed this to 331.216 so
that the speed of sound at room temperature calculates to the more
accurate 343.216 m/s

// speed of sound at room temperature is 343.216 m/s at 20 degrees c
"""

from PyQt6.QtWidgets import QApplication, QLabel, \
    QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys

app = QApplication(sys.argv)
combo = QComboBox()
combo2 = QComboBox()


class SpeedOfSound(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sound Calculations Tool")
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        combo.addItems(
            ["Meters (M)", "Centimeters (CM)", "Feet (ft)", "Inches (in)"])

        temp_label = QLabel("Temp:")
        self.temp_line_edit = QLineEdit()

        combo2.addItems(
            ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_sos)

        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(combo, 0, 2)
        grid.addWidget(temp_label, 1, 0)
        grid.addWidget(self.temp_line_edit, 1, 1)
        grid.addWidget(combo2, 1, 2)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_sos(self):
        distance = float(self.distance_line_edit.text())
        temp = float(self.temp_line_edit.text())

        unit_to_formula = {
            "Meters (M)": 331.216 + (0.6 * temp),
            "Centimeters (CM)": ((331.216 + (0.6 * temp)) * 100),
            "Feet (ft)": 1086.6667 + (0.6 * temp),
            "Inches (in)": ((1086.6667 + (0.6 * temp)) * 12)
        }

        if combo.currentText() in unit_to_formula:
            formula = unit_to_formula[combo.currentText()]
            combo_choice = distance / formula
            self.output_label.setText(
                f"Sound will reach point in: {round(combo_choice, 3)} seconds")
        else:
            self.output_label.setText("Invalid unit of temperature selected.")


SOS = SpeedOfSound()
SOS.show()
sys.exit(app.exec())
