def check_palindrome(strs):
    j=len(strs)-1
    for i in range(len(strs)):
        if(strs[i]==strs[j]):
            j-=1
        else:
            return False
    return True