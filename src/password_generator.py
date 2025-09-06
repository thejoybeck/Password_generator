import random
import string

def generate_password(length=15):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password

new_password = generate_password()
print("Generated Password:", new_password)

# Save to file (simple way)
with open("passwords.txt", "a") as file:
    file.write(f"MySite: {new_password}\n")