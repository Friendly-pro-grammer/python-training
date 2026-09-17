import time
def logger(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        try:
            print("Function name:",func.__name__)
            print("Arguments:",args,kwargs)
            
            result = func(*args,*kwargs)
            
            print(f"Return value:{result}")
            print("Status:SUCCESS")
            return result
            
           
        except Exception as e:
            print("STATUS:FAILED")
            print(e)
            raise
        finally:
            end=time.time()
            print(f"Execution time: {end-start:.8f}")
            if(end-start>2):
                print("Warning Takes longer")
            
    return wrapper
