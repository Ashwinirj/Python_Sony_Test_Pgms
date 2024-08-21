def fetch_nos():
    try:
        for i in range(10):
            yield i
    except StopIteration:
        print("Finished Yielding")


mynos = fetch_nos()
print(next(mynos))
print(next(mynos))
print(next(mynos))