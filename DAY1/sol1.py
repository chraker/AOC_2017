def sumSequence(sequence: list):
    prev = sequence.pop(0)
    sequence.append(prev)
    sum = 0
    for n in sequence:
        if n is prev:
            sum += n
        prev = n
    return sum
