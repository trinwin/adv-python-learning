# ----------------------------------------------------------------------
# Name:       helloagain
# Purpose:    demonstrate command line arguments with the sys module
#
# Author:     Rula Khayrallah
#
# ----------------------------------------------------------------------
"""
Print a customized greeting a given number of times.

usage: helloagain.py name number
"""
import sys

def main():
    print('This is sys.argv:', sys.argv) # for demonstration purposes

    if len(sys.argv) != 3:  # Check for the right number of arguments
        print('Error: invalid number of arguments')
        print('Usage: helloagain.py name number')
    else:
        name = sys.argv[1]  # Get the name argument
        try:
            number = int(sys.argv[2])  # Get the number argument
        except ValueError:
            print('Error: invalid argument value')
            print('Usage: helloagain.py name number')

        else:   # Print the name the specified number of times
            for times in range (number):
                print(f'Hello {name}')

if __name__ == '__main__':
    main()