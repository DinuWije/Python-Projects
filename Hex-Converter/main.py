""" 
This program can be used to convert between HEX and RGB color codes, and vice-versa
Author: Dinu Wijetunga 
""" 
invalid_msg = "Sorry, that value is invalid. Please try again. \n"
def rgb_hex():
  red = int(raw_input("Enter the value for Red: "))
  if red > 255 or red < 0:
    print invalid_msg
    return
  green = int(raw_input("Enter the value for Green: "))
  if green > 255 or green < 0:
    print invalid_msg
    return
  blue = int(raw_input("Enter the value for Blue: "))
  if blue > 255 or blue < 0:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print "Hex Code: %s \n" % (hex(val)[2::]).upper() 

def hex_rgb():
  hex_val = raw_input("Enter a hexadecimal value: ")
  if len(hex_val) != 6:
    print invalid_msg
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "R: %s \nG: %s \nB: %s \n" % (red,green,blue)

def convert():
  while(True):
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ") 
    if option == '1':
      print "RGB to Hex"
      rgb_hex()
    elif option == "2":
      print "Hex to RGB"
      hex_rgb()
    elif option == "x" or option == "X":
      print "Exiting..."
      break
    else:
      print "Error. Please try again. \n"

convert()

    