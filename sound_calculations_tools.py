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

the second goal is an accurate reverb and delay calculator
referenced from https://passionforedm.com/blog/reverbs-pre-delay-decay-durations/
"""

from PyQt6.QtWidgets import QApplication, QLabel, \
    QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys, re

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
        self.distance_line_edit = QLineEdit("")

        combo.addItems(
            ["Meters (M)", "Centimeters (CM)", "Feet (ft)", "Inches (in)"])

        self.previous_index = 0

        def qline_distance_update(index):

            distance_text = self.distance_line_edit.text()

            if not distance_text or not distance_text.replace('.', '',
                                                              1).isdigit():
                # Handle the case where the text is empty or not a valid float value

                self.distance_line_edit.setText(
                    "0")  # Set a default value if the text is empty or not a valid float

                return

            distance_value = float(self.distance_line_edit.text())
            if index == 0:  # Meters (M)
                if self.previous_index == 1:
                    to_centimeters = (distance_value / 100)
                    self.distance_line_edit.setText(f"{(to_centimeters):.2f}")
                elif self.previous_index == 2:
                    to_feet = (distance_value / 3.28084)
                    self.distance_line_edit.setText(f"{(to_feet):.2f}")
                elif self.previous_index == 3:
                    to_inches = (distance_value / 39.3701)
                    self.distance_line_edit.setText(f"{(to_inches):.2f}")


            elif index == 1:  # Centimeters (CM)

                if self.previous_index == 0:
                    to_meters = (distance_value * 100)
                    self.distance_line_edit.setText(f"{(to_meters):.2f}")
                elif self.previous_index == 2:
                    to_feet = (distance_value / 0.0328084)
                    self.distance_line_edit.setText(f"{(to_feet):.2f}")
                elif self.previous_index == 3:
                    to_inches = (distance_value / 0.393701)
                    self.distance_line_edit.setText(f"{(to_inches):.2f}")

            elif index == 2:  # Feet (ft)

                if self.previous_index == 0:
                    to_meters = (distance_value * 3.28084)
                    self.distance_line_edit.setText(f"{(to_meters):.2f}")
                elif self.previous_index == 1:
                    to_centimeters = (distance_value / 30.48)
                    self.distance_line_edit.setText(f"{(to_centimeters):.2f}")
                elif self.previous_index == 3:
                    to_inches = (distance_value / 12)
                    self.distance_line_edit.setText(f"{(to_inches):.2f}")

            elif index == 3:  # Inches (in)

                if self.previous_index == 0:
                    to_meters = (distance_value * 39.37)
                    self.distance_line_edit.setText(f"{(to_meters):.2f}")
                elif self.previous_index == 1:
                    to_centimeters = (distance_value / 2.54)
                    self.distance_line_edit.setText(f"{(to_centimeters):.2f}")
                elif self.previous_index == 2:
                    to_feet = (distance_value * 12)
                    self.distance_line_edit.setText(f"{(to_feet):.2f}")

            self.previous_index = index

        combo.currentIndexChanged.connect(qline_distance_update)
        combo.currentIndexChanged.connect(self.calculate_sos)

        temp_label = QLabel("Temp:")
        self.temp_line_edit = QLineEdit("20")

        combo2.addItems(
            ["Celsius (C)", "Fahrenheit (F)"])

        def qline_temp_update(index):  # this def is for changing the temp
            # in the QLineEdit() from celsius to fahrenheit, doing the
            # calculation for you

            temp_text = self.temp_line_edit.text()

            if not temp_text or not (temp_text.replace('.', '',1).isdigit() or
            (temp_text.startswith('-') and temp_text[1:].replace('.', '', 1).isdigit())):

                # Handle the case where the text is empty or not a valid float value

                self.temp_line_edit.setText(
                    "0")  # Set a default value if the text is empty or not a valid float
                return

            temp_value = float(self.temp_line_edit.text())

            if index == 0:  # Celsius (C)
                # Convert the temperature to Fahrenheit
                temp_in_fahrenheit = (temp_value - 32) / 1.8
                self.temp_line_edit.setText(f"{(temp_in_fahrenheit):.2f}")
            elif index == 1:  # Fahrenheit (F)
                # Convert the temperature to Celsius
                temp_in_celsius = (temp_value * 1.8) + 32
                self.temp_line_edit.setText(f"{(temp_in_celsius):.2f}")

        combo2.currentIndexChanged.connect(qline_temp_update)
        combo2.currentIndexChanged.connect(self.calculate_sos)

        self.output_label = QLabel("")

        # reverb calculator
        tool_label2 = QLabel("Reverb calculator:")
        bpm_label = QLabel("BPM:")

        self.BPM_line_edit = QLineEdit("")

        def qline_BPM_update():

            bpm_text = self.BPM_line_edit.text()

            numeric_parts = re.findall(r'\d+', self.BPM_line_edit.text())
            numeric_value = ''.join(numeric_parts)
            if numeric_value:
                self.BPM_line_edit.setText(numeric_value)

            elif bpm_text or not bpm_text.replace('.', '',1).isdigit():
                # Handle the case where the text is empty or not a valid float value

                self.BPM_line_edit.setText(
                    "128")  # Set a default value if the text is empty or not a valid float
                return

        reverb_calc_combo_boxes_updater = [combo3, combo4, combo5, combo6]

        for combo_box in reverb_calc_combo_boxes_updater:
            combo_box.currentIndexChanged.connect(qline_BPM_update)

        pre_delay_label = QLabel("Pre-delay duration:")
        combo3.addItems(["0 ms", "0.1 ms", "1 ms", "10 ms", "30 ms",
                         "1/512 note", "1/256 note", "1/128 note",
                         "1/64 note", "1/32 note"])

        combo3.currentIndexChanged.connect(self.calculate_reverb)

        combo5.addItems(["---", "dotted", "triplet"])

        combo5.currentIndexChanged.connect(self.calculate_reverb)

        self.output_label3 = QLabel("")

        pre_delay_decay_label = QLabel("Pre-delay + Decay duration:")
        combo4.addItems(["1/32 note", "1/16 note", "1/8 note", "1/4 note",
                         "1/2 note", "1 note", "2 notes", "4 notes",
                         "8 notes"])

        combo4.currentIndexChanged.connect(self.calculate_reverb)

        combo6.addItems(["---", "dotted", "triplet"])

        combo6.currentIndexChanged.connect(self.calculate_reverb)

        self.output_label4 = QLabel("")

        decay_label = QLabel("Decay duration:")

        self.output_label2 = QLabel("")

        grid.addWidget(tool_label, 0, 0)
        grid.addWidget(distance_label, 1, 0)
        grid.addWidget(self.distance_line_edit, 1, 1)
        grid.addWidget(combo, 1, 2)
        grid.addWidget(temp_label, 2, 0)
        grid.addWidget(self.temp_line_edit, 2, 1)
        grid.addWidget(combo2, 2, 2)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

        # reverb calculator

        grid.addWidget(tool_label2, 5, 0)
        grid.addWidget(bpm_label, 6, 0)
        grid.addWidget(self.BPM_line_edit, 6, 1)
        grid.addWidget(pre_delay_label, 7, 0)
        grid.addWidget(combo3, 7, 1)
        grid.addWidget(combo5, 7, 2)
        grid.addWidget(self.output_label3, 8, 1, 1, 2)
        grid.addWidget(pre_delay_decay_label, 9, 0)
        grid.addWidget(combo4, 9, 1)
        grid.addWidget(combo6, 9, 2)
        grid.addWidget(self.output_label4, 11, 1, 1, 2)
        grid.addWidget(decay_label, 13, 0)
        grid.addWidget(self.output_label2, 14, 0, 1, 2)

        self.setLayout(grid)



    def calculate_sos(self):

        if (self.distance_line_edit.text() and self.temp_line_edit.text()) == "":
            # Handle the case where the text is empty or not a valid float value

            self.distance_line_edit.setText("0")
            self.temp_line_edit.setText("0")

        if any(char.isalpha() for char in self.distance_line_edit.text()):
            self.distance_line_edit.setText("0")

        if any(char.isalpha() for char in self.temp_line_edit.text()):
            self.temp_line_edit.setText("0")


        distance = float(self.distance_line_edit.text())
        temp = float(self.temp_line_edit.text())

        unit_to_formula_celsius = {
            "Meters (M)": 331.216 + ((0.6 * temp)),
            "Centimeters (CM)": ((331.216 + (0.6 * temp)) * 100),
            "Feet (ft)": 1086.6667 + (0.6 * temp),
            "Inches (in)": ((1086.6667 + (0.6 * temp)) * 12)
        }

        unit_to_formula_fahrenheit = {
            "Meters (M)": 331.216 + (((temp - 32) / 1.8) * 0.6),
            "Centimeters (CM)": ((331.216 + ((temp - 32) / 1.8) * 0.6) * 100),
            "Feet (ft)": 1086.6667 + (((temp - 32) / 1.8) * 0.6),
            "Inches (in)": ((1086.6667 + ((temp - 32) / 1.8) * 0.6) * 12)
        }

        if combo.currentText() in unit_to_formula_celsius and combo2.currentText() == "Celsius (C)":
            formula = unit_to_formula_celsius[combo.currentText()]
            combo_choice = distance / formula
            self.output_label.setText(
                f"Sound will reach point in: {round(combo_choice, 3)} seconds")

        elif combo.currentText() in unit_to_formula_fahrenheit and combo2.currentText() == "Fahrenheit (F)":

            formula = unit_to_formula_fahrenheit[combo.currentText()]
            combo_choice = distance / formula
            self.output_label.setText(
                f"Sound will reach point in: {round(combo_choice, 3)} seconds")


    def numbers(self):
        self.BPM = float(self.BPM_line_edit.text())

        self.pre_delay1 = {
            "0 ms": 0,
            "0.1 ms": 0.100,
            "1 ms": 1,
            "10 ms": 10,
            "30 ms": 30,
        }

        self.pre_delay2 = {

            "1/512 note": 128,
            "1/256 note": 64,
            "1/128 note": 32,
            "1/64 note": 16,
            "1/32 note": 8
        }

        self.pre_delay_decay = {
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

    def calculate_reverb(self):

        self.numbers()

        pre_delayo = 60000 / self.BPM
        decay_amt = self.pre_delay_decay[combo4.currentText()]
        delay_decay = ((60000 / self.BPM) / decay_amt)

        if combo3.currentText() in self.pre_delay1 and combo6.currentText() == "triplet":
            pre_delay_amt1 = self.pre_delay1[combo3.currentText()]

            self.output_label4.setText(f"{((delay_decay / 3) * 2):.2f} ms")

            self.output_label2.setText(
                f"{(((delay_decay / 3) * 2) - pre_delay_amt1):.2f} ms")

        elif combo3.currentText() in self.pre_delay1 and combo6.currentText() == "dotted":  # params between 1/512 and 1/32 note
            pre_delay_amt1 = self.pre_delay1[combo3.currentText()]
            zang = delay_decay / 2

            self.output_label4.setText(f"{((delay_decay + zang)):.2f} ms")  #

            self.output_label3.setText(f"{pre_delay_amt1 :.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay + zang - (pre_delay_amt1)):.2f} ms")

        elif combo3.currentText() in self.pre_delay1 and combo4.currentText() in self.pre_delay_decay:
            pre_delay_amt1 = self.pre_delay1[combo3.currentText()]

            self.output_label4.setText(f"{(pre_delayo / decay_amt):.2f} ms")

            self.output_label3.setText(f"{pre_delay_amt1 :.2f} ms")

            self.output_label2.setText(
                f"{((pre_delayo / decay_amt) - pre_delay_amt1):.2f} ms")


        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "triplet"
                and combo6.currentText() == "triplet"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            prang = (delay_decay / 3)

            self.output_label4.setText(f"{(prang * 2):.2f} ms")

            self.output_label3.setText(
                f"{(((pre_delayo / pre_delay_amt2) / 3) * 2):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay - ((((pre_delayo / pre_delay_amt2) / 3) * 2) + prang)):.2f} ms")

        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "triplet"
                and combo6.currentText() == "dotted"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            zang = delay_decay / 2

            self.output_label4.setText(f"{(delay_decay + zang):.2f} ms")

            self.output_label3.setText(
                f"{(((pre_delayo / pre_delay_amt2) / 3) * 2):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay - (((pre_delayo / pre_delay_amt2) / 3) * 2) + zang):.2f} ms")

        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "triplet"
                and combo6.currentText() == "---"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            self.output_label4.setText(f"{(pre_delayo / decay_amt):.2f} ms")

            self.output_label3.setText(
                f"{(((pre_delayo / pre_delay_amt2) / 3) * 2):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay - (((pre_delayo / pre_delay_amt2) / 3) * 2)):.2f} ms")

        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "---"
                and combo6.currentText() == "triplet"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            result = (
                float(((delay_decay / 3) * 2) - (pre_delayo / pre_delay_amt2)))

            if result is not None and result < 0:

                self.output_label4.setText(f"{((delay_decay / 3) * 2):.2f} ms")

                self.output_label3.setText(
                    f"{(pre_delayo / pre_delay_amt2):.2f} ms")

                self.output_label2.setText(
                    f"{(result):.2f} duration of the delay is shorter than the pre-delay")

            else:

                self.output_label4.setText(f"{((delay_decay / 3) * 2):.2f} ms")

                self.output_label3.setText(
                    f"{(pre_delayo / pre_delay_amt2):.2f} ms")

                self.output_label2.setText(f"{(result):.2f} ms")


        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "dotted"
                and combo6.currentText() == "triplet"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]
            sumbo = (pre_delayo / pre_delay_amt2) / 2
            prang = (delay_decay / 3)

            self.output_label4.setText(f"{((delay_decay / 3) * 2):.2f} ms")

            self.output_label3.setText(
                f"{((pre_delayo / pre_delay_amt2) + sumbo):.2f} ms")

            result = (float(
                delay_decay - ((pre_delayo / pre_delay_amt2) + sumbo) - prang))

            if result is not None and result < 0:

                self.output_label2.setText(
                    f"{(result):.2f} duration of the delay is shorter than the pre-delay")

            elif result is not None:

                self.output_label2.setText(f"{(result):.2f} ms")

        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "dotted"
                and combo6.currentText() == "dotted"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]
            sumbo = (pre_delayo / pre_delay_amt2) / 2
            zang = delay_decay / 2

            self.output_label4.setText(f"{(delay_decay + zang):.2f} ms")

            self.output_label3.setText(
                f"{((pre_delayo / pre_delay_amt2) + sumbo):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay - (((pre_delayo / pre_delay_amt2) + sumbo) - zang)):.2f} ms")

        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "dotted"
                and combo6.currentText() == "---"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]
            sumbo = (pre_delayo / pre_delay_amt2) / 2

            self.output_label4.setText(f"{(pre_delayo / decay_amt):.2f} ms")

            self.output_label3.setText(
                f"{((pre_delayo / pre_delay_amt2) + sumbo):.2f} ms")

            result = (delay_decay - ((pre_delayo / pre_delay_amt2) + sumbo))

            if result is not None and result < 0:
                self.output_label2.setText(
                    f"{(result):.2f} duration of the delay is shorter than the pre-delay")

            elif result is not None:

                self.output_label2.setText(f"{(result):.2f} ms")


        elif (
                combo3.currentText() in self.pre_delay2 and combo5.currentText() == "---"
                and combo6.currentText() == "dotted"):  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            zang = delay_decay / 2

            self.output_label4.setText(f"{(delay_decay + zang):.2f} ms")

            self.output_label3.setText(
                f"{(pre_delayo / pre_delay_amt2):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay + zang - (pre_delayo / pre_delay_amt2)):.2f} ms")

        elif combo3.currentText() in self.pre_delay2:  # params between 1/512 and 1/32 note
            pre_delay_amt2 = self.pre_delay2[combo3.currentText()]

            self.output_label4.setText(f"{(pre_delayo / decay_amt):.2f} ms")

            self.output_label3.setText(
                f"{(pre_delayo / pre_delay_amt2):.2f} ms")

            self.output_label2.setText(
                f"{(delay_decay - (pre_delayo / pre_delay_amt2)):.2f} ms")


SOS = SpeedOfSound()
SOS.show()
sys.exit(app.exec())
