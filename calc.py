from os import replace
from posixpath import split
import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from numpy import sqrt, square


# Set app size
Window.size = (430, 580)
Builder.load_file("calc.kv")


class Calculator(Widget):
    # clearing the screen
    def clear(self):
        self.ids.inputed_number.text = '0'
        self.ids.reflection.text = ''
        self.ids.inputed_number.font_size = 50

    # Pressing number functionality
    def button_pressed(self, button):
        initial_input = self.ids.inputed_number.text
        if initial_input == '0':
            self.ids.inputed_number.text = ''
            self.ids.inputed_number.text = f'{button}'
        else:
            self.ids.inputed_number.text = f'{initial_input}{button}'

        # this function deletes the mimic/formular screen
    def delete_last_number(self):
        if self.ids.reflection.text != '':
            self.ids.reflection.text = ''
        else:
            initial_input = self.ids.inputed_number.text
            initial_input = initial_input[:-1]
            self.ids.inputed_number.text = initial_input

        # for inputing the operation signs
    def operation_signs(self, sign):
        initial_input = self.ids.inputed_number.text
        end_of_input = initial_input[-1]
        new = sign
        if end_of_input == '+' or end_of_input == '÷' or end_of_input == '-' or end_of_input == 'x':
            pass
        else:
            final_output = f"{initial_input}{sign}"
            self.ids.inputed_number.text = final_output
            self.ids.reflection.text = self.ids.inputed_number.text

        # working with decimals

    def decimal_point(self):
        initial_input = self.ids.inputed_number.text
        number_input_addtion = initial_input.split("+")
        number_input_subtraction = initial_input.split("-")
        number_input_multiplication = initial_input.split("x")
        number_input_division = initial_input.split("÷")

        if "+" in initial_input and "." not in number_input_addtion[-1]:
            initial_input = f"{initial_input}."
            self.ids.inputed_number.text = initial_input
        if "-" in initial_input and "." not in number_input_subtraction[-1]:
            initial_input = f"{initial_input}."
            self.ids.inputed_number.text = initial_input
        if "x" in initial_input and "." not in number_input_multiplication[-1]:
            initial_input = f"{initial_input}."
            self.ids.inputed_number.text = initial_input
        if "÷" in initial_input and "." not in number_input_division[-1]:
            initial_input = f"{initial_input}."
            self.ids.inputed_number.text = initial_input

        elif "." in initial_input:
            pass
        else:
            initial_input = f"{initial_input}."
            self.ids.inputed_number.text = initial_input

        # add or removes a plus sign
    def plus_or_minus(self):
        initial_input = self.ids.inputed_number.text
        if "-" in initial_input:
            self.ids.inputed_number.text = f'{initial_input.replace("-", "")}'
        elif self.ids.inputed_number.text == "Cannot divide by zero":
            self.ids.inputed_number.text = "0"
        else:
            self.ids.inputed_number.text = f'-{initial_input}'

        # conerts the input into a percentage
    def percentage_sign(self):
        try:
            initial_input = self.ids.inputed_number.text
            answer = float(initial_input) / 100
            self.ids.inputed_number.text = str(answer)
        except ValueError:
            pass

        # one divides te input
    def one_divides_x(self):
        try:
            initial_input = self.ids.inputed_number.text
            answer = 1/float(initial_input)
            self.ids.inputed_number.text = str(answer)
            self.ids.reflection.text = f"1/({initial_input})"
        except ValueError:
            self.ids.inputed_number.text = "0"
        except ZeroDivisionError:
            self.ids.inputed_number.text = "Cannot divide by zero"

            # squares the input
    def square_of_x(self):
        initial_input = self.ids.inputed_number.text
        try:
            if float(initial_input):
                answer = float(initial_input)*float(initial_input)
                self.ids.inputed_number.text = str(answer)
                self.ids.reflection.text = f"sqr({initial_input})"

        except ValueError:
            self.ids.inputed_number.text = "0"
        # square roots the number

    def square_root_of_x(self):
        try:
            initial_input = self.ids.inputed_number.text
            initial_input = float(initial_input)
            answer = sqrt(initial_input)
            self.ids.inputed_number.text = str(answer)
            self.ids.reflection.text = f"√({initial_input})"

        except ValueError:
            self.ids.inputed_number.text = "0"

        # solves the  4 basic matematical operations [+,-, x, /]
    def equals_to(self):
        try:
            initial_input = self.ids.inputed_number.text
            if "x" in initial_input:
                initial_input = initial_input.replace("x", '*')
            elif "÷" in initial_input:
                initial_input = initial_input.replace("÷", '/')

            answer = eval(initial_input)
            self.ids.inputed_number.text = str(answer)
            self.ids.reflection.text = f"{initial_input}="

        except ZeroDivisionError:
            self.ids.inputed_number.font_size = 30
            self.ids.inputed_number.text = "Cannot divide by zero"
        except ValueError:
            self.ids.inputed_number.text = "0"
        except SyntaxError:
            self.ids.inputed_number.text = "0"


class PrettyCalculatorApp(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        return Calculator()


if __name__ == '__main__':
    PrettyCalculatorApp().run()
