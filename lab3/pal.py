s = input()



def palindrome(a):
    rev = ''
    for i in reversed(a):
        rev += i
    if rev == a:
        return True
    else:
        return False


if palindrome(s):
    print("Palindrome")
else:
    print("Not a Palindrome")
