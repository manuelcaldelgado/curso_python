__author__ = 'Manuel C. D.'



def f(a,b,**x):
    print(a,b,x)
d = {'b':'append', 'a':'block','x':'extract','x':'yes'}
dd = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)
f(**dd)
