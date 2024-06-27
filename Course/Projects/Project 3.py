def is_valid_CC(number):
    if not (13 <= len(number) <= 16) or not number.isdigit():
        return False
    if not (number.startswith('4') or number.startswith('5') or number.startswith('6') or number.startswith('37')):
        return False
    
    def luhn_algorithm(n):
        sum_odd = sum(int(n[i]) for i in range(len(n)-1, -1, -2))
        sum_even = 0
        for i in range(len(n)-2, -1, -2):
            double = int(n[i]) * 2
            if double > 9:
                double = double - 9
            sum_even += double
        total = sum_odd + sum_even
        return total % 10 == 0
    
    return luhn_algorithm(number)

def is_valid_RN(number):
    if len(number) != 9 or not number.isdigit():
        return False
    
    def aba_algorithm(n):
        sum_thirds = sum(int(n[i]) for i in range(len(n)-1, -1, -3))
        sum_thirds_2 = sum(int(n[i]) for i in range(len(n)-2, -1, -3)) * 7
        sum_thirds_3 = sum(int(n[i]) for i in range(len(n)-3, -1, -3)) * 3
        total = sum_thirds + sum_thirds_2 + sum_thirds_3
        return total % 10 == 0
    
    return aba_algorithm(number)

def test_validation():
    print("Credit Card Entry")
    print("-" * 80)
    while True:
        cc_number = input("Enter credit card number: ")
        if cc_number.lower() == 'q':
            break
        print(f"{cc_number} is {'valid' if is_valid_CC(cc_number) else 'invalid'}")

    print("\nRouting Number Entry")
    print("-" * 80)
    while True:
        rn_number = input("Enter routing number: ")
        if rn_number.lower() == 'q':
            break
        print(f"{rn_number} is {'valid' if is_valid_RN(rn_number) else 'invalid'}")

test_validation()
