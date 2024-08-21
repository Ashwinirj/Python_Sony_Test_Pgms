def func1():
    try:
        dict1 = {"IN": "India", "US": "United States"}
        del dict1["IN"]
        value =100 
        print(value)
        print(dict1)
    except ZeroDivisionError:
        print("QW", end=" ")
        vlaue = int(dict1[0])
    except KeyError:
        print("DE", end=" ")
    finally:
        print("FTI", end=" ")

try:
    func1()
    print("CR")
except:
    print("PA")