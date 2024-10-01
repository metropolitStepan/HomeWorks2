def final_pairs():

    boys = []
    while True:
        name = input('Введите имя мужчины или "стоп", если хотите завершить ввод: ')
        if name == 'стоп':
            break
        boys.append(name)
    girls = []
    while True:
        name = input('Введите имя девушки или "стоп", если хотите завершить ввод:')
        if name == 'стоп':
            break
        girls.append(name)

    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)

    if len(sorted_boys) != len(sorted_girls):
        return'К сожалению, пара найдется не всем'
    pairs = 'идеальные пары:\n'
    for i in range(len(sorted_boys)):
        pairs += f'{sorted_boys[i]} и {sorted_girls[i]}\n'

    return pairs

result = final_pairs()
print(result)