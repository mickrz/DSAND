def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    if number == 0 or number == 1:
        return number
    
    if number < 0:
        return -1

    lower_bound = number // 2
    upper_bound = lower_bound
    delta = upper_bound - lower_bound
    
    while delta != 1:
        if lower_bound * lower_bound > number:
            upper_bound = lower_bound
            lower_bound //= 2

        if upper_bound * upper_bound <= number:
            return upper_bound

        delta = upper_bound - lower_bound
        if delta > lower_bound:
            upper_bound -= delta // 2
        elif delta < 10 and delta > 1:
            upper_bound -= (upper_bound % 2) + 1
        elif delta == 1:
            return lower_bound        
        else:
            upper_bound -= delta // 1000 + 1
            

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (-1 == sqrt(-27)) else "Fail")
print ("Pass" if  (4567 == sqrt(20857489)) else "Fail")
print ("Pass" if  (9510 == sqrt(90440100)) else "Fail")