class Dummy(object):
    def __init__(self):
        self.dummy_attr_1 = 5

    def __getattribute__(self,attr):
        __dict__ = super(Dummy, self).__getattribute__('__dict__')
        if attr in __dict__:
            """if the attribute belongs to the class then return its value."""
            return super(Dummy, self).__getattribute__(attr)
        else:
            """if the attribute doesnt belong to the class then do the 
            following action."""
            return attr.upper()


d = Dummy()
d.does_not_exist
d.what_about_this_one

d.value = "Python"
print(d.value)
print(d.dummy_attr_1)