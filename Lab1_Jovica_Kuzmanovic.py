#Jovica Kuzmanovic

#ACIT 1515



#Part 1
current_year = 2024
responded = False

#Part 3
birth_year = input("Please enter your Birth Year: ")
if len(birth_year) > 0 and birth_year.isdigit():
    print(f'You are {current_year - int(birth_year)} years old!')
    responded = True

#Part 4
fave = input("Please enter your Favourite number: ")
if fave and fave.isdigit():
    fave = int(fave)
    print(f'Your favourite number squared is: {fave * fave}')
    print(f'Your favorutie number divided by 2 is: {fave / 2}')
    if fave % 2 == 0:
        print("Your favourite number is even")
    else:
        print("Your favourite number is odd!")


#Part 5
name = input("Please eneter your name:")
if name:
    print(f'Your name is {len(name)} letters long')
    print(" ")

#Part 6
letter_from_name = input("Please enter a letter form your name: ")

if letter_from_name and letter_from_name.isalpha() and letter_from_name in name:
    print("Your name contains that letter!")

else:
    print("Your name does not contain that letter.")


print('Thanks for repsonding!')


