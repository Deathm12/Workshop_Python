##
## EPITECH PROJECT, 2021
## test_python
## File description:
## part_1
##

print("Success")

pie_crust = "empty"
isOvenOn = False
fruit = "apples"
quantity = 5

print(f'''You have {quantity} {fruit} and the pie crust is {pie_crust},
is the oven on ? {isOvenOn}''')

def print_hello_please() :
    print("Hello")

print_hello_please()

def print_hello_with_my_name_please(myName):
    print("Hello", myName)

print_hello_with_my_name_please("Byleth")

def calc_my_age_in_two_years(myCurrentAge):
    print(f"You are {myCurrentAge} years old")
    my_age_in_two_years = myCurrentAge + 2
    return my_age_in_two_years

my_age_in_two_years = calc_my_age_in_two_years(33)

print(f"In two years, i'll be {my_age_in_two_years} years old")


fruit = "apples"
quantity = 5
pie_crust = "empty"
isOvenOn = False

def prepMyFruit(quantity, fruit, pie_crust):
    print(f"{quantity} {fruit}")
    pie_crust = f"filled with delicious {fruit}"
    return pie_crust

pie_crust = prepMyFruit(quantity, fruit, pie_crust)
print("my pie is", pie_crust)

fruit = "banana"
quantity = 4
pie_crust = " empty "
is_oven_on = False

def trun_no_oven(is_oven_on):
    is_oven_on = True
    return is_oven_on

pie_crust = prepMyFruit(quantity, fruit, pie_crust)
is_oven_on = trun_no_oven(is_oven_on)
print("my pie is", pie_crust)
print("Is the oven turned on ?", is_oven_on)

def cookDaPie(pie_crust):
    print(f"Your pie {pie_crust} is cooked, Bon appetit")

cookDaPie(pie_crust)
