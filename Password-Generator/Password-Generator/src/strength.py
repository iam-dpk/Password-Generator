from .generator import SPECIAL_CHARACTERS

def password_strength(password):
    if not password: return "Empty", 0
    score = min(len(password) * 4, 40)
    groups = sum([any(c.islower() for c in password), any(c.isupper() for c in password),
                  any(c.isdigit() for c in password), any(c in SPECIAL_CHARACTERS for c in password)])
    score = min(100, score + groups * 15 + (5 if len(set(password)) >= max(6, len(password)//2) else 0))
    label = "Weak" if score < 40 else "Medium" if score < 70 else "Strong" if score < 90 else "Very Strong"
    return label, score
