import os

def display_high_scorers():
    print("Students who scored more than 75 marks:")
    with open("marks.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            if int(marks) > 75:
                print(name,marks)

def main():
    
    fobj = display_high_scorers()
    print(fobj)

if __name__ == "__main__":
    main()
