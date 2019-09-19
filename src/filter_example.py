numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filterOddNum(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


out_filter = filter(filterOddNum, numbers)

print("Type:", type(out_filter))
print("Filtered seq:", out_filter)
