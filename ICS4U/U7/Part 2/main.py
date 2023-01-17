# Name - Ryan Alumkal
# Grade - 12
# Description - Scrapes QB information from a pre-determined data set. Asks user for what information they need and prints them out
# Date -  1/16/2023

#functions 
def user_choice():#asks user for what information they want 
    print("\n(1) Print first name, last name, and passer rate \n(2) Print last name, first name \n(3) Print the name of the highest rated plater \n(4) Print average number of yards per completed pass \n(5) Print out the # of players with over 300 passes \n(6) End the program")
    while True:
        try:
            choice = int(input("What choice do you want? (Enter a value between 1 to 6): "))#asks user for a number depending on the choice 
            if choice == 1 or choice == 2 or choice ==3 or choice ==4 or choice ==5 or choice==6:#if input is invalid 
                break
            else:
                print("\nEnter a proper value")
        except: #if user input is invalid 
            print("\nEnter a proper value")
    return choice #returns choice 

def qb_information(data): #finds qb information: first name, last name, and passer rate
    for line in data: #reads every line in "qbdata.txt"
        values = line.split() #gets the different values, creates a list
        first_name = values[0] #gets first name
        last_name = values[1] #gets last name
        rating = values[10] #gets rating 
        print(f"\n{first_name} {last_name} had a rating of {rating}") #prints first name, last name, and passer rate

def qb_name(data): #lists qb last name and first name
    for line in data: #reads every line in "qbdata.txt"
        values = line.split() #gets the different values, creates a list
        first_name = values[0] #gets first name
        last_name = values[1] #gets last name
        print(f"\n{last_name}, {first_name}") #prints last name and first name 

def highest_rated_player(data): #finds highest rated player 
    highest_rated_player = [] #variable to hold player info
    highest_rating = 0.0 #highest rating variable 
    for line in data: #reads every line in "qbdata.txt"
        values = line.split() #gets the different values, creates a list
        first_name = values[0] #gets first name
        last_name = values[1] #gets last name
        rating = values[10] #gets rating 
        if float(rating) > highest_rating: #if specific player rating is higher than previous players' rating
            highest_rated_player = [first_name,last_name,rating] #holds new highest rating player info
            highest_rating = float(rating) #hold new highest rating
    print(f"\nThe highest rated player is {highest_rated_player[0]} {highest_rated_player[1]} with a rating of {highest_rated_player[2]}") #prints result

def average_num_of_yards(data): #finds average number of yards completed per pass
    for line in data: #reads every line in "qbdata.txt"
        values = [] #variable for values
        values = line.split() #gets the different values, creates a list
        first_name = values[0] #gets first name
        last_name = values[1] #gets last name
        average = round((int(values[6])/int(values[4])),2) #finds average: yards/completions
        print(f"\n{last_name}, {first_name} has an average number of yards per completed pass of {average}") #prints result

def over_three_hundred_passes(data): #finds # of players with over 300 completed passes 
	count = 0 #counter 
	name = ''
	for line in data: #reads every line in "qbdata.txt"
		values = [] #variable for values
		values = line.split() #gets the different values, creates a list
		if int(values[4]) > 300: #if player completed passes is over 300
			count +=1
			name += str(values[:2]) + ", "
	print(f"The number of players that have completed over 300 passes is {count}. These players are: {name}") #prints results 

#main function
def main():
    try:
        file = open(r'qbdata.txt','r') #opens file "studentdata.txt"; includes path
        data = file.readlines() #gets data from file
    finally:
        file.close() #closes file 

    while True: #while user wants to run program
        choice = user_choice() #gets user choice 
        if choice == 1: #prints first name, last name, and passer rate
            print("\nFirst name, last name, and passer rate: ")
            qb_information(data)
        if choice == 2: #prints last name, first name
            print("\nLast name, first name:")
            qb_name(data)
        if choice == 3: #prints QB with highest rating
            print("\nQB with highest rating:")
            highest_rated_player(data)
        if choice == 4: #prints average number of yards per completed pass
            print("\nAverage number of yards per completed pass:")
            average_num_of_yards(data)
        if choice == 5: #prints number of players that have completed over 300 passes
            print("\nNumber of players that have completed over 300 passes:")
            over_three_hundred_passes(data)
        if choice == 6: #ends program
            print("\nThank you for using the program")
            break

#main program
if __name__ == "__main__":
    main()