"""Anna Rogozin 323686477
   Maor Yatzkan 301791380"""

from math import sqrt


""""""""""""""""""""""""""""""""""""""""""""""""""""EX1.1_Point"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def make_class(attrs, base_class=None):
    """

    :param attrs: that is an dictionary of an point object
    :param base_class: is the class an object have inheritance from
    :return: return dispatch dictionary
    """
    '''Getter: class attribute (looks in this class, then base)'''
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base_class is not None:
            return base_class['get'](name)

    '''Setter: class attribute (always sets in this class)'''
    def set(name, value):
        attrs[name] = value

    '''Return a new initialized object instance (a dispatch dictionary)'''
    def new(*args):
            return init_instance(cls, *args)
    cls = { 'get': get, 'set': set, 'new': new }
    return cls


    ''' funcrion get dictionery of the class and an ardumants in our case the point'''
def init_instance(cls, *args):
	instance = make_instance(cls)
	init = cls['get']('__init__')
	if init:
	    init(instance, *args)
	return instance


def make_instance(cls):
	attributes = {}
	def get_value(name):
	    if name in attributes:
	        return attributes[name]
	    else:
	        value = cls['get'](name)
	        return bind_method(value, instance)
	def set_value(name, value):
	    attributes[name] = value
	instance = {'get': get_value, 'set': set_value}
	return instance


def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value


def make_Point_class():
    '''make point'''
    '''constructor'''
    def __init__(self,x=0,y=0):
        self['set']('x',x)
        self['set']('y',y)
    def setX(self,x):
        self['set']('x',x)
    def setY(self,y):
        self['set']('y',y)
    def getX(self):
        return self['get']('x')
    def getY(self):
        return self['get']('y')
    def str(self):
        '''return the point'''
        return (getX(self),getY(self))
    def distance(self,p2):
        '''return the distance between two points'''
        return sqrt((getX(self)-getX(p2))**2+(getY(self)-getY(p2))**2)

    attributes={'__init__': __init__,'setX': setX, 'setY':setY, 'getX': getX, 'getY': getY, 'str': str,'distance':distance}
    return make_class(attributes)



Point=make_Point_class()
p1 = Point['new'](4, 8)
print(p1['get']('str')())
p1['get']('setY')(3)
print(p1['get']('str')())
p2 = Point['new']()
print(p2['get']('str')())
p2['get']('setX')(4)
print(p2['get']('str')())
print(p1['get']('distance')(p2))


""""""""""""""""""""""""""""""""""""""""""""""""""""EX1.1_Line"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def make_Line_class():
    # make line class
    '''constructor'''

    def __init__(self):
        self['set']('p1', Point['new']())
        self['set']('p2', Point['new'](1, 1))

    def getPoint(self, num):

        if num == 1:
            return self['get']('p1')
        elif num == 2:
            return self['get']('p2')
        else:
            print("error")

    def setPoint(self, num, x, y):
        if num == 1:
            Point['get']('setX')(self['get']('p1'), x)
            Point['get']('setY')(self['get']('p1'), y)
        elif num == 2:
            Point['get']('setX')(self['get']('p2'), x)
            Point['get']('setY')(self['get']('p2'), y)
        else:
            print("error")

    def str(self):
        '''return straight equation and distance'''
        if (Point['get']('getX')(self['get']('p2')) == Point['get']('getX')(self['get']('p1'))):
            '''if x-x=0'''
            return "x={0}".format(Point['get']('getX')(self['get']('p2')))

        elif Point['get']('getY')(self['get']('p2')) == Point['get']('getY')(self['get']('p1')):
            '''if y-y=0'''
            return "y={0}".format(Point['get']('getY')(self['get']('p2')))

        else:
            a = (Point['get']('getY')(self['get']('p2')) - Point['get']('getY')(self['get']('p1'))) / (
                        Point['get']('getX')(self['get']('p2')) - Point['get']('getX')(self['get']('p1')))
            x = a * Point['get']('getX')(self['get']('p2'))
            x = Point['get']('getY')(self['get']('p2')) - x

            if x > 0:
                if a == 1:
                    return "y=x+{0}".format(x)
                else:
                    return "y={0}x+{1}".format(a, x)
            elif x == 0:
                return "y={0}x".format(a)
            else:
                if a == 1:
                    return "y=x{0}".format(x)
                else:
                    return "y={0}x{1}".format(a, x)

    '''function chaeck if the point on the line'''

    def isOnLine(self, p):
        if (Point['get']('getX')(self['get']('p2')) == Point['get']('getX')(self['get']('p1'))):
            if p['get']('getX')() == Point['get']('getX')(self['get']('p2')):
                return True
            else:
                return False
        elif (Point['get']('getY')(self['get']('p2')) == Point['get']('getY')(self['get']('p1'))):
            if p['get']('getY')() == Point['get']('getY')(self['get']('p2')):
                return True
            else:
                return False
        else:
            a = (Point['get']('getY')(self['get']('p2')) - Point['get']('getY')(self['get']('p1'))) / (
                        Point['get']('getX')(self['get']('p2')) - Point['get']('getX')(self['get']('p1')))
            x = a * Point['get']('getX')(self['get']('p2'))
            x = Point['get']('getY')(self['get']('p2')) - x
            flag = a * p['get']('getX')() + x
            if (p['get']('getY')() == flag):
                return True
            else:
                return False

    '''dictionary'''
    attributes = {'__init__': __init__, 'getPoint': getPoint, 'setPoint': setPoint, 'str': str, 'isOnLine': isOnLine}
    return make_class(attributes, Point)


