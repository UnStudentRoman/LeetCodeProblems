def totalFruit(fruits):
    if len(fruits) == 1:
        return 1
    l = 0
    max_fruits = 0
    accepted_fruits = nextFruits(l)

    while l < len(fruits) - 2:
        potential_fruits = 0

        for fruit in fruits[l:]:
            if fruit in accepted_fruits:
                potential_fruits += 1
            else:
                break

        if potential_fruits > max_fruits:
            max_fruits = potential_fruits
        l += potential_fruits - 1

        accepted_fruits = nextFruits(l)

    return max_fruits


def nextFruits(l):
    accepted_fruits = []
    for fruit in fruits[l:]:
        if fruit not in accepted_fruits:
            accepted_fruits.append(fruit)
        if len(accepted_fruits) == 2:
            break
    return accepted_fruits

if __name__ == '__main__':
    fruits = [0,1,1,6,6,4,4,6]
    print(totalFruit(fruits))