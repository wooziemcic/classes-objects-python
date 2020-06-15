class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()

if __name__ == "__main__":
  main()
