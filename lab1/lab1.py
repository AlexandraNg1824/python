#Name: Wingyi Ng
#Lab1
#Part One
MAX = 45
name = input('Enter your name: ')
numberOfClasses = int(input("Enter the number of programming classes you've taken:"))
goal = input('Enter the goal you have for this class: ')
print()
print('*' * MAX)
print('*' + (MAX - 2) * " " + '*')
spaceBefore = (MAX - len(name) - 2) // 2
spaceAfter = MAX - 2 - len(name) - spaceBefore
print('*' + spaceBefore * " " + name.title() + spaceAfter * " " + '*')
print('*' + (MAX - 2) * " " + '*')
print('*' * MAX)
print("You've taken", numberOfClasses, "programming classes")
print("Your goal for this class is:")
print(goal.upper())

