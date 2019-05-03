from itertools import groupby


def is_string_reducible(source):
    tokens = [''.join(g) for _, g in groupby(source)]
    for i in range(len(tokens)):
        if len(tokens[i]) > 1:
            reduced_source = ''.join([x for j, x in enumerate(tokens) if j != i])
            if not reduced_source or is_string_reducible(reduced_source):
                return True
    return False

