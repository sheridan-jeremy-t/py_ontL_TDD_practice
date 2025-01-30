def add(*numbers):
    total = 0 #initialize a total of zero
    for number in numbers: #iterate over each param value
        total += number #add the number to the total
    return total