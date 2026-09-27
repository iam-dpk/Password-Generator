from src.strength import password_strength

def test_empty(): assert password_strength("")[0] == "Empty"

def test_stronger_score(): assert password_strength("A9!longSecurePassword")[1] > password_strength("abc")[1]
