

# Formula:
# (k1 * var + k2) mod (possible_vars) + n, n = 0 or n = 1
you_var = 12
k1 = [i for i in range(2,6)]
k2 = [i for i in range(1,6)]
possible_vars = [27, 18]
k1k2 = False  # True False
show_pr = True # True False

def get_variant_by_number(v = you_var, k1 = 3, k2 = 5, pos_var = 10, show_pr = show_pr):

    # (k1 * var + k2) mod (possible_vars) + n, n = 0 or n = 1
    vr = (k1* v + k2) % pos_var

    if show_pr:
        print(f'  ({k1}*{v} + {k2}) % {pos_var}', vr,sep = ' = ')
    return vr

def all_war(var=you_var, k1=k1, k2=k2, posibble_var = possible_vars):
    all_w = []

    print('Формула: (k1 * var + k2) mod (possible_vars) + n, n = 0 or n = 1')
    print(f"Ваш номер по списку: {var}")
    print(f'Значения параметра k1: {k1}')
    print(f'Значения параметра k2: {k2}')
    print(f'Максимальное число вариантов: {possible_vars}')
    print(f'Равные коэфиценты k1k2 возможны?: {k1k2}')
    print(f'Показывать действия?: {show_pr}')


    # k1*v+k2 & pos_var
    for i in posibble_var:
        print(f'\nДля максимального числа вариантов {i}')
        all_w.append([str(i)])

        va = set()
        for ki in k1:
            for kj in k2:
                if ki == kj and k1k2:
                    continue

                # (k1 * var + k2) mod (possible_vars) + n, n = 0 or n = 1
                vr = get_variant_by_number(var, ki, kj, i)

                # n = 0
                va.add(vr)
                # n = 1
                va.add(vr+1)

        print(f'Возможные варианты: {va}')
        all_w[-1].append(va)

    return all_w

w = all_war()
#print(*w, sep ='\n')


