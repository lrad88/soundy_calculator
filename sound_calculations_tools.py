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
combo3 = QComboBox()
combo4 = QComboBox()


class SpeedOfSound(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sound Calculations Tool")
        grid = QGridLayout()

        tool_label = QLabel("Speed of a sound:")

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

# reverb calculator
        tool_label2 = QLabel("Reverb calculator:")
        bpm_label = QLabel("BPM:")
        self.BPM_line_edit = QLineEdit()
        Pre_delay_label = QLabel("Pre-delay duration:")
        combo3.addItems(
            ["0 ms", "0.1 ms", "1 ms", "10 ms", "30 ms", "1/512 note triplet",
             "1/512 note", "1/512 note dotted", "1/256 note triplet", "1/256 note",
             "1/256 note dotted", "1/128 note triplet", "1/128 note", "1/128 note dotted",
             "1/64 note triplet", "1/64 note", "1/64 note dotted", "1/32 note triplet",
             "1/32 note", "1/32 note dotted"])
        pre_delay_decay_label = QLabel("Pre-delay + Decay duration:")
        combo4.addItems(
            ["1/32 note", "1/32 note dotted", "1/16 note triplet", "1/16 note",
             "1/16 note dotted", "1/8 note triplet", "1/8 note", "1/8 note dotted",
             "1/4 note triplet", "1/4 note", "1/4 note dotted", "1/2 note triplet",
             "1/2 note", "1/2 note dotted", "1 note triplet", "1 note", "1 note dotted",
             "2 notes triplet", "2 notes", "2 notes dotted", "4 notes triplet", "4 notes",
             "4 notes dotted", "8 notes triplet", "8 notes", "8 notes dotted"])

        calculate_button2 = QPushButton("Calculate")
        calculate_button2.clicked.connect(self.calculate_sos)

        self.output_label2 = QLabel("")


        grid.addWidget(tool_label, 0, 0)
        grid.addWidget(distance_label, 1, 0)
        grid.addWidget(self.distance_line_edit, 1, 1)
        grid.addWidget(combo, 1, 2)
        grid.addWidget(temp_label, 2, 0)
        grid.addWidget(self.temp_line_edit, 2, 1)
        grid.addWidget(combo2, 2, 2)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

# reverb calculator

        grid.addWidget(tool_label2, 5, 0)
        grid.addWidget(bpm_label, 6, 0)
        grid.addWidget(self.BPM_line_edit, 6, 1)
        grid.addWidget(Pre_delay_label, 7, 0)
        grid.addWidget(combo3, 7, 1)
        grid.addWidget(pre_delay_decay_label, 8, 0)
        grid.addWidget(combo4, 8, 1)
        grid.addWidget(calculate_button2, 9, 1)
        grid.addWidget(self.output_label2, 10, 0, 1, 2)


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
