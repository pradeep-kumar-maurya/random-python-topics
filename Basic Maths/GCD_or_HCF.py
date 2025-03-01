# ------------------------- Euclidean Normal ------------------------------
def find_hcf(n1, n2):  # Worst case T.C = O(min(n1, n2)), S.C = O(1)
    # Euclidean algorithm
    '''
    Euclidean algorithm states that hcf(n1, n2) = hcf((n2-n1), n1)
    where n2 > n1. The process i.e. hcf((n2-n1), n1) keeps on happening until
    (n2-n1) becomes 0. If (n2-n1) is 0 then answer is n1.
    '''
    temp1 = -1
    temp2 = -1

    while True:

        temp1 = max(n1, n2) - min(n1, n2)
        temp2 = min(n1, n2)

        if temp1 == 0:
            return temp2
        
        n1 = temp1
        n2 = temp2
# ------------------------- Euclidean Normal ------------------------------


# ------------------------- Euclidean RECURSION ---------------------------
def gcd(a, b):  # Worst case T.C = O(min(a, b)), S.C = O(min(a, b))
    if a == 0:
        return b
    
    return gcd(max(a, b) - min(a, b), min(a, b))


def find_hcf(n1, n2):
    return gcd(n1, n2)
# ------------------------- Euclidean RECURSION ---------------------------


# ------------------------------ BEST T.C ----------------------------------
'''
The idea here is:- let's take (52, 10). 52-10=42, 42-10=32, 32-10=22, 22-10=12
12-10=2. Basically, we were able to subtract 10 from 52, 5 times until it becomes
-ve. This is nothing but divisibilty of 52 by 10, and at last, we will get 2 which
is (52 % 10). Once it is (2, 10), the same divisibilty and remainder priciple can
be applied to 2, 10 i.e. (10 % 2). Modulus value becomes 0 and ans is min(10, 2) i.e. 2.
'''
def find_hcf(n1, n2):  # T.C = O(log(min(n1, n2)) base to phi)
    if n1 == 0 or n2 == 0:
        return 0

    while True:
        temp1 = max(n1, n2) % min(n1, n2)
        temp2 = min(n1, n2)

        if temp1 == 0:
            return temp2
        
        n1 = temp1
        n2 = temp2


print(find_hcf(0, 0))
print(find_hcf(52, 10))
# ------------------------------ BEST T.C ----------------------------------

