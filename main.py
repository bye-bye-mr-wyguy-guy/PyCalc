#Defines operations
def add(a, b):
    return (a + b)
def multi(a, b):
    return (a * b)
def div(a, b):
    if b == 0:
        raise ValueError("Haha, so funny chucklenuts. Restart the program. Here, fine. Infinity. Or zero. Probably Zero. Why are you still reading?")
    return (a / b)
def dif(a, b):
    return (a - b)
def pow(a, b):
    return(a ** b)
def avg(num):
    # Ready data point storage
    data_points = []
    dpnum = 1

    #Add data points
    for i in range(num): 
        data_points.append(float(input(f'Data point {dpnum}: ')))
        dpnum = dpnum + 1

    #Calculate avg
    return (sum(data_points) / len(data_points))
    
def mod(a, b):
    if b == 0:
        exit("Nice try. Modulus by zero is undefined too.")
    quotient = int(a // b)
    remainder = a % b
    return f"{quotient}r{remainder:g}"
    
def fact(a):
    #Safeguard
    if a < 0:
        exit('Positives ONLY')
    #Setup
    numf = a
    total = 1
    #Factoring
    while numf > 1:
        total = total * numf
        numf = numf - 1
    return total
def expg(a, b, num):
    print(a)  # Print the initial starting number
    cur = a
    while num > 0:
        # Dynamically evaluates the math expression string (e.g., "1.0 + 3")
        cur = eval(f"{cur} {b}")
        print(cur)
        num = num - 1

      
def sci(a):
    return f"{float(a):.6g}"

def perc(a, b):
    return (a / 100) * b

def convert(a, mode):
    if mode == 1:
        return a * 1.609344
    elif mode == 2:
        return a / 1.609344
    elif mode == 3:
        return (a * 9 / 5) + 32
    elif mode == 4:
        return (a - 32) * 5 / 9
    elif mode == 5:
        return a * 0.45359237
    elif mode == 6:
        return a / 0.45359237
    elif mode == 7:
        return a * 29.57353
    elif mode == 8:
        return a / 29.57353
    else:
        raise ValueError("Unknown conversion")
        
def ratsimp(a, b):
    # Convert inputs to strings to count decimal places
    a_str = str(a)
    b_str = str(b)

    decimals_a = len(a_str.split(".")[1]) if "." in a_str else 0
    decimals_b = len(b_str.split(".")[1]) if "." in b_str else 0
    decimals = max(decimals_a, decimals_b)

    # Shift both decimal points equally
    scale = 10 ** decimals
    a = round(a * scale)
    b = round(b * scale)

    # Find the greatest common divisor
    x = abs(a)
    y = abs(b)

    while y:
        x, y = y, x % y

    if x == 0:
        raise ValueError("Cannot simplify 0:0")

    return f"{a // x}:{b // x}"


def fuladd(a, mode):

    def fullen(a):
        total = 0
        while a >= 0:
            total += a
            a -= 1
        return total

    total = 0

    if mode == 1:
        return fullen(a)

    elif mode == 2:
        while a >= 0:
            total += fullen(a)
            a -= 1

    else:
        raise ValueError("Unknown mode")

    return total

        
#Gets problem info/ creates problem
oper = int(input('Enter Operation(sum=1, multiply=2, divide=3, difference=4, power=5, mean=6, divide with remainder=7, factorial=8, exponential growth=9, scientific conversion=10, percent of=11, converter=12, ratio simplifier=13, fullen and adden numbers=14):'))
if oper < 1 or oper > 14:
    exit('Unknown operator')
if oper ==6:
    num = int(input('How many data points?'))
    print(avg(num))
    exit("Thank you for using PyCalc!")
if oper ==8:
    a = int(input('What factored?(Whole number)'))
    #if a ==:
      #exit("We got waterjug patrick here tryna' use Python. I mean HOW are you so dumb that you bypass the int()?")
    print(fact(a))
    exit("Thank you for using PyCalc!")
if oper ==9:
    a = float(input("Enter starting number:"))
    b = input("Enter operation(With space, like [* 7]:")
    if any(char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]" for char in b):
      exit("You are not injecting today, buckaroo!")
    if len(b.strip()) > 10:
        exit("Whoa there, buckaroo! Keep your modifier numbers small and reasonable.")
    num = int(input("How many times?"))
    expg(a, b, num)
    exit("Thank you for using PyCalc!")
if oper ==10:
  print(sci(input("What should I convert?")))
  exit("Thank you for using PyCalc!")
if oper ==12:
    mode = int(input("What to what?(1= mi to km, 2= km to mi, 3=c to f, 4=f to c, 5=lbs to kg, 6=kg to lbs, 7=fl oz to ml, 8=ml to fl oz):"))
    a = float(input("What amount?"))
    print(convert(a, mode))
    exit("Thank you for using PyCalc!")
if oper ==14:
    a = int(input("What number?"))
    mode = int(input("What mode(1=Fullen, 2=Adden)"))
    print(fuladd(a, mode))
    exit("Thank you for using PyCalc!")
a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))

#Solves problem and prints answer(see 'Defines operations')
if oper == 1:
    print(add(a, b))
elif oper == 2:
    print(multi(a, b))
elif oper == 3:
    print(f"{div(a, b):.2f}")
    more = input('More?(T/t or F/f)')
    if more in ['T', 't']:
        print(div(a, b))
elif oper ==4:
    print(dif(a, b))
elif oper ==5:
    print(pow(a, b))
elif oper ==7:
    print(mod(a, b))
elif oper ==11:
    print(perc(a, b))
elif oper ==13:
    print(ratsimp(a, b))

    

  #This is a Python 13-operation calculator by Wyatt Fullerton
  
