"""
"Main menu" script for this strength program.
Written by Paul Lee.
"""

import NippardStrengthStandard
import WeightBreakdown
import ORMPredictor

options = ['t', 'w', 'p']

def main():
    print("\nWelcome to the strength application main menu.")
    while True:
        # Decision tree
        print("'t'\tStrength Level Tester")
        print("'w'\tWeight Converter")
        print("'p'\tOne-Rep Max (1RM) Predictor")
        choice = input("Please enter an option: ")
        while choice not in options: choice = input("Please enter a valid option: ")
        if choice == 't': NippardStrengthStandard.main()
        elif choice == 'w': WeightBreakdown.main()
        elif choice == 'p': ORMPredictor.main()

        # Stop the program again
        stop_program = input("\nRun another application? (y/n): ")
        if stop_program != 'y': break
    return

if __name__ == "__main__":
    main()