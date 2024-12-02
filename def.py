
def func(text,*args):
    print(text, end="")
    for i in args:
        print(i, ' ==> ', type(i), end = ' | ')
       
func('List is : ', 1, 'Mostapha', True, 1.33)

print('-'*30)
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
