def rollDice3(K, m, Z):
    point = [i for i in range(1, K + 1)]
    counter = [0 for _ in range(Z + 1)]

    for i in range(1, K + 1):
        if i >= Z:
            counter[Z] += 1
        else:
            counter[i] = 1

    times = m - 1
    roll = 1
    while times > 0:
        tmp = [0 for _ in range(Z + 1)]
        for i in range(roll, Z + 1):
            for p in point:
                if i + p >= Z:
                    tmp[Z] += counter[i]
                else:
                    tmp[i + p] += counter[i]
        times -= 1
        roll += 1
        counter = tmp

    res = counter[Z]

    return res / (K ** m)
