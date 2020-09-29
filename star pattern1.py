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
for i in range(6,-1,-1):
    for j in range(i):
        print("*", end=" ")
    print("")

'''o/p:
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''
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

k=10
for i in range(5,-1,-1):
    for j in range(k,0,-1):
        print("",end=" ")
    k=k+1
    for j in range(i+1):
        print("*", end=" ")
    print("")
'''o/p:
          * * * * * * 
           * * * * * 
            * * * * 
             * * * 
              * * 
               * '''

k=15
for i in range(5):
    for j in range(k):
        print("",end=" ")
    k=k-1
    for j in range(i+1):
        print("*", end=" ")
    print("")
k=10
for i in range(5,-1,-1):
    for j in range(k,0,-1):
        print("",end=" ")
    k=k+1
    for j in range(i+1):
        print("*", end=" ")
    print("")
'''o/p:
               * 
              * * 
             * * * 
            * * * * 
           * * * * * 
          * * * * * * 
           * * * * * 
            * * * * 
             * * * 
              * * 
               * 




