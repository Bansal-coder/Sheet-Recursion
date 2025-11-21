def pal(s):
    if len(s)<2:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])
s=input()
if pal(s):
    print("palindrome")
else:
    print("not palindrome")