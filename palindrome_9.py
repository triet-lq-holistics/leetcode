def isPalindrome(self, x: int) -> bool:
    strX = str(x)

    leftP = 0
    rightP = len(strX) - 1

    while leftP < rightP:
        if strX[leftP] != strX[rightP]:
            return False
        leftP += 1
        rightP -= 1
    
    return True

def isPalindrome(self, x: int) -> bool:
    if x <0:
          return False
     
    reserve = 0

    while x > reserve:
        reserve = reserve*10 + x%10
        x //= 10

    return (x == reserve) or (reserve == x // 10)
