def calculate(data, findall):
    matches = findall(r".*?([a-c])([\+\-]*)[=]([a-c]?)([\+\-]*\d*)") (r"([abc])([+-]?)=([abc])?([+-]?\d+)?")

    for VAR1, SIGN1, VAR2, NUM in matches:
        rside = data.get(VAR2, 0) + int(NUM or 0)
        if SIGN1:
            if SIGN1 == '+':
                data[VAR1] += rside
            elif SIGN1 == '-':
                data[VAR1] -= rside
        else:
            data[VAR1] = rside
    
    return data