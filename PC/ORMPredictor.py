"""
Program that estimates 1RM given a weight and reps performed, indiscriminate of units.
Also shows various percentages of the estimated 1RM.
Pretty much a copy of exrx.net's 1RM calculator.
Written by Paul Lee.
"""

def printEstimate(w, r):
    # Print stuff
    if (r == 1): p = 1
    elif (r == 2): p = 0.9722
    elif (r == 3): p = 0.9443
    elif (r == 4): p = 0.9166
    elif (r == 5): p = 0.8888
    elif (r == 6): p = 0.861
    elif (r == 7): p = 0.8332
    elif (r == 8): p = 0.8054
    elif (r == 9): p = 0.7776
    elif (r == 10): p = 0.75
    e = round(w/p)
    print(f"\nEstimated 1RM: {e}")
    print(24*'-')
    print(f"50%: {round(e*0.5):<10}75%: {round(e*0.75)}")
    print(f"55%: {round(e*0.55):<10}80%: {round(e*0.8)}")
    print(f"60%: {round(e*0.6):<10}85%: {round(e*0.85)}")
    print(f"65%: {round(e*0.65):<10}90%: {round(e*0.9)}")
    print(f"70%: {round(e*0.7):<10}95%: {round(e*0.95)}")

    return

def main():
    print("\nThis is a program that will estimate your one-rep max (1RM) for a lift.")
    while True:
        while True:
            try:
                w = float(input("Enter the amount of weight lifted: "))
            except:
                print("Enter a number only.")
                continue
            else: break
        while True:
            try:
                r = int(input("Enter the number of reps performed (between 1 and 10): "))
                while not (r >= 1 and r <= 10):
                    r = int(input("The number of reps performed must be between 1 and 10: "))
            except:
                print("Enter a whole number only.")
                continue
            else: break
        
        printEstimate(w, r)
        
        # Stop the program
        stop_program = input("\nEstimate 1RM again? (y/n): ")
        if stop_program != 'y': break
    return

if __name__ == "__main__":
    main()