def checksumP1(input : list):
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

def checksumP2(input : list):
    checksum = 0
    for row in input:
        for c in row:
            rowCheckSum = None
            for cc in row:
                if not c % cc and not c is cc:
                    rowCheckSum = c / cc
                    break
            if rowCheckSum is not None:
                checksum += rowCheckSum
                break
    return checksum
