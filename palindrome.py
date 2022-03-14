string=input("Enter string :")
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return "Not Palindrome"
        left_pos += 1
        right_pos -= 1
    return "Palindrome"


print(isPalindrome(string))
