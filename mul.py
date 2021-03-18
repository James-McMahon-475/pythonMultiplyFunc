def multiply(u, v):

    try:
        i = int(u)
        j = int(v)

        out = int(i) * int(j)
        error = "false"
    except ValueError:
        out = "NaN"
        error = "true"

    return out, error