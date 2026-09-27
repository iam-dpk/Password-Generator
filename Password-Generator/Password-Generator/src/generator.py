import secrets
import string
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/|~"

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    pools, required = [], []
    if use_upper:
        pools.append(string.ascii_uppercase); required.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        pools.append(string.ascii_lowercase); required.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        pools.append(string.digits); required.append(secrets.choice(string.digits))
    if use_special:
        pools.append(SPECIAL_CHARACTERS); required.append(secrets.choice(SPECIAL_CHARACTERS))
    if not pools:
        raise ValueError("Select at least one character type.")
    alphabet = "".join(pools)
    password = required + [secrets.choice(alphabet) for _ in range(max(0, length-len(required)))]
    for i in range(len(password)-1, 0, -1):
        j = secrets.randbelow(i+1)
        password[i], password[j] = password[j], password[i]
    return "".join(password)
