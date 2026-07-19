h=float(input('height of cylinder is:'))
r=float(input('radius of cylinder is:'))
operator=input('What you would find?\n(lateral surface area ,total surface area or volume ) \n{note :-only write first word!} \n : ')

from math import pi

lateral =2*pi*r*h
total= 2*pi*r**2+2*pi*r*h
volume=pi*r**2*h

if operator== 'lateral':
    print('lateral surface area of given cylinder is:-',lateral)
if operator=='total':
    print('total surface area of given cylinder is :-',total)
if operator=='volume':
    print('volume of given cylinder is:-',volume)


