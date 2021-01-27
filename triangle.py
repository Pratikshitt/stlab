

while(1):
        while(1):
        
        
            print("\nEnter 3  sides of triangle\n")
            a=int(input())
            b=int(input())
            c=int(input())

            print(a,b,c)
            c1 = a>=1 and a<=10
            c2= b>=1 and b<=10
            c3= c>=1 and c<=10
            if (not c1):
                
                print(a,"is not in range")
                continue
            elif (not c2):
                
                print(b,"is not in range")
                continue
            elif (not c3):
                print(c,"is not in range")
                continue
            else:
                break
     

        if( a<b+c and b<a+c and c<a+b ):      
            if ((a==b) and (b==c)):
                print("\nequilateral triangle\n")

            
            elif ((a!=b) and (a!=c) and (b!=c)):
                print("\nscalene triangle\n")

            
            else:
                print("\nisosceles triangle\n")
                
        else:
            print("\nNot a triangle\n")




    
    
