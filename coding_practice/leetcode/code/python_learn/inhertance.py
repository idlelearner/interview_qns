class BaseClass: pass
class SubClass(BaseClass): pass

if __name__=='__main__':
    print issubclass(SubClass, BaseClass)