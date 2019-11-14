import random
import string
from random import choice

def generate_password(m):
    password = ''
    for i in range(m):
        val = random.choice([1, 2])
        if val == 1:
            while 1:
                tamp = random.sample(string.digits, 1)[0]
                if tamp != '0' and tamp != '1':
                    password += tamp
                    break
        elif val == 2:
            while 1:
                tamp = random.sample(string.ascii_letters, 1)[0]
                if tamp != 'l' and tamp != 'I' and tamp != 'O' and tamp != 'o':
                    password += tamp
                    break
    return password

def main(n, m):
    list_of_passwords = []
    for i in range(n):
        list = []
        list.append(generate_password(m))
        list_of_passwords.append(list)
    list_of_passwords = [item for sublist in list_of_passwords for item in sublist]
    return list_of_passwords

print('Cлучайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15),  sep='\n')
