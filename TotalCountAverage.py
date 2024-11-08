def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False


total = 0.0
count = 0
average = 0
while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    number = check_for_float(input_number)
    if not number:
        continue

    count += 1
    total += number

if count != 0:
    average = total / count
print(total, count, average)


