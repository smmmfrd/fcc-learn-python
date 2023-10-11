def loop_add_one(num):
    total = num
    for _ in range(9 - num):
        total += 1
        print(total)
    return total + 1


looptotal = loop_add_one(0)
print(looptotal)


def rec_add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)
    return rec_add_one(total)


rectotal = rec_add_one(0)
print(rectotal)
