import getpass
user = str(input('Enter your username: \n'))
password = str(input('Enter your password: \n'))
lenght = len(password)
password = getpass.getpass(lenght='*')
print(password)
print(f'Parola pentru userul {user} este {maskedpasword} si are {lenght} caractere.')