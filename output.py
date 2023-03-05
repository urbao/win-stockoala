# get.py used to implement some useful function
# like output, show...

# print line with color (green/red/yellow/cyan/purple/white)
def color_output(color, line, newline):
    if color=="red":
        code="31m"
    elif color=="yellow":
        code="33m"
    elif color=="green":
        code="32m"
    elif color=="cyan":
        code="36m"
    elif color=="purple":
        code="35m"
    else:
        code="37m" # white
    if newline:
        print("\033[1;"+code+line+"\033[0m")
    else:
        print("\033[1;"+code+line+"\033[0m", end=" ")
    return

# test color_output acting normal
#color_output("red", "damnit bro", True)
#color_output("yellow", "damnit bro", True)
#color_output("green", "damnit bro", True)
#color_output("cyan", "damnit bro", True)
#color_output("purple", "damnit bro", True)
#color_output("nothing", "damnit bro", True)
