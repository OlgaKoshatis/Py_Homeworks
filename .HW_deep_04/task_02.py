#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — хэш значения переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def fun_k_dict(**kwargs):
    return {v if v.__hash__ is not None else str(v) : k for k, v in kwargs.items()}

function(a=1, b=2)
{1: 'a', 2: 'b'}
function(a=1, b=[1,2])
{1: 'a', '[1, 2]': 'b'}
function(arg1="Hello",arg2=2,arg3="123",arg4=[1,2,3,4,5])
{'Hello': 'arg1', 2: 'arg2', '123': 'arg3', '[1, 2, 3, 4, 5]': 'arg4'}