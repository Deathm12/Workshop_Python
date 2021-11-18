##
## EPITECH PROJECT, 2021
## test_python
## File description:
## part_2
##

def dice_roll_res(dice_value1, dice_value2):
    if dice_value1 == dice_value2:
        return("Same value, play again")
    if dice_value1 == 1 or dice_value2 == 1:
        return("too bad you lose")
    elif dice_value1 % 2 == 0 and dice_value2 % 2 != 0:
        return("you win")
    else:
        return("nothing happen...")
print(dice_roll_res(1,3))
print(dice_roll_res(3,3))
print(dice_roll_res(6,3))
print(dice_roll_res(7,3))

def ask_me_about_string(str):
    if str[0] == 'a':
        print("that's an A")
    if len(str) < 5:
        print("error, need longer string")
    if str[0] == str[len(str)]:
        print("they are the same O_O")
    else:
        print("what a boring string...")

ask_me_about_string("rat")
ask_me_about_string("alpaga")
ask_me_about_string("Alpaga")
ask_me_about_string("KayAk")
ask_me_about_string("ce workshop me rapporte 2 xp merci")