import logging
logging.basicConfig(level=logging.INFO)

o =int(input('Podaj dzialanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
f= float(input('Podaj pierwszą liczbę: '))
s=float(input('Podaj drugą liczbę: '))
s1=''
s2=''
m=0
if o==1:
    s1='Dodaję '
    s2= ' do '
    m=f+s
elif o==2:
    s1='Odejmuję '
    s2= ' od '
    m=f-s
elif o==3:
    s1='Mnożę '
    s2= ' przez '
    m = f * s
elif o==4:
    s1 = 'Dzielę '
    s2= ' przez '
    m = f / s
logging.info(s1 + str(f) + s2 + str(s))

print('Wynik to: ' + str(m))