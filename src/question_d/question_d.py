#write functions here, don't add input('') statements here!

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False 
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True 