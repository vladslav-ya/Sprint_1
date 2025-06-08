def digit_root(num):
    while num > 9:
        summ_num = 0
        while num > 0:
            l_dig = num % 10
            summ_num += l_dig
            num = num // 10
        num = summ_num

    return num


print(digit_root(889987))
