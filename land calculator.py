str=input("enter the shape")
pie=3.14
if(str=="land"):
    sqin=float(input("enter the acre of land"))
    acre=(sqin/6272639.99)
    sqfeet=(acre*43560.00)
    sqyard=(sqin/1296)
    
    print("acre is {} when square inch is {}".format(acre,sqin))
    print("square feet is {} when square inch is {} ".format(sqfeet,sqin))
    print("square yard  is {} when square inch is {}".format(sqyard,sqin))
    
elif(str=="tri"):
    h=float(input("enter the height of triangle"))
    b=float(input("enter the base of triangle"))
    a=float((0.5)*b*h)
    print("%.2f"%a)
elif(str=="circle"):
    r=float(input("enter the radius of circle"))
    a=float(pie*r**2)
    print("%.2f"%a)
elif(str=="rect"):
    l=float(input("enter the length of rectangle"))
    b=float(input("enter the breadth of rectangle"))
    a=float(b*l)
    print("%.2f"%a)
elif(str=="square"):
    s=float(input("enter the side of square"))
    a=float(s**2)
    print("%.2f"%a)
else:
    print("please enter the shape")
    
    
    
'''o/p:
enter the shapeland
enter the acre of land234
acre is 3.730486690979375e-05 when square inch is 234.0
square feet is 1.6250000025906157 when square inch is 234.0 
square yard  is 0.18055555555555555 when square inch is 234.0

=========
 
enter the shapetri
enter the height of triangle2
enter the base of triangle3
3.00
===
enter the shapecircle
enter the radius of circle2
12.56
========
enter the shaperect
enter the length of rectangle4
enter the breadth of rectangle3
12.00
>>> 
========
>>> 
enter the shapesquare
enter the side of square4
16.00'''
