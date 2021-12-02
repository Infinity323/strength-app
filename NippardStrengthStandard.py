"""
Program that shows your strength levels according to Jeff Nippard's standards.
Also displays progression relative to those strength level intervals.
Written by Paul Lee.
"""

# "Enumerate" strength category names
rankings = ["Crippled", "Noob", "Beginner", "Intermediate", "Advanced", "Elite", "Freak"]
MAX_WEIGHT = 2000


class Athlete:
    def printProgress(self):
        print(33*'-')
        print(f"| Squat:\t{self.s}\t({self.s/self.bw:.2f}x)\t|")
        print(f"| Bench:\t{self.b}\t({self.b/self.bw:.2f}x)\t| ")
        print(f"| Deadlift:\t{self.d}\t({self.d/self.bw:.2f}x)\t|")
        print(f"| Total:\t{self.s+self.b+self.d}\t({(self.s+self.b+self.d)/self.bw:.2f}x)\t|")
        print(33*'-')
        # Squat
        low = self.s_div[self.s_level]
        high = self.s_div[self.s_level+1]
        percent = (self.s - low)/(high - low)
        print(f"{rankings[self.s_level]}-level squat: [{low:.1f}-{high:.1f}). {percent*100:.1f}% progression.")
        print(f"{low:.1f}",'|'+'▮'*int(percent*50)+'∙'*int(50-percent*50)+'|',f"{high:.1f}")
        # Bench
        low = self.b_div[self.b_level]
        high = self.b_div[self.b_level+1]
        percent = (self.b - low)/(high - low)
        print(f"{rankings[self.b_level]}-level bench: [{low:.1f}-{high:.1f}). {percent*100:.1f}% progression.")
        print(f"{low:.1f}",'|'+'▮'*int(percent*50)+'∙'*int(50-percent*50)+'|',f"{high:.1f}")
        # Deadlift
        low = self.d_div[self.d_level]
        high = self.d_div[self.d_level+1]
        percent = (self.d - low)/(high - low)
        print(f"{rankings[self.d_level]}-level deadlift: [{low:.1f}-{high:.1f}). {percent*100:.1f}% progression.")
        print(f"{low:.1f}",'|'+'▮'*int(percent*50)+'∙'*int(50-percent*50)+'|',f"{high:.1f}")

        return

    def __init__(self, bw, s, b, d):
        self.bw = bw
        self.s = s
        self.b = b
        self.d = d


class MaleAthlete(Athlete):
    def classify(self):
        """Crippled = 0, Noob = 1, Beginner = 2, Intermediate = 3, Advanced = 4, Elite = 5, Freak = 6"""
        if self.s < 45: self.s_level = 0
        elif self.s >= 45 and self.s < 135: self.s_level = 1
        elif self.s >= 135 and self.s < 1.25*self.bw: self.s_level = 2
        elif self.s > 1.25*self.bw and self.s < 1.75*self.bw: self.s_level = 3
        elif self.s >= 1.75*self.bw and self.s < 2.5*self.bw: self.s_level = 4
        elif self.s >= 2.5*self.bw and self.s < 3*self.bw: self.s_level = 5
        else: self.s_level = 6

        if self.b < 45: self.b_level = 0
        elif self.b >= 45 and self.b < 95: self.b_level = 1
        elif self.b >= 95 and self.b < self.bw: self.b_level = 2
        elif self.b >= 1*self.bw and self.b < 1.5*self.bw: self.b_level = 3
        elif self.b >= 1.5*self.bw and self.b < 2*self.bw: self.b_level = 4
        elif self.b >= 2*self.bw and self.b < 2.25*self.bw: self.b_level = 5
        else: self.b_level = 6

        if self.d < 45: self.d_level = 0
        elif self.d >= 45 and self.d < 135: self.d_level = 1
        elif self.d >= 135 and self.d < 1.5*self.bw: self.d_level = 2
        elif self.d > 1.5*self.bw and self.d < 2.25*self.bw: self.d_level = 3
        elif self.d >= 2.25*self.bw and self.d < 3*self.bw: self.d_level = 4
        elif self.d >= 3*self.bw and self.d < 3.5*self.bw: self.d_level = 5
        else: self.d_level = 6

        return

    def __init__(self, bw, s, b, d):
        Athlete.__init__(self, bw, s, b, d)
        self.s_div = [0, 45, 135, 1.25*self.bw, 1.75*self.bw, 2.5*self.bw, 3*self.bw, MAX_WEIGHT]
        self.b_div = [0, 45, 95, self.bw, 1.5*self.bw, 2*self.bw, 2.25*self.bw, MAX_WEIGHT]
        self.d_div = [0, 45, 135, 1.5*self.bw, 2.25*self.bw, 3*self.bw, 3.5*self.bw, MAX_WEIGHT]
        self.classify()
        self.printProgress()


