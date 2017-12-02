def checksum(input : list):
    checksum = 0
    for row in input:
        max = min = row[0]
        for c in row:
            if(c > max):
                max = c
            if(c < min):
                min = c
        checksum += max - min
    return checksum