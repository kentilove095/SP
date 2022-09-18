def superfizzbuzz(num):
    tmp = ""
    if num % 3 == 0:
        tmp += "Fizz"
        if num % 9 == 0:
            tmp += "Fizz"
            if num % 25 == 0:
                tmp += "BuzzBuzz"
        elif num % 5 == 0:
            tmp += "Buzz"
    elif num % 5 == 0:
        tmp += "Buzz"
        if num % 25 == 0:
            tmp += "Buzz"
    else:
        tmp = "NoFizzBuzz"
    return tmp
