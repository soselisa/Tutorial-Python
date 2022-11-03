'''
#Tutorial Execption
def main():  
    x = get_int("x: ")
    print(f"x adalah {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
'''

"""
#Turorial Module/Library - random
import random

kartu = ["jack", "king", "queen"]
random.shuffle(kartu)

for k in kartu:
    print(k)
"""

