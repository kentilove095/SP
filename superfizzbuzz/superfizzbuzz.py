def superfizzbuzz(num):
    tmp = ""
    if num % 3 == 0:
        tmp.append("Fizz")
        if num % 9 == 0:
            tmp.append("Fizz")
            if num % 25 == 0:
                tmp.append("BuzzBuzz")
        elif num % 5 == 0:
            tmp.append("Buzz")
    elif num % 5 == 0:
        tmp.append("Buzz")
        if num % 25 == 0:
            tmp.append("Buzz")
    else:
        tmp = "NoFizzBuzz"
    return (tmp)
