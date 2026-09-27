from src.generator import generate_password, SPECIAL_CHARACTERS

def test_password_length(): assert len(generate_password(20)) == 20

def test_password_contains_groups():
    p=generate_password(24)
    assert any(c.isupper() for c in p); assert any(c.islower() for c in p)
    assert any(c.isdigit() for c in p); assert any(c in SPECIAL_CHARACTERS for c in p)

def test_invalid_length():
    try: generate_password(3); assert False
    except ValueError: assert True

def test_no_groups():
    try: generate_password(12,False,False,False,False); assert False
    except ValueError: assert True
