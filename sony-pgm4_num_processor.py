import sys 

def num_processor(func):
    def wrapper(*args, **kwargs):
        val =func(*args)
        try:
            return val+int(sys.argv[2])
        finally:
            return val+int(sys.argv[1])
        return wrapper
    
    @num_processor
    def calc_sum(num1, num2):
        return num1+num2
    
    print(calc_sum(7,8))

