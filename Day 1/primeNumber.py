print("_____________Prime number tester_____________")
testNumber = int(input("Enter the test number: "))

def isPrime(num):
    if num == 1:
        return False
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while(i*i <= num):
        if num%5 == 0 or num%(i+2) == 0:
            return False
        i+=6
    return True

print(isPrime(testNumber))
    