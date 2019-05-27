
from threading import Lock

class Singleton(type):
    def __init__(cls, *args, **kwargs):
        print('singleton init')
        cls._lock = Lock()
        cls._instance = None
        super().__init__(*args, **kwargs)
        print('singleton init finish')

    def __new__(cls, name,bases,attrs):
        print('singleton new')
        print('singleton new finish')

        return  super(Singleton,cls).__new__(cls,name,bases,attrs)

    def __call__(cls, *args, **kwargs):
        print('singleton call')

        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        print('singleton call finish')        
        return cls._instance

class Foo(metaclass=Singleton):
    pass

def main():
    print(id(Foo()))
    print(id(Foo()))

if __name__ == '__main__':
    main()
    

    
