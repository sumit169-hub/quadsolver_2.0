print("Welcome, to Quad_eq_solver_v2.0")
print("For more info look for Readme.md")
while True:
    action=input()
    if action=='Q':
        print("Bye")
        break
    elif action=='S':
        print('Program Started...')
        while True:
            
                
            c1=int(input('a='))
            a=c1
            x='x'
            c2=int(input('b='))
            c3=int(input('c='))
            d=int(input('d='))
            if c1==0:
                print("Your equation is %sx+%s=%s"%(c2,c3,d))
                v=d-c3
                v2=v/c2
                print("x=%s"%(v2))
                action=input()
                if action=='Q':
                    break
                
            
                    
            else:
                if d==0:
                    print('Calculating for Solution ........')
                    if 0<a<2:
                        print('Your equation is  x^2+(%s)x+(%s)=0'%(c2,c3))
                    else:
                        print('Your equation is  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,c3))
                    D=c2**2-4*c1*c3
                    x1=(-c2+(D**0.5))/(2*c1)
                    x2=(-c2-(D**0.5))/(2*c1)
                    print("Roots are")
                    print("x1=",x1)
                    print("x2=",x2)
                    action=input()
                    if action=='Q':
                        break
                    else:
                        continue
               
                
                elif d>=0:
                    print('Solving...')
                    if 0<a<2:
                        print('Your equation is  x^2+(%s)x+(%s)=(%s)'%(c2,c3,d))
                    else:
                        print('Your equation is  (%s)x^2+(%s)x+(%s)=(%s)'%(c1,c2,c3,d))
                    D=c3-d
                    if 0<a<2:
                        print('Equation becomes:  x^2+(%s)x+(%s)=0'%(c2,D))
                    else:
                        print('Equation becomes:  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,D))
                    D3=c2**2-4*c1*D
                    x1=(-c2+(D3**0.5))/(2*c1)
                    x2=(-c2-(D3**0.5))/(2*c1)
                    print("Roots are")
                    print("x1=",x1)
                    print("x2=",x2)
                    action=input()
                    if action=='Q':
                        break
                    else:
                        continue
                
                
                elif d<=0:
                    print('Solving..')
                    if 0<a<2:
                        print('Your equation is  x^2+(%s)x+(%s)=(%s)'%(c2,c3,d))
                    else:
                        print('Your equation is  (%s)x^2+(%s)x+(%s)=(%s)'%(c1,c2,c3,d))
                    D=c3-d
                    if 0<a<2:
                        print('Equation becomes:  x^2+(%s)x+(%s)=0'%(c2,D))
                    else:
                        print('Equation becomes:  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,D))
                    D3=c2**2-4*c1*D
                    x1=(-c2+(D3**0.5))/(2*c1)
                    x2=(-c2-(D3**0.5))/(2*c1)
                    print("Roots are")
                    print("x1=",x1)
                    print("x2=",x2)
                    action=input()
                    if action=='Q':
                        break
                    else:
                        continue
          
        
        
            
         
print('Thanks for using')      