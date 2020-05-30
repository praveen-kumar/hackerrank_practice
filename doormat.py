# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

def get_vals():
    height, width = map(int, input().split())
    assert height % 2 == 1  # Make sure to follow the constraints
    assert width == height * 3
    return height, width


def design_mat(design, text):
    h, w = get_vals()

    # Top
    pattern = [i for i in range(1, h, 2)]
    for i in pattern:
        yield '{}'.format(str(design * i)).center(w, '-')

    # Middle
    yield '{}'.format(text).center(w, '-')

    # Bottom
    pattern = list(reversed(pattern))
    for i in pattern:
        yield '{}'.format(str(design * i)).center(w, '-')


for line in design_mat('.|.', 'WELCOME'):
    print(line)
