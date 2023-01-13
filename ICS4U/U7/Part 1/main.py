# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date -  

def user_choice():
    print("\n(1)Find the students with more than 6 quiz scores \n(2) Calculate the average grade for each student \n(3) Calculate the minimum and maximum score for each student\n(4) End the program")
    try:
        choice = int(input("What choice do you want? (Enter a value between 1 to 4): "))
        if choice != 1 and choice != 2 and choice !=3 and choice !=4:
            print("Enter a proper value1")
        return choice
    except:
        print("Enter a proper value2")
def num_of_quiz(file):
    for line in file.readlines():
                count = 0
                values = []
                values = line.split()
                name = values[0]
                for i in range (len(values[1:])):
                    count +=1
                if count > 6:
                    print(f"Student {name} has more than 6 quiz scores at {count} scores")

def quiz_average(file):
    for line in file.readlines():
        total = 0
        values = []
        values = line.split()
        name = values[0]
        for i in range (1,len(values)):
            total += int(values[i])
        average = total/i
        print(f"The average of {name}'s quiz scores is {average:.2f}")


def min_and_max(file): 
    for line in file.readlines():
        values = []
        values = line.split()
        name = values[0]
        minimum = min(values[1:], key=int)
        maximum= max(values[1:], key=int)
        print(f"{name}'s minimum quiz score was {minimum} and maximum score was {maximum}")
       

def main():
    while True:
        try:
            file = open(r'U7/Part 1/studentdata.txt','r')
            choice = user_choice()
            if choice == 1:
                num_of_quiz(file)
            elif choice == 2:
                quiz_average(file)
            elif choice == 3:
                min_and_max(file)
            elif choice == 4:
                print("Thank you for using the program")
                break
            
        finally:
            file.close()

if __name__ == "__main__":
    main()

