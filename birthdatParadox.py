from birthday_utils import generate_birthdays, get_match

numbers_of_birthdays = int(input("enter how many birthdays do you want?:> "))

# آزمایش را به تعداد بالا مثلا یک میلیون بار تکرار کنید و احتمال را محاسبه کنید

birthdays = generate_birthdays(numbers_of_birthdays)
match = get_match(birthdays)
print(match)


