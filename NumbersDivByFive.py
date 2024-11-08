def numbers_divisible_byfive(p_list):
    for num in p_list:
        if num > 130:
            break
        if num % 5 == 0:
            print(num)
    print("STOP")


list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
print(numbers_divisible_byfive(list1))
