#we need a function to check if an integer is pandigital
def isPandigital(n):
    n = str(n)
    l = len(n)
    beg = set([i for i in range(1, l + 1)])
    end = set([int(d) for d in n])
    return beg == end
#we need a function to check if a product whose multiplicand/multiplier/product identity is 9 pandigital
def isProduct9Pandigital(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigital(int(numbers))
products = []
#now let's go through all the reasonable possibilities (use paper & pencil)
for a in range(1, 10000):
    for b in range(a, 10000):
        # If one product is not valid then the higher products aren't also
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if isProduct9Pandigital(a, b):
            products.append(a*b)
            print("%i x %i = %i" % (a, b, a*b))
#then return the sum of the set (no index so it goes faster)
print (sum(set(products)))
