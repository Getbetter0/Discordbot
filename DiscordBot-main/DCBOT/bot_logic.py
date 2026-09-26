import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coin_flip():
    return random.choice(["Orzeł", "Reszka"])