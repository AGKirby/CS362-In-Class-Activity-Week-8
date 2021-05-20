def main(year):
    if(year % 4 == 0): # if year is divisible by 4
        if(year % 100 != 0 or year % 400 == 0): # if year is not divisble by 100 unless divisible by 400
            return True
    return False
