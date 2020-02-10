print('Welcome to N00b-Age-Calculator 1.2!')
print('created by groozchique')
a = int(input('Hello! Please, enter your age: '))
while(int(a) < 1) or (int(a) > 110):
    print('Are you really human?')
    a = int(input('Please, try again. Enter your age: '))
s = int(a) * 365 * 24 * 60 * 60
m = int(a) * 365 * 24 * 60
h = int(a) * 365 * 24
w = int(a) * 12 * 4
mn = int(a) * 12
ea = str(80 - int(a))
print('Ok, here is your results:')
print('You survived in this cruel world for ' + str(s) + ' seconds' ', ' + str(m) + ' minutes' ', ' + str(h) + ' hours' ', ' + str(w) + ' weeks' ' or ' + str(mn) + ' months')
print('And you have to suffer in this world for, approximately, ' + str(ea) + ' years!')
f = input('Press any button to close the window.')
