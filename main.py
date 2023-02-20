import operators
import others
import trig


# x = operators.add(20,10)
# y = operators.subtract(20,10)
# p = operators.multiply(3,6)
# print(p)

# x=others.cube(3)
# print(x)
operator=input("enter operator:")
#get numbers
if operator=="cube":
    num=eval(input("enter number:"))
    b=others.cube(num)
    print(b)

elif operator=="sin":
      angle=eval(input("enter angle in degrees:"))
      sin_of_angle=trig.get_sine(angle)
      print(sin_of_angle)
    
elif operator=="tan":
      angle=eval(input("enter angle in degrees:"))
      
      print(trig.get_tan(angle))
      
elif operator=="cos":
      angle=eval(input("enter angle in degrees:"))
      
      print(trig.get_cos(angle)) 

else:
 num1=eval(input("enter number:"))
 num2=eval(input("enter number:"))

if operator=="+":
        x=operators.add(num1,num2)
        print(x)
elif operator=="-":
        y=operators.subtract(num1,num2)
        print(y)
elif operator=="*" or operator=="x"or operator=="X":
        a=operators.multiply(num1,num2)
        print(a)
elif operator=="/":
        q=operators.divide(num1,num2)
        print(q)


