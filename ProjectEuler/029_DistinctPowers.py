__author__ = 'johan'

# Consider all integer combinations of a^b for 2 ? a ? 5 and 2 ? b ? 5:
#
#    2^2=4, 2^3=8, 2^4=16, 2^5=32
#    3^2=9, 3^3=27, 3^4=81, 3^5=243
#    4^2=16, 4^3=64, 4^4=256, 4^5=1024
#    5^2=25, 5^3=125, 5^4=625, 5^5=3125
#
# If they are then placed in numerical order, with any repeats removed, we get the following
# sequence of 15 distinct terms:
#
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
#
# How many distinct terms are in the sequence generated by a^b for 2 ? a ? 100 and 2 ? b ? 100?


# x^y = (x*x)^(y/2)
#
# The total number of terms generated will be 99 * 99 = 9801
# How many of those will be duplicates? Those where x is a square and 4 <= sqrt(x) <= 10 and 2 * y < 100.
# E.g. 2^4 = 16 = 4^2, 2^6 = 64 = 4^3, 2^8 = 256 = 4^4, 2^10 = 1024 = 4^5 etc.
#
# There are 9 squares between 2 and 100:
# 2 => 4, 3 => 9, 4 => 16, 5 => 25, 6 => 36, 7 => 49, 8 => 64, 9 => 81, 10 => 100
# All the coefficients y for these where 2 <= y <= 50 have corresponding results for lower combinations.
#
# 9 * 49 = 441
# 9801 - 441 = 9360



def brute_force(xmin, xmax, ymin, ymax):
    result = {}

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            temp = x ** y

            if temp not in result.keys():
                result[temp] = [(x, y)]
            else:
                print(temp, ":", x, y)

    return result

print(brute_force(2, 5, 2, 5))
print(len(brute_force(2, 100, 2, 100)))
