# Name - Ryan Alumkal
# Grade - 12
# Description - Scrapes data from a list of student data. Asks the user what information they want and prints the information
# Date -  1/16/2023

#functions
def user_choice(): #asks user for what information they want 
    print("\n(1) Find the students with more than 6 quiz scores \n(2) Calculate the average grade for each student \n(3) Calculate the minimum and maximum score for each student\n(4) End the program")
    while True:
        try:
            choice = int(input("What choice do you want? (Enter a value between 1 to 4): ")) #asks user for a number depending on the choice 
            if choice == 1 or choice == 2 or choice ==3 or choice ==4: #if input is invalid 
                break
            else:
                print("\nEnter a proper value")
        except: #if user input is invalid 
            print("\nEnter a proper value")
    return choice #returns choice 

def num_of_quiz(data): #finds students with more than 6 quiz scores 
    for line in data: #reads every line in "studentdata.txt"
        count = 0 #counter for the # of quizes 
        values = line.split() #gets the different values, creates a list
        name = values[0] #gets name of student
        for i in range (1,len(values)): #for every quiz entry
            count +=1 #increases count per entry 
        if count > 6: #if quiz count is greater than 6
            print(f"\n{name} has more than 6 quiz scores at {count} scores") #prints student names with more than 6 quizzes along with # of quizzes 

def quiz_average(data):# finds average grade for each student 
    for line in data: #reads every line in "studentdata.txt"
        total = 0
        values = line.split() #gets the different values, creates a list
        name = values[0] #gets name of student
        for i in range (1,len(values)): #for every quiz entry 
            total += int(values[i]) #adds to total sum of quiz entries 
        average = total/i #finds average 
        print(f"\nThe average of {name}'s quiz scores is {average:.2f}") #prints name and average of each student 


def min_and_max(data): 
    for line in data: #reads every line in "studentdata.txt"
        values = line.split() #gets the different values, creates a list
        name = values[0] #gets name of student
        minimum = min(values[1:], key=int) #finds minimum integer in each entry after the name
        maximum= max(values[1:], key=int) #finds maximum integer in each entry after the name
        print(f"\n{name}'s minimum quiz score was {minimum} and maximum score was {maximum}") #prints the name, min, and max scores 
       
#main function
def main():
    try:
        file = open(r'ICS4U/U7/Part 1/studentdata.txt','r') #opens file "studentdata.txt"; includes path
        data = file.readlines() #gets data from file
    finally:
        file.close() #closes file 

    while True: #while user wants to run program
        choice = user_choice() #gets user choice 
        if choice == 1: #prints students with more than 6 quiz scores
            print("\nStudents with more than 6 quiz scores:")
            num_of_quiz(data)
        elif choice == 2: #prints average scores for each student
            print("\nAverage scores for each student:")
            quiz_average(data)
        elif choice == 3: #prints minimum and Maximum score for each student
            print("\nMinimum and Maximum score for each student:")
            min_and_max(data)
        elif choice == 4: #if user wants to end program
            print("\nThank you for using the program")
            break
    

#main program 
if __name__ == "__main__": 
    main()
