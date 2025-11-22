import functools

#Exercitiul1
def create_dict(lista) :
    rez = {}
    for key, value in lista :
        if key in rez :
            rez[key] += value
        else :
            rez[key] = value
    return rez
print(create_dict([('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]))

#Exercitiul2
def dict_liste(lista) :
    rez = {}
    for sir in lista :
        for char in sir :
            if char in rez :
                rez[char] += 1
            else :
                rez[char] = 1
    return rez
print(dict_liste(["aaa", "bbb", "aabbb"]))

#Exercitiul3
def my_filter(dictionar) :
    def functie(acc,elem) :
        key, value = elem
        if(lambda x : x>=5)(value) :
            acc[key] = value
        return acc
    return functools.reduce(functie, dictionar.items(), {})
dictionar1 = {'a': 5, 'b': 7, 'c': 1}
print(my_filter(dictionar1))

#Exercitiul4
def exists(dictionar2) :
    def functie2(acc, elem) :
        key, value = elem
        if((lambda x : x>=5)(value)) :
            acc = True
        return acc
    return functools.reduce(functie2,dictionar2.items(), {})
dict2 = {'a': 5, 'b': 7, 'c': 1}
print(exists(dict2))

def for_all(dictionar3) :
    def functie3(acc, elem) :
        key, value = elem
        return acc and (value >= 5)
    return functools.reduce(functie3,dictionar3.items(), True)
dict3 = {'a': 5, 'b': 7, 'c': 1}
print(for_all(dict3))

#Exercitiul5
def my_map(dictionar4, functie4) :
    def f(acc, elem) :
        key, value = elem
        acc[key] = functie4(value)
        return acc

    return functools.reduce(f, dictionar4.items(), {})
dict4 = {'a': 5, 'b': 7, 'c': 11}
print(my_map(dict4, lambda x:x+1))

#Exercitiul6
def multime_siruri_intregi(dictionar5, lista, multime = set()) :
    if(lista == []) :
        return multime
    else :
        if(lista[0] in dictionar5) :
            multime.add(dictionar5[lista[0]])
    return multime_siruri_intregi(dictionar5, lista[1:], multime)
print(multime_siruri_intregi({'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']))

#Exericitul7
def maxim(g, dictionar6) :
    def f(acc, elem) :
        key, value = elem
        acc = max(acc, g(key,value))
        return acc
    return functools.reduce(f,dictionar6.items(),0)
def k(key, value) :
    return value + 1
print(maxim(k,dict4))