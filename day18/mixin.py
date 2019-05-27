
class MyDict(object):
    __slots__ = ('a', 'b', 'c')

    def __init__(self):
        self._dict = {}

    def set(self, key, value):
        self._dict[key] = value

    def __setattr__(self, name, value):
        if hasattr(self, '_dict'):
            self._dict[name] = value
        return super().__setattr__(name, value)


class SetOnceAttrMixin(object):
    # TypeError: multiple bases have instance lay-out conflict
    # __slots__= ('a','b')
    def set(self, key, value):
        if key == 'error':
            self._dict['ERROR']='ERROR!!!'
            raise KeyError('key is error')
        return super().set(key, value)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise KeyError(str(name) + ' is already set')

        return super().__setattr__(name, value)


class SetOnceMyDict(SetOnceAttrMixin, MyDict):
    pass


class SetOnceKeyMixin(object):
    # __slots__=()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' is already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceKeyMixin, dict):
    pass


if __name__ == '__main__':
    d = SetOnceMyDict()
    # d = MyDict()
    d.set('err', 1)
    try:
        d.set('error', 1)  # error
    except KeyError as e:
        print('catch you!', e)

    d.a = 1
    d.b = 2
    d.c = 3
    d.d = 4
    try:
        d.a = 5  # error
    except KeyError as e:
        print('catch you!', e)
        print(d._dict)
    # d = SetOnceDict()
    # d['a']=1
    # d['b']=2
    # d['c']=3
    # d['a']=4
