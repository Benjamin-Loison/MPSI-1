iteration = 0
size = 7

while iteration <= size:
    if iteration <= size // 2:
        print('* ' * iteration + '#' + ' *' * (size - 2 - 2 * iteration) + ' #' + ' *' * iteration)
    else:
        print('* ' * (size - iteration) + '#' + ' *' * (2 * iteration - size - 2) + ' #' + ' *' * (size - iteration))
    iteration += 1