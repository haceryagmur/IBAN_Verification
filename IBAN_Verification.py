# IBAN Verification

iban = input("IBAN: ")
first_number = ord(iban[:1]) - ord("A") + 10
second_number = ord(iban[1:2]) - ord("A") + 10
new_number = iban[4:] + str(first_number) + str(second_number) + "00"
resulting_number = int(new_number) % 97 
check_digit = 98 - resulting_number
if check_digit == int(iban[2:4]):
    print("Entered IBAN is valid")
else:
    print("Please enter a valid IBAN")

