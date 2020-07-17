print("Prime or Composite?")


while True: #repeats forever
    print('''

    ''')
        
    #error checking
        num = input("Please Enter a Number:   ")
        error = num.isdecimal()
        while error==False:
            print("The Value You Have Entered is Invalid. Please Enter a Positive Integer Instead.")      
            num = input("Please Enter a Number:   ")
            error = num.isdecimal()
        num = int(num)

    if num == 2 or num == 1: #makes sure 1 and 2 are included as prime
        print(num, "is a prime number")
    elif num == 0: #zero is a special number
        print(num, "is neither prime nor composite")
    elif num > 2: #divides num by every value between 2 and num to see whether num is prime or composite
        for val in range(1, num):
            if num%val == 0: #% is used to determine the remainder. If the remainder is 0, then the value is composite
                print(num, "is a composite number") 
                break
            else:
                print(num, "is a prime number")
                break
    else:
        print(num, "is not a prime number") # is num is negative, it is composite

    
    
