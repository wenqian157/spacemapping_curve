# from spacemapping_curve.quadtree import *

# def test(arg, args):

#     for arg in args:
#         print('arg is {0}'.format(arg))

# list = [1, 2, 3, 4]
# test('a', list)

# def test(args, kwargs):
#     for arg in args:
#         print('arg is {0}'.format(arg))
#     for key in kwargs:
#         print('arg is {0}: {1}'.format(key, kwargs[key]))

# list = [1, 2, 3, 4]

# dic = {'a':1, 'b':2, 'c':3}
# test(list, dic)

def foo(*args, **kwargs):
    for item in args:
        print('{0} in args'.format(item))
    for k, v in kwargs.items():
        print('{0}: {1} in kwargs'.format(k, v))

foo(1,2,3,4,a=1,b=3)
# list1 = ['a', 'b', 'c', 3]
# for i, a in enumerate(list1[1:]):
#     print('test', i, a)
# list1 = [0,2,3,4,1]
# print(list1.index(2))

# for i in range(10):
#     if i == 4:
#         continue 
#     print(i)
# a = 1
# b = 2

# a, b = b, a
# print(a)