class myclass:
    def myfunc(city, city2 = 'Delhi'):
        print(city)
        print(city2)

o1=myclass()
#o1.myfunc('Chennai', 'Mumbai')  #output: TypeError myclass.myfunc() takes from 1 to 2 positional arguments but 3 were given
o1.myfunc()           #output: Delhi
o1.myfunc('Chennai')  #output: Chennai
