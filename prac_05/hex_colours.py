color_codes = {"black": "#000000", "blue": "#0000ff", "green": "#7fff00",
               "gold": "#ffd700", "gray": "#bebebe", "pink": "#ff69b4",
               "purple": "#9370db", "yellow": "#ffff00", "white": "#ffffff",
               "red": "#ff4500"}

name_color = input("Enter color name: ")
while name_color != "":
    if name_color in color_codes:
        print("The color's code for {} is {}".format(name_color, color_codes[name_color]))
    else:
        print("Invalid color name")
    color = input("Press Enter to stop")
    break
