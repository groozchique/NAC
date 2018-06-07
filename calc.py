print('Welcome to Noob-Age-Calculator 1.1!')
name  = input('Enter your name: ')
age = int(input("Enter your age: '))
if int(age) < 1 or int(age) > 100:
    print('You are not human!')
    quit()
seconds = int(age) * 365 * 24 * 60 * 60
minutes = int(age) * 365 * 24 * 60
hours = int(age) * 365 * 24
weeks  = int(age) * 12 * 4
months = int(age) * 12
print('Hi, ' + str(name) + ', there is your results:')
print('Your age in seconds: ' + str(seconds) + " seconds')
print('Your age in minutes: ' + str(minutes) + " minutes')
print('Your age in hours: ' + str(hours) + " hours')
print('Your age in weeks: ' + str(weeks) + " weeks')
print('Your age in months: '+ str(months) + ' months')
print('And you have to suffer in this world ' + str(100 - int(age)) + ' years!')
f = input('Press any button to close the window.')
