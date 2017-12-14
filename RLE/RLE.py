# Runlength encoder: onvert 'kkkbbbb' til [(3,'k'),(4,'b')]

def encode(mess):
    if not mess:
        return ''
    old = mess[0]
    i = 1
    res = []

    for c in mess[1:]:
        if c != old:
            res.append((i,old))
            i = 1
            old = c
        else:
            i += 1
    res.append((i,old))

    return res

def decode(mess):
    res = [i*c for i,c in mess]
    return ''.join(res)
