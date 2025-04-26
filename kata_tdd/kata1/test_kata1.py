import sys
sys.path.append(".") 
from kata_tdd.kata1.kata1 import validar_password

def test_validar_password_longitud():
    assert validar_password("abc") == False 
    assert validar_password("abcdefgh") == True
    

def test_validar_password_compleja():
    assert validar_password("Abcdefg1") == True 
    assert validar_password("abcdefgh") == False 