from math import atan2

PI = 4 * atan2(1, 1)

def triangle(*args):
    return 0.5 * args[0] * args[1]

def rectangle(*args):
    return args[0] * args[1]

def square(*args):
    return args[0] ** 2

def circle(*args):
    return PI * (args[0] ** 2)

def main():
  switcher = {
      't':"triangle",
      'r':"rectangle",
      's':"square",
      'c':"circle"
  }
    # switcher keys to list 
  strings = [*switcher]

  string = input(" Input string : ")
  if not string in strings:
      print(" Your input must be one of these strings : {}".format(', '.join(strings)))
      exit(1)

  func = switcher[string]
  area = 0
  if string in strings[slice(2)]:

      n1 = int(input(" Input n1 : "))
      n2 = int(input(" Input n2 : "))
        #call func by it's name in a string
      area = globals()[func](n1,n2)

  elif string in strings[slice(2,4)]:
      n1 = int(input(" Input n1 : "))
      area = globals()[func](n1)

  print(" Your {} area is {} ".format(func,area))
  
if __name__== "__main__":
  main()