#ProjectEuler Question 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    strNum = str(number)
    for i in range(0, len(strNum)/2):
        if strNum[i] != strNum[len(strNum) - 1 - i]:
            return False
    return True

def largestProduct(num1, num2):
    largest = 0
    while num1 > 99 and num2 > 99:
        x = 0
        product = num1 * num2        
        while num1 > 99 and num2 > 99:
            product = num1 * num2
            print num1, num2, product
            if isPalindrome(product) == True and product > largest:
                largest = product
            else:
                num1 -= 1
        x += 1
        num1 = 999 - x
        num2 -=1
    return 'The largest palindrome made from the product of two 3-digit numbers is ' + str(largest) + '.'

def main():
    num1 = 999
    num2 = 999
    print largestProduct(num1, num2)

if __name__ == '__main__':
    main()
            