Line = make_Line_class()
l1 = Line['new']()
l1['get']('setPoint')(1, 2, 3)
l1['get']('setPoint')(2, 8, 6)
l1['get']('str')()
p = l1['get']('getPoint')(1)
l1['get']('isOnLine')(p)


# Our custom OOP
def make_singleton_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    count = 0
    singleton = None

    # print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized object instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        nonlocal singleton
        if singleton is not None:
            return singleton
        else:
            obj = {'get': get, 'set': set}
            # calls constructor if present
            init = get('__init__')
            if init:
                nonlocal count
                if count == 0:
                    init(*args)
                    count = 1
            singleton = obj
            return singleton

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    return cls


def make_printerDriver_class():
    def __init__(self, nickname=""):
        self['set']('nickname', nickname)

    def str(self):
        print(self['get']('__str__')())

    def __str__(self):
        return self['get']('nickname')

    def activate(self, path):
        with open(path, 'r') as f:
            print(*f.readlines())

    return make_singleton_class(locals())


def driver_printer():
    driver1 = PrinterDriver['new']("hp")
    driver1['get']('str')()
    driver2 = PrinterDriver['new']("espon")
    driver2['get']('activate')("file.txt")


PrinterDriver = make_printerDriver_class()
driver_printer()


class WeightKG(object):
    def __init__(self, weight):
        self.weight = weight
        self.weight_kg = weight

    @property
    def weight_lb(self):
        return convertion_chart[('kg', 'lb')](self.weight)

    @property
    def weight_oz(self):
        return convertion_chart[('kg', 'oz')](self.weight)

    def __str__(self):
        return "%f kg" % self.weight

    def __add__(self, other):
        return add(self, other)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.weight})'


class WeightLB(object):
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight_kg(self):
        return convertion_chart[('lb', 'kg')](self.weight)

    @property
    def weight_oz(self):
        return convertion_chart[('lb', 'oz')](self.weight)

    def __str__(self):
        return "%f lb" % self.weight

    def __add__(self, other):
        return add(self, other)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.weight})'


class WeightOZ(object):
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight_kg(self):
        return convertion_chart[('oz', 'kg')](self.weight)

    @property
    def weight_lb(self):
        return convertion_chart[('oz', 'lb')](self.weight)

    def __add__(self, other):
        return add(self, other)

    def __str__(self):
        return "%f oz" % self.weight

    def __repr__(self):
        return f'{self.__class__.__name__}({self.weight})'


def add(w1, w2):
    """
    :param w21: weight in kg,lb or oz
    :param w22:  weight in kg,lb or oz
    :return:  the sum of weights in kg
    """
    return WeightKG(w1.weight + w2.weight)


def sub(w1, w2):
    """
    :param w1: weight in kg,lb or oz
    :param w2:  weight in kg,lb or oz
    :return:  the diff of weights in kg
    """
    return WeightKG(w1.weight_kg - w2.weight_kg)


