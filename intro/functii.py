def printGreeting():
    print('Buna ziua, bine ati venit!')
def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} { prenume}')
printGreeting()
printGreeting()
printGreetingByName('Sinpetrean', 'Andy')
printGreetingByName('Sinpetrean', 'Crina')
printGreetingByName('Sinpetrean', 'Ares')

def mediaNr(a, b, c):
    return (a+b+c)/3
print(mediaNr(3,3,4))