M=int(input("enter no of males"))
F=int(input("enter no of females"))
total=M+F
_M=(M/total)#percentage of male
_F=(F/total)#percentage of female
print("percentage of male is {:.0%}".format(_M))
print("percentage of female is {:.0%}".format(_F))
'''o/p:
enter no of males40
enter no of females70
percentage of male is 36%
percentage of female is 64%'''




M=int(input("enter no of males"))
F=int(input("enter no of females"))
total=M+F
_M=int((M/total)*100)#percentage of male
_F=int((F/total)*100)#percentage of female
print("percentage of male is {}".format(_M),end='%\n')
print("percentage of female is {}".format(_F),end='%')
'''o/p:
enter no of males16
enter no of females24
percentage of male is 40%
percentage of female is 60%'''



M=int(input("enter no of males"))
total=int(input("enter total students"))
F=total-M
_M=(M/total)#percentage of male
_F=(F/total)#percentage of female
print("percentage of male is {:.0%}".format(_M))
print("percentage of female is {:.0%}".format(_F))
'''o/p:
enter no of males16
enter total students40
percentage of male is 40%
percentage of female is 60%'''







