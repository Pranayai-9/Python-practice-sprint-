import random
import string

def passw():
    characters = string.ascii_letters + string.digits + string.punctuation
    passwordLength = random.randint(8,12)
    password = ''.join(random.choices(characters, k=passwordLength))
    return password
print('Generated password:', passw()) 

    
