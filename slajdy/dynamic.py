def sum(xs, init):
    result = init 
    for x in xs:
        result += x
    return result


print(sum([1, 2, 3], 0)) # prints 6
print(sum({'a': 'b', 'c': 'd'}, 'Keys: ')) # prints: Keys: ac
