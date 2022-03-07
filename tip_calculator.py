#Tip calculator

#Function to get the cost of the bill before taxes from the user
def get_cost():
    is_float=False
    #to ensure an invalid value can not be entered
    while is_float==False:
        cost_food=input('What is the cost of food and drinks?')
        try:
            float_cost=float(cost_food)
            is_float=True
        except ValueError:
            print('That is not a valid cost')
    return cost_food


#function to get the number of people in the party
def get_num_people():
    is_int=False
    #to ensure an invalid value can not be entered
    while is_int==False:
        num_people=input('How many people are in your party?')
        try:
            int_people=int(num_people)
            is_int=True
        except ValueError:
            print('That is not a valid number of people')
    return num_people


#function to ask the user what percent tip they would like to leave
def get_tip():
    is_float=False
    #to ensure an invalid number can not be entered
    while is_float==False:
        tip=input('what percent tip would you like to leave?')
        try:
            float_tip=float(tip)
            is_float=True
        except ValueError:
            print('That is not a valid tip')
    return tip

#assigning the cost of food, sales tax, and number of people to variables that cna be passed into a function
cost_food=float(get_cost())
sales_tax=.053
num_people=int(get_num_people())

# asking the user how much of a tip they would like to leave and calculating the total for each person
# tip is in the function so it is a value that can be changed later
def calculate_tip():
    tip=float(get_tip())
    total_cost=cost_food+(sales_tax*cost_food)+(cost_food*(tip/100))
    share=round(total_cost/num_people, 2)
    print(f"Each persons share of the bill is {share}")

#running the calculation for the first time
calculate_tip()

#asking the user if they would like to calculate a new tip value
new_tip=input('Would you like to calculate a different tip? (yes/no)')

#running the calculate function with a new tip value input until the user anwsers no 
while new_tip=='yes':
    calculate_tip()
    new_tip=input('Would you like to calculate a different tip?')        
else:
    print('Have a nice night!')
    #prints once the user anwsers no to new_tip and ends the loop
         
  
 