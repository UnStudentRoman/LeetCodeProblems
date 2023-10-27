
def isHappy(n):
    previous_n = []
    n_sqrt = num_sqrt(n)
    while n_sqrt != 1:
        if n_sqrt in previous_n:
            return False
        previous_n.append(n_sqrt)
        n_sqrt = num_sqrt(n_sqrt)
    return True

def num_sqrt(number):
    number = [int(digit)**2 for digit in str(number)]
    return sum(number)



if __name__ == '__main__':
    n = 19
    print(isHappy(n))