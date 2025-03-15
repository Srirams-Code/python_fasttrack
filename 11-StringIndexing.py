# indexing = accessing elements of a sequence using [] ( indexing operator )
#            [start : end : step ]

credit_card_number = "1234-5678-9485-4758"

print(credit_card_number[5])
print(credit_card_number[5:])
print(credit_card_number[5:8])
print(credit_card_number[::3])
print(credit_card_number[::2])
print(credit_card_number[::4])

last_4_digits = credit_card_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_4_digits}")

# reversing a string
print(credit_card_number[::-1]) 