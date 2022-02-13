
def new_line():
    print(".")

def three_lines(): #prints three lines
    new_line()
    new_line()
    new_line()

def nine_lines(): #prints nine lines
    three_lines()
    three_lines()
    three_lines()

print("Printing nine lines")
print(nine_lines())

print("Printing 25 lines")

def clear_screen(): #prints 16 lines, to be added later to 9 lines and yield 25
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print(nine_lines(), clear_screen())