class FemaleAthlete(Athlete):
    def classify(self):
        """Crippled = 0, Noob = 1, Beginner = 2, Intermediate = 3, Advanced = 4, Elite = 5, Freak = 6"""
        if self.s < 45: self.s_level = 0
        elif self.s >= 45 and self.s < 95: self.s_level = 1
        elif self.s >= 95 and self.s < self.bw: self.s_level = 2
        elif self.s >= self.bw and self.s < 1.5*self.bw: self.s_level = 3
        elif self.s >= 1.5*self.bw and self.s < 1.75*self.bw: self.s_level = 4
        elif self.s >= 1.75*self.bw and self.s < 2.25*self.bw: self.s_level = 5
        else: self.s_level = 6

        if self.b < 45: self.b_level = 1
        elif self.b >= 45 and self.b < 0.5*self.bw: self.b_level = 2
        elif self.b >= 0.5*self.bw and self.b < 0.75*self.bw: self.b_level = 3
        elif self.b >= 0.75*self.bw and self.b < 1*self.bw: self.b_level = 4
        elif self.b >= 1*self.bw and self.b < 1.25*self.bw: self.b_level = 5
        else: self.b_level = 6

        if self.d < 45: self.d_level = 0
        elif self.d >= 45 and self.d < 135: self.d_level = 1
        elif self.d >= 135 and self.d < 1.25*self.bw: self.d_level = 2
        elif self.d > 1.25*self.bw and self.d < 1.75*self.bw: self.d_level = 3
        elif self.d >= 1.75*self.bw and self.d < 2.25*self.bw: self.d_level = 4
        elif self.d >= 2.25*self.bw and self.d < 3*self.bw: self.d_level = 5
        else: self.d_level = 6

        return

    def __init__(self, bw, s, b, d):
        Athlete.__init__(self, bw, s, b, d)
        self.s_div = [0, 45, 95, self.bw, 1.5*self.bw, 1.75*self.bw, 2.25*self.bw, MAX_WEIGHT]
        self.b_div = [0, 0, 45, 0.5*self.bw, 0.75*self.bw, self.bw, 1.25*self.bw, MAX_WEIGHT]
        self.d_div = [0, 45, 135, 1.25*self.bw, 1.75*self.bw, 2.25*self.bw, 3*self.bw, MAX_WEIGHT]
        self.classify()
        self.printProgress()


def main():
    print("\nThis is a program that will classify your strength levels by Jeff Nippard's standards.")
    while True:
        # Get the inputs
        g = input("\nWhat is your gender? (m/f): ")
        while g != 'm' and g != 'f':
            g = input("What is your gender? Please enter only 'm' or 'f': ")
        while True:
            try:
                bw = int(input("What is your bodyweight? Enter number in lbs: "))
            except:
                print("Enter numbers only.")
                continue
            else: break
        while True:
            try:
                s = int(input("How much can you squat? Enter number in lbs: "))
                while s > MAX_WEIGHT: s = int(input("Stop the cap. How much can you squat? "))
            except:
                print("Enter numbers only.")
                continue
            else: break
        while True:
            try:
                b = int(input("How much can you bench? Enter number in lbs: "))
                while b > MAX_WEIGHT: b = int(input("Stop the cap. How much can you bench? "))
            except:            
                print("Enter numbers only.")
                continue
            else: break
        while True:
            try:
                d = int(input("How much can you deadlift? Enter number in lbs: "))
                while d > MAX_WEIGHT: d = int(input("Stop the cap. How much can you deadlift? "))
            except:
                print("Enter numbers only.")
                continue
            else: break

        if g == 'm': MaleAthlete(bw, s, b, d)
        elif g == 'f': FemaleAthlete(bw, s, b, d)

        # Stop the program
        stop_program = input("\nTest strength levels again? (y/n): ")
        if stop_program != 'y': break

    return


if __name__ == "__main__":
    main()