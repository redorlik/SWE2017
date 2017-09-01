from RLE import encode

def test_encode():
    assert encode('kkkkkbbbb') == '5k4b'

def test_encode_empty():
    assert encode('') == ''

def test_encode_emoji():
    assert encode('😇') == '1😇'
    assert encode('😇😇😇😇😇') == '5😇'
