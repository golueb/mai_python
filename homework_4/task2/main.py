import itertools

def infinit_gen(): #бесконечный генератор чисел
    return itertools.count(0, 2)

def func_iter(): #Применение функций к каждому элементу в итераторе.
    def func(a,b):
        return a+2*b
    #try:
    l1=itertools.starmap(func,[(0,2),(1,5),(2,10)])
    print(list(l1))
    #except TypeError:
    #    print('ошибка в пункте 2')


def chain_iter(): #Объединение нескольких итераторов в один
    list_a = [1, 22]
    list_b = [7, 20]
    list_c = [3, 70]
    print(list(itertools.chain(list_a, list_b, list_c)))


try:
    print('\nпункт 1')
    for i in infinit_gen():#infinit_gen():
        print(i, end=" ")  # 0 2 4 6 8 10 12 14 16 18
        if i>100:
            break

    print('\nпункт 2')
    func_iter()
    print('\nпункт 3')
    chain_iter()
except TypeError:
    pass