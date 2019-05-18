def get_summ(one, two, delimiter="&"):
    a = (one + delimiter + two)
    sentence = a.upper()
    return sentence


print(get_summ("learn", "python"))
