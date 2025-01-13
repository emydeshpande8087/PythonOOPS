class MyCustomClass:
  def __init__(self):
    self.name='test'
    self.last_name='tester'
    self.directory='etc'

  def ObjectToDict(self):
    '''Converts MyCustomClass object to a dictionary.'''
    #vars(self) will give all the attributes present in the class.
    #getattr(self,attr) will give the value of the attribute of the class refered by "self".
    #lastly using dictionary comprehension will give the dictionary representation of the class's attribute sand values
    return {attr: getattr(self, attr) for attr in vars(self)}


#How to use ? 
#create your class object.
obj=MyCustomClass()
print('Type of class is',type(obj))
#get a dict representation 

data=obj.ObjectToDict()
print('Type of data variable  is',type(obj)) # this will be dictionary
