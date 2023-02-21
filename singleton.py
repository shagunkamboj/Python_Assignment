# #the __new__ method is defined as a static method which requires to pass a parameter cls.
# class Singleton:
#     #_instance = "object"
#     def __new__(cls, *args, **kwargs):#__new__ method will be called when an object is created 
#         if not hasattr(Singleton, '_instance'):#True
#             cls._instance = super().__new__(cls,*args, **kwargs)
#         return cls._instance
    
# a = Singleton()
# a.data1 = "object"
# print(a.data1)
# b = Singleton()
# print(b.data1)
# # a = Singleton("object")
# # print(a)

class A(object):
	def __new__(cls):
		print("Creating instance")
		return super(A, cls).__new__(cls)

	def __init__(self):
		print("Init is called")

A()#firstly __new__ method is called and then __init__method is called


class _Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance
        else:
            raise Exception("exception raised")
a = _Singleton()
a.data = "value"
print(a.data)
b = _Singleton()
print(b.data)