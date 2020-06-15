
# def capital_case(x):
#     return chr(ord(x) - ord('a') + ord('A'))
#
# def setup_module(module): #before tests
#     return module
#
# def test_capital_case():
#     assert len(setup_module("Start")) == 5
#     assert capital_case('a') == 'A'
#     assert capital_case('x') == 'X'
#     assert capital_case('z') == 'Z'
#
# def teardown_module(module): # after tests
#     return module
#
# def test_capital_case2():
#     assert capital_case('9') == '9'
#     assert capital_case('(') == '('
#     assert capital_case('#') == '#'

##############################################################


from PasswordGenerator import *
import re

# Write Tests cases to test foreign code
# Code adapted from: http://pythonfiddle.com/generate-random-password/
# • random_password_generator.py is provided in Github
# • It generates random password with following rules:
# 1. 6-20 characters
# 2. at least one uppercase character
# 3. at least one lowercase character
# 4. at least one digit
# 5. at least one special character (!, @, #, $, %, ^, &, *) 6. no more than 2 characters repeating consecutively
# Make appropriate use of @pytest.mark.parametrize


def test_length_pw():
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    assert len(pw) >= 6 and len(pw) <= 20

def test_upper_case_pw():
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    # match = re.findall(r'[A-Z]', pw)
    # assert match != None
    assert any(x.isupper() for x in pw)

def test_lower_case_pw():
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    assert any(x.islower() for x in pw)

def test_digit_pw():
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    assert any(x.isdigit() for x in pw)

def test_one_special_character_pw():
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    match = re.findall(r'[!@#$%^&*]', pw)
    # print(match)
    assert match


# @pytest.mark.parametrize ('par', ["!", "@", "#", "$", "%", "^", "&", "*"])
# def test_one_special_character_pw1(par):
#     pw = generate_random_password(random.randint(6, 30), SEQUENCE)
#     assert (any(set(pw).intersection(set(par))))

def test_repeat_two_char_pw():
    new_str = ""
    pw = generate_random_password(random.randint(6, 30), SEQUENCE)
    for i, ch in enumerate(pw):
        if len(pw) < i+1:
            if ch == pw[i+1]:
                new_str += str(ch)
    assert new_str == ""