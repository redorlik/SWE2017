from RLE import encode

def test_encode():
    assert encode('kkkkkbbbb') == '5k4b'
