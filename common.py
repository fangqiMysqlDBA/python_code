#!/usr/bin/python

def humanize_bytes(bytesize, precision=0):
    abbrevs = (
        (10**15, 'PB'),
        (10**12, 'TB'),
        (10**9, 'GB'),
        (10**6, 'MB'),
        (10**3, 'kB'),
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f%s' % (precision, round(float(bytesize) / factor), suffix)
