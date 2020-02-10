print('Welcome to N00b-Age-Calculator 1.1!')
print('created by groozchique')
age = int(input('Hello! Please, enter your age: '))
while(int(age) < 1) or (int(age) > 110):
    print('Are you really human?')
    age = int(input('Please, try again. Enter your age: '))
seconds = int(age) * 365 * 24 * 60 * 60
minutes = int(age) * 365 * 24 * 60
hours = int(age) * 365 * 24
weeks = int(age) * 12 * 4
months = int(age) * 12
ea = str(80 - int(age))
print('Ok, here is your results:')
print('You survived in this cruel world for ' + str(seconds) + ' seconds' ', ' + str(minutes) + ' minutes' ', ' + str(hours) + ' hours' ', ' + str(weeks) + ' weeks' ' or ' + str(months) + ' months')
print('And you have to suffer in this world for, approximately, ' + str(ea) + ' years!')
f = input('Press any button to close the window.')
