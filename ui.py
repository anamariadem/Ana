from service import Calculator
from domain import RationalNumber
class Console:
    def __init__(self,calc):
        self._calculator = calc

    def print_menu(self):
        print("Calculator")
        print("  + to add a rational number to the total")
        print("  t to print the total")
        print("  r to reset the calc")
        print("  ? to print the n umber of instances")
        print("  u to undo")
        print("  x to exit")

    def add(self):
        num = input("Input nominator:")
        denom = input("Input denominator:")
        self._calculator.add(RationalNumber(num,denom))

    def total(self):
        print(self._calculator._total)
    def reset(self):
        self._calculator.reset()
    def count(self):
        print(self._calculator.count)
    def undo(self):
        try:
            self._calculator.undo()
        except ValueError as e:
            print(e)

    def run(self):
        commands = {'+': self.add, 't': self.total, 'r':self.reset, '?':self.count, 'u':self.undo}
        while True:
            self.print_menu()
            command = input("Enter command: ")
            if command == 'x':
                break
            try:
                commands[command]()
            except KeyError as e:
                print(e)
