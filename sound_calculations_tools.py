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
combo5 = QComboBox()
combo6 = QComboBox()


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
        pre_delay_label = QLabel("Pre-delay duration:")
        combo3.addItems(["0 ms", "0.1 ms", "1 ms", "10 ms", "30 ms",
                        "1/512 note", "1/256 note", "1/128 note",
                         "1/64 note", "1/32 note"])

        combo5.addItems(["---", "dotted", "triplet"])

        pre_delay_decay_label = QLabel("Pre-delay + Decay duration:")
        combo4.addItems(["1/32 note","1/16 note","1/8 note","1/4 note",
             "1/2 note", "1 note", "2 notes", "4 notes","8 notes"])

        combo6.addItems(["---", "dotted", "triplet"])

        calculate_button2 = QPushButton("Calculate")
        calculate_button2.clicked.connect(self.calculate_reverb)

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
        grid.addWidget(pre_delay_label, 7, 0)
        grid.addWidget(combo3, 7, 1)
        grid.addWidget(combo5, 7, 2)
        grid.addWidget(pre_delay_decay_label, 8, 0)
        grid.addWidget(combo4, 8, 1)
        grid.addWidget(combo6, 8, 2)
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

    def calculate_reverb(self):
        BPM = float(self.BPM_line_edit.text())

        pre_delay = {
            "0 ms": 0,
            "0.1 ms": 0.1,
            "1 ms": 1,
            "10 ms": 10,
            "30 ms": 30,
            "1/512 note": 128,
            "1/256 note": 64,
            "1/128 note": 32,
            "1/64 note": 16,
            "1/32 note": 8,
        }

        pre_delay_decay = {
            "1/32 note": 8,
            "1/16 note": 4,
            "1/8 note": 2,
            "1/4 note": 1,
            "1/2 note": 0.5,
            "1 note": 0.250,
            "2 notes": 0.125,
            "4 notes": 0.0625,
            "8 notes": 0.03125
        }

        extra = {
            "dotted": 1.5,
            "triplet": 2
        }

        if combo3.currentText() in pre_delay:
            formula2 = pre_delay[combo3.currentText()]

            if combo4.currentText() in pre_delay_decay:
                formula21 = pre_delay_decay[combo4.currentText()]

                #formula2111 = (((60000 / BPM) - formula2) / formula21)

                #self.output_label2.setText(f"{round(formula2111, 3)}")

                if combo5.currentText() == "dotted":
                    extra1 = extra[combo5.currentText()]

                    formula2111 = (((60000 / BPM) - formula2) / formula21) * extra1

                    self.output_label2.setText(f"{round(formula2111, 3)}")

                elif combo5.currentText() == "triplet":
                    extra1 = extra[combo5.currentText()]

                    formula2111 = ((((60000 / BPM) - formula2) / formula21) / 3) * extra1

                    self.output_label2.setText(f"{round(formula2111, 3)}")

                elif combo5.currentText() == "---":

                    formula2111 = (((60000 / BPM) - formula2) / formula21)

                    self.output_label2.setText(f"{round(formula2111, 3)}")



                if combo6.currentText() == "dotted":
                    extra2 = extra[combo6.currentText()]

                    formula2111 = (((60000 / BPM) - formula2) / formula21) * extra2

                    self.output_label2.setText(f"{round(formula2111, 3)}")

                elif combo6.currentText() == "triplet":
                    extra2 = extra[combo6.currentText()]

                    formula2111 = ((((60000 / BPM) - formula2) / formula21) / 3) * extra2

                    self.output_label2.setText(f"{round(formula2111, 3)}")

                elif combo6.currentText() == "---":

                    formula2111 = ((((60000 / BPM) - formula2) / formula21))

                    self.output_label2.setText(f"{round(formula2111, 3)}")


SOS = SpeedOfSound()
SOS.show()
sys.exit(app.exec())
