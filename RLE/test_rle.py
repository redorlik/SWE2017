from RLE import encode,decode
from pytest import raises

def test_encode():
    assert encode('kkkkkbbbb') == [(5,'k'),(4,'b')]

def test_encode_empty():
    assert encode('') == ''

def test_encode_emoji():
    assert encode('😇') == [(1,'😇')]
    assert encode('😇😇😇😇😇') == [(5,'😇')]

def test_exeption():
    with raises(TypeError):
        encode(111)

def test_decode():
    assert decode('4k') == 'kkkk'
    assert decode('4k3b') == 'kkkkbbb'
    assert decode('4😇') == '😇😇😇😇'
    assert decode('10æ') == 'ææææææææææ'

def test_decode_empty():
    assert decode('') == ''

def test_decode_error():
    assert decode('1') == ''
#    assert decode('4k-----10æ') == ''
