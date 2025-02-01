print("Equation a*x**2 + b*x + c == 0")                  
a = float(input("Enter a: "))                            
b = float(input("Enter b: "))                            
c = float(input("Enter c: "))                            
delta = b**2-4*a*c                                       
if delta > 0:                                            
    x_1 = (-b-delta**0.5)/(2*a)                          
    x_2 = (-b+delta**0.5)/(2*a)                          
    print("Primes of the quadratic equation")            
    print(f"x_1 = {x_1}")                                
    print(f"x_2 = {x_2}")                                
elif delta == 0:                                         
    x_1 = (-b)/(2*a)                                     
    x_2 = x_1                                            
    print("Primes of the quadratic equation:")           
    print(f"x_1 = x_2 = {x_1}")                          
else:                                                    
    print("no solution")                                 
                                               
