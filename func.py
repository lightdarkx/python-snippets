def intToDigits(number):

    digits = []
    while (number > 0):
        digits.append(number % 10) 
        number //= 10
    
    digits.reverse()

    return digits
    



print("Enter Number")
num = int(input())
print(intToDigits(num))