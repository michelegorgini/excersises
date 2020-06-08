# Example of recursive function
#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens


def iGcd(m, n):
    """Calculate the Greatest Common Divisor of m and n.

    Unless n==0, the result will have the same sign as n (so that when
    n is divided by it, the result comes out positive).
    """
    while n > 0:
        m, n = n, m % n
        print(m,n)
    print(m, 'result')
    return m


#This procedure recursively computes the gcd of two numbers
def rGcd(m, n):
    print (m, n)
    if m % n == 0:
        print(n, 'return n')
        # when we get n, n became the result of previous call line 27 (gcd = rGcd(n, m % n) -> 14 = rGcd(28, 14) ->
        # 14 = rGcd(658, 28) -> 14 = rGcd(1344, 658) ->
        return n
    else:
        gcd = rGcd(n, m % n)
        print(gcd, 'Result', n, 'm number', m % n, 'n number')
        return gcd

#iGcd(11, 7)

rGcd(2002, 1344)
