import random
import string       #importing string library

def generate_pass(min_length,numbers=True,special_char=True): #defining func for generate a password
    char=string.ascii_letters
    num=string.digits
    special_chart=string.punctuation

    word=char
    if numbers:
        word += num

    if special_char:
        word += special_chart

    pwd=""
    meet_criteria    = False
    has_num     = False
    has_sp_char = False

    while not meet_criteria or len(pwd) < min_length: #checking whether all pwd condition gets satisfied
        new_char=  random.choice(word)
        pwd += new_char

        if new_char in num:
            has_num = True
            
        elif new_char in special_chart:
            has_sp_char = True

        meet_criteria == True
        if numbers:
            meet_criteria = has_num
        if special_char:
            meet_criteria = meet_criteria and has_sp_char

    return pwd


pwd = generate_pass(10)

print(pwd)