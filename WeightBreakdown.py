"""
Program that displays barbell plate weight breakdown given total weight.
Can convert from pounds to kilograms or vice versa.
Written by Paul Lee.
"""

def pounds(w):
    one_side = (w - 45)/2
    red = 0
    one_side -= red*55
    blue = int(one_side / 45) if one_side >= 45 else 0
    one_side -= blue*45
    yellow = 0
    one_side -= yellow*35
    green = int(one_side / 25) if one_side >= 25 else 0
    one_side -= green*25
    ten = int(one_side / 10) if one_side >= 10 else 0
    one_side -= ten*10
    five = int(one_side / 5) if one_side >= 5 else 0
    one_side -= five*5
    two = int(one_side / 2.5) if one_side >= 2.5 else 0
    one_side -= two*2.5
    one = int(one_side) if one_side >= 1 else 0
    one_side -= one*1
    half = int(one_side / 0.50)
    print(f"Norm\t{red}\t{blue}\t{yellow}\t{green}\t{ten}\t{five}\t{two}\t{one}\t{half}")

    return

def compPounds(w):
    one_side = (w - 45)/2
    red = int(one_side / 55) if one_side >= 55 else 0
    one_side -= red*55
    blue = int(one_side / 45) if one_side >= 45 else 0
    one_side -= blue*45
    yellow = int(one_side / 35) if one_side >= 35 else 0
    one_side -= yellow*35
    green = int(one_side / 25) if one_side >= 25 else 0
    one_side -= green*25
    ten = int(one_side / 10) if one_side >= 10 else 0
    one_side -= ten*10
    five = int(one_side / 5) if one_side >= 5 else 0
    one_side -= five*5
    two = int(one_side / 2.5) if one_side >= 2.5 else 0
    one_side -= two*2.5
    one = int(one_side) if one_side >= 1 else 0
    one_side -= one*1
    half = int(one_side / 0.50)
    print(f"Comp\t{red}\t{blue}\t{yellow}\t{green}\t{ten}\t{five}\t{two}\t{one}\t{half}")

    return

def kilos(w):
    one_side = (w - 20)/2
    red = 0
    one_side -= red*25
    blue = int(one_side / 20) if one_side >= 20 else 0
    one_side -= blue*20
    yellow = 0
    one_side -= yellow*15
    green = int(one_side / 10) if one_side >= 10 else 0
    one_side -= green*10
    ten = int(one_side / 5) if one_side >= 5 else 0
    one_side -= ten*5
    five = int(one_side / 2.5) if one_side >= 2.5 else 0
    one_side -= five*2.5
    two = int(one_side / 1) if one_side >= 1 else 0
    one_side -= two*1
    one = int(one_side / 0.5) if one_side >= 0.5 else 0
    one_side -= one*0.5
    half = int(one_side / 0.25)
    print(f"Norm\t{red}\t{blue}\t{yellow}\t{green}\t{ten}\t{five}\t{two}\t{one}\t{half}")

    return

def compKilos(w):
    one_side = (w - 20)/2
    red = int(one_side / 25) if one_side >= 25 else 0
    one_side -= red*25
    blue = int(one_side / 20) if one_side >= 20 else 0
    one_side -= blue*20
    yellow = int(one_side / 15) if one_side >= 15 else 0
    one_side -= yellow*15
    green = int(one_side / 10) if one_side >= 10 else 0
    one_side -= green*10
    ten = int(one_side / 5) if one_side >= 5 else 0
    one_side -= ten*5
    five = int(one_side / 2.5) if one_side >= 2.5 else 0
    one_side -= five*2.5
    two = int(one_side / 1) if one_side >= 1 else 0
    one_side -= two*1
    one = int(one_side / 0.5) if one_side >= 0.5 else 0
    one_side -= one*0.5
    half = int(one_side / 0.25)
    print(f"Comp\t{red}\t{blue}\t{yellow}\t{green}\t{ten}\t{five}\t{two}\t{one}\t{half}")

    return

def main():
    print("\nThis program breaks down a given barbell weight into individual plates.")
    while True:
        # Get the inputs
        while True:
            try:
                w, u = input("Enter weight, followed by unit of measurement (e.g. 135 lb, 61 kg): ").split(" ")
                while u != "lb" and u != "kg":
                    w, u = input("Invalid unit of measurement. Please re-enter weight with lb or kg: ").split(" ")
                w = float(w)
                while (u == "lb" and w < 45) or (u == "kg" and w < 20):
                    w, u = input("Weight must be greater than 45 lb or 20 kg. Please re-enter weight with lb or kg: ").split(" ")
            except:
                print("Enter numbers only for the weight")
                continue
            else: break

        print()
        if u == "lb":
            print(25*'-'+f"Rounding {w} lb to {round(w)} lb"+25*'-')
            w = round(w)
            print("lb\t55 (R)\t45 (B)\t35 (Y)\t25 (G)\t10\t5\t2.5\t1\t0.5")
            pounds(w)
            compPounds(w)
            print(25*'-'+f"Converting {w} lb to {round(w/2.205*2)/2} kg"+25*'-')
            print("kg\t25 (R)\t20 (B)\t15 (Y)\t10 (G)\t5\t2.5\t1\t0.5\t0.25")
            kilos(round(w/2.205*2)/2)
            compKilos(round(w/2.205*2)/2)
        elif u == "kg":
            print(25*'-'+f"Rounding {w} kg to {round(w*2)/2} kg"+25*'-')
            w = round(w*2)/2
            print("kg\t25 (R)\t20 (B)\t15 (Y)\t10 (G)\t5\t2.5\t1\t0.5\t0.25")
            kilos(w)
            compKilos(w)
            print(25*'-'+f"Converting {w} kg to {round(w*2.205)} lb"+25*'-')
            print("lb\t55 (R)\t45 (B)\t35 (Y)\t25 (G)\t10\t5\t2.5\t1\t0.5")
            pounds(round(w*2.205))
            compPounds(round(w*2.205))


        # Stop the program
        stop_program = input("\nConvert another weight? (y/n): ")
        if stop_program != 'y': break

    return

if __name__ == "__main__":
    main()