def is_fizzbuzz(numbers):
    tmp1 = ""
    tmp2 = ""
    if numbers == int(numbers):
        if numbers%3 == 0:
            tmp1 = "fizz"
        if numbers%5 == 0:
            tmp2 = "buzz"
        return str(tmp1) + str(tmp2)
    else:
        return False