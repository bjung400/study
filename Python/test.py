iterable, visited = [1, 2, 3, 4, 5], [False] * 5

def get_permutation( _currentindex, _permutation):
    if _currentindex == 5:
        print(_permutation)
        return

    for index, value in enumerate(iterable):
        if not visited[index]:
            visited[index], _permutation[_currentindex] = True, value
            get_permutation(_currentindex + 1, _permutation)
            visited[index] = False

if __name__ == '__main__':
    get_permutation(0, [None] * 5)

import itertools

iterable = [1, 2, 3, 4, 5]
result = itertools.permutations(iterable)
for permutation in result:
    print(list(permutation))
    