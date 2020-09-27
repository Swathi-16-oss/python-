import string
a=list(string.ascii_uppercase)
print(a)
#o/p ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(string.ascii_uppercase)
#o/p ABCDEFGHIJKLMNOPQRSTUVWXYZ

for i in range(len(a)):
    print("")
    for j in range(0,i+1):
        print(a[j],end=" ")
'''o/p
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
A B C D E F G 
A B C D E F G H 
A B C D E F G H I 
A B C D E F G H I J 
A B C D E F G H I J K 
A B C D E F G H I J K L 
A B C D E F G H I J K L M 
A B C D E F G H I J K L M N 
A B C D E F G H I J K L M N O 
A B C D E F G H I J K L M N O P 
A B C D E F G H I J K L M N O P Q 
A B C D E F G H I J K L M N O P Q R 
A B C D E F G H I J K L M N O P Q R S 
A B C D E F G H I J K L M N O P Q R S T 
A B C D E F G H I J K L M N O P Q R S T U 
A B C D E F G H I J K L M N O P Q R S T U V 
A B C D E F G H I J K L M N O P Q R S T U V W 
A B C D E F G H I J K L M N O P Q R S T U V W X 
A B C D E F G H I J K L M N O P Q R S T U V W X Y 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '''

for i in range(len(a)):
    print("")
    for j in range(0,i+1):
        j=i
        print(a[j],end=" ")
'''
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F 
G G G G G G G 
H H H H H H H H 
I I I I I I I I I 
J J J J J J J J J J 
K K K K K K K K K K K 
L L L L L L L L L L L L 
M M M M M M M M M M M M M 
N N N N N N N N N N N N N N 
O O O O O O O O O O O O O O O 
P P P P P P P P P P P P P P P P 
Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q 
R R R R R R R R R R R R R R R R R R 
S S S S S S S S S S S S S S S S S S S 
T T T T T T T T T T T T T T T T T T T T 
U U U U U U U U U U U U U U U U U U U U U 
V V V V V V V V V V V V V V V V V V V V V V 
W W W W W W W W W W W W W W W W W W W W W W W 
X X X X X X X X X X X X X X X X X X X X X X X X 
Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y 
Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z Z '''
 
