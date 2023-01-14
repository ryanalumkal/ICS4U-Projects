# Name - Ryan Alumkal
# Grade - 12
# Description - Scrapes QB information from a pre-determined data set. Asks user for what information they need and prints them out
# Date -  

def user_choice():
    print("\n(1) Print first name, last name, and passer rate \n(2) Print last name, first name \n(3) Print the name of the highest rated plater \n(4) Print average number of yards per completed pass \n(5) Print out the # of players with over 300 passes \n(6) End the program")
    try:
        choice = int(input("What choice do you want? (Enter a value between 1 to 6): "))
        if choice != 1 and choice != 2 and choice !=3 and choice !=4 and choice !=5 and choice!=6:
            print("Enter a proper value")
        return choice
    except:
        print("Enter a proper value")

def qb_information(file):
    for line in file.readlines():
            values = []
            values = line.split()
            first_name = values[0]
            last_name = values[1]
            rating = values[10]
            print(f"\n{first_name} {last_name} had a rating of {rating}")

def qb_name(file):
    for line in file.readlines():
            values = []
            values = line.split()
            first_name = values[0]
            last_name = values[1]
            print(f"\n{last_name}, {first_name}")

def highest_rated_player(file):
    highest_rated_player = []
    highest_rating = 0.0
    for line in file.readlines():
            values = []
            values = line.split()
            first_name = values[0]
            last_name = values[1]
            rating = values[10]
            if float(rating) > highest_rating:
                highest_rated_player = [first_name,last_name,rating]
                highest_rating = float(rating)
            else:
                continue
    print(f"\nThe highest rated player is {highest_rated_player[0]} {highest_rated_player[1]} with a rating of {highest_rated_player[2]}")

def average_num_of_yards(file):
    for line in file.readlines():
            values = []
            values = line.split()
            first_name = values[0]
            last_name = values[1]
            average = round((int(values[6])/int(values[4])),2)
            print(f"\n{first_name} {last_name} has an average number of yards per completed pass of {average}")

def over_three_hundred_passes(file):
    count = 0
    for line in file.readlines():
            values = []
            values = line.split()
            if values[4]:
                count +=1
    print(f"The number of players that have completed over 300 passes is {count}")

def main():
    while True:
        file = open(r'ICS4U/U7/Part 2/qbdata.txt','r')
        try:
            choice = user_choice()
            if choice == 1:
                print("\nFirst name, last name, and passer rate: ")
                qb_information(file)
            if choice == 2:
                print("\nLast name, first name:")
                qb_name(file)
            if choice == 3:
                print("\nQB with highest rating:")
                highest_rated_player(file)
            if choice == 4:
                print("\nAverage number of yards per completed pass:")
                average_num_of_yards(file)
            if choice == 5:
                print("\nNumber of players that have completed over 300 passes:")
                over_three_hundred_passes(file)
            if choice == 6:
                print("Thank you for using the program")
                break
        finally:
            file.close()
    
if __name__ == "__main__":
    main()