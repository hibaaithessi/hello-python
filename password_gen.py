import random
import string

longueur = 16

caracteres = string.ascii_letters + string.digits + "!@#$%^&*"

mot_de_passe = ""

for i in range(longueur):
    mot_de_passe += random.choice(caracteres)

print("كلمة السر ديالك:", mot_de_passe)