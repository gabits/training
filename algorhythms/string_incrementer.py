def increment_string(strng):
    slist = list(strng)
    for a in range(len(slist)):
        if strng[a] in '0123456789':
            change = [str(int(''.join(slist[a:])) + 1)]
            while len(change) < len(slist[a:]):
                change.insert(0, '0')
            return ''.join(slist[:a]) + ''.join(change)
    return strng + '1'


increment_string("foobar099")
