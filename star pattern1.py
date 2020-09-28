k=10
for i in range(6):
    for j in range(k):
        print("",end=" ")
    k=k-2
    for j in range(i):
        print("*", end=" ")
    print("")
'''o/p:
        * 
      * * 
    * * * 
  * * * * 
* * * * * '''
k=5
for i in range(6):
    for j in range(k):
        print("",end=" ")
    k=k-1
    for j in range(i):
        print("*", end=" ")
    print("")
'''o/p:
  
    * 
   * * 
  * * * 
 * * * * 
* * * * * '''


