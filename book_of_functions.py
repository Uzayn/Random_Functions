def translate(phrase): #our translate function takes in a phrase or a string
    translation = "" # we set this to an empty string
    for letter in phrase:
        if letter in "AEIOUaeiou": #for all the letter in the phrase we input, if any letter is in aeiouAEIOU 
            translation = translation + ""#
        else:
            translation = translation + letter
    return translation


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num 
    return result


def add_function(num1, num2):
    return num1 + num2
