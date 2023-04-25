def sanitize(time):
    if '-' in time:
        splitter = "-"
    elif ':' in time:
        splitter = ":"
    else:
        return time
    (min,sec) = time.split(splitter,1)
    return(min + '.' + sec)
