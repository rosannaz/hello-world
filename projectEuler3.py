#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def main():
    number = int(raw_input('Please Enter an Integer: '))
    print 'The largest prime factor of ' + str(number) + ' is ' + str(findLargestPrimeFactor(number)) + '.'

def findLargestPrimeFactor(number):  
    factor = 2
    if isPrime(number) == True:
        largest = number
    else:    
        while number > 1:
            if number % factor == 0 and isPrime(number / factor) == True:
                largest = number/factor
                break
            factor+=1
    return largest

def isPrime(x):
        global largest
        for i in range(2,int(x**(0.5) + 1)):
            if x % i == 0:
                return False
        return True  
        
if __name__ == '__main__':
    main()