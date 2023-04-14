
def prime_factors(num):
    """This function give us the list of prime factors of the written number."""
    while num > 1:
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                break
        else:
            factor = num

        num //= factor
        yield factor

def is_prime(num):
    """This function return us True if number is prime and False if number is not."""
    for i in range(2 ,int (num ** 0.5) + 1 ):
        if num % i == 0:
            return False
    return True

def prime_range(num):
    """This function give us the range from 2 to the given number including only prime numbers."""        
    for i in range(2, num ):
        if is_prime(i):
            yield i
          