types_tags = {WeightKG: 'kg', WeightOZ: 'oz', WeightLB: 'lb'}
convertion_chart = {('lb', 'kg'): lambda x: x / 2.2046226218,
                    ('oz', 'kg'): lambda x: x / 35.27396195,
                    ('kg', 'lb'): lambda x: x * 2.2046226218,
                    ('kg', 'oz'): lambda x: x * 35.27396195,
                    ('oz', 'lb'): lambda x: x / 35.27396195 * 2.2046226218,
                    ('lb', 'oz'): lambda x: x / 2.2046226218 * 35.27396195
                    }


def add_kg_lb(wkg, wlb):
    return wkg + wlb


def add_kg_oz(wkg, woz):
    return wkg + woz


def add_kg_kg(wkg1, wkg2):
    return wkg1 + wkg2


def add_lb_kg(wlb, wkg):
    return WeightLB(wlb.weight + wkg.weight_lb)


def add_lb_lb(wlb1, wlb2):
    return WeightLB(wlb1.weight + wlb2.weight)


def add_lb_oz(wlb, woz):
    return WeightLB(wlb.weight + woz.weight_lb)


def add_oz_oz(woz1, woz2):
    return WeightOZ(woz1.weight + woz2.weight)


def add_oz_kg(woz, wkg):
    return WeightOZ(woz.weight + wkg.weight_oz)


def add_oz_lb(woz, wlb):
    return WeightOZ(woz.weight, wlb.weight_oz)


def sub_kg_kg(wkg1, wkg2):
    return WeightKG(wkg1.weight - wkg2.weight)


def sub_kg_oz(wkg, woz):
    return WeightKG(wkg.weight - woz.weight_kg)


def sub_kg_lb(wkg, wlb):
    return WeightLB(wkg.weight - wlb.weight_kg)


def sub_lb_kg(wlb, wkg):
    return WeightLB(wlb.weight - wkg.weight_lb)


def sub_lb_lb(wlb1, wlb2):
    return WeightLB(wlb1.weight - wlb2.weight)


def sub_lb_oz(wlb, woz):
    return WeightLB(wlb.weight - woz.weight_lb)


def sub_oz_oz(woz1, woz2):
    return WeightOZ(woz1.weight - woz2.weight)


def sub_oz_lb(woz, wlb):
    return WeightOZ(woz.weight - wlb.weight_oz)


def sub_oz_kg(woz, wkg):
    return WeightOZ(woz.weight - wkg.weight_oz)


def apply(operator_name, w1, w2):
    tags = (types_tags.get(type(w1)), types_tags.get(type(w2)))
    key = (operator_name, tags)
    return apply.implementation[key](w1, w2)


apply.implementation = {
    ('add', ('kg', 'kg')): add_kg_kg,  # return kg
    ('add', ('kg', 'lb')): add_kg_lb,  # return kg
    ('add', ('kg', 'oz')): add_kg_oz,  # return kg
    ('add', ('lb', 'kg')): add_lb_kg,  # return lb
    ('add', ('lb', 'lb')): add_lb_lb,  # return lb
    ('add', ('lb', 'oz')): add_lb_oz,  # return lb
    ('add', ('oz', 'kg')): add_oz_kg,  # return oz
    ('add', ('oz', 'lb')): add_oz_lb,  # return oz
    ('add', ('oz', 'oz')): add_oz_oz,  # return oz

    ('sub', ('kg', 'lb')): sub_kg_lb,  # return kg
    ('sub', ('kg', 'kg')): sub_kg_kg,  # return kg
    ('sub', ('kg', 'oz')): sub_kg_oz,  # return kg
    ('sub', ('lb', 'kg')): sub_lb_kg,  # return lb
    ('sub', ('lb', 'lb')): sub_lb_lb,  # return lb
    ('sub', ('lb', 'oz')): sub_lb_oz,  # return lb
    ('sub', ('oz', 'kg')): sub_oz_kg,  # return oz
    ('sub', ('oz', 'oz')): sub_oz_oz,  # return oz
    ('sub', ('oz', 'lb')): sub_oz_lb  # return oz

}

w1 = WeightKG(12)
print(w1.__class__)
w2 = WeightLB(7)
print(w2)
w3 = WeightOZ(100)
print(w3)
print(w1 + w2)
print(w2 + w3)
print(apply('add', w1, w1))
print(apply('sub', w1, w2))
print(apply('add', w2, w3))
print(apply('sub', w3, w2))
code = input(">>")
eval(code)
