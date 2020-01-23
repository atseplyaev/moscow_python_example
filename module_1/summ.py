
def get_summ(one, two, delimiter='&'):
    return "{}{}{}".format(one, delimiter, two)

print(get_summ("Learn", "python"))
print(get_summ("Learn", "python").upper())