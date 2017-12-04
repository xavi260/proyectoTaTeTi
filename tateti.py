#!/usr/bin/env python3

import time

print ("Welcome to Tateti")

time.sleep (2)

print("")
print("------|------|------")
print("      |      |      ")
print("  7   |   8  |   9  ")
print("      |      |      ")
print("------|------|------")
print("      |      |      ")
print("  4   |   5  |   6  ")
print("      |      |      ")
print("------|------|------")
print("      |      |      ")
print("  1   |   2  |   3  ")
print("      |      |      ")
print("------|------|------")
print("")

time.sleep (2)

player = input("Elija su pieza X/O :")

if player == "x":
    print("Buena eleccion")
elif player == "o":
    print("Buena Eleccion")
elif player == "":
    print("Error")
