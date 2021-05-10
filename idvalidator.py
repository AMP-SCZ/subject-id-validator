def validate(some_id):
    # Basic checks: len == 7 and first two chars are not numbers
    if len(some_id) != 7:
        return False
    if some_id[0].isdecimal() or some_id[1].isdecimal():
        return False

    # Convert ID to array of numbers, excluding check digit
    id_array = []
    id_array.append(ord(some_id[0]))
    id_array.append(ord(some_id[1]))
    id_array = id_array + list(some_id[2:6])

    # Use check digit algorithm to generate correct check digit
    check_digit_array = []

    for pos in range(0, len(id_array)):
        check_digit_array.append(int(id_array[pos]) * (pos+1))
    check_digit = sum(check_digit_array) % 10

    # Check correct check digit against entered ID
    if int(some_id[6]) != check_digit:
        return False

    return True