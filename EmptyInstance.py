class MyCustomClass:
    def __init__(self):
        self.name='test'
        self.last_name='tester'
        self.directory='etc'
    
    @classmethod
    def getEmptyInstance(cls):
        #create a empty object of this class and then fill up the attributes as you wish.
        instance=cls.__new__(cls)
        return instance

#create a object of this class the normal way.
obj=MyCustomClass()
emptyObj=MyCustomClass.getEmptyInstance() # get empty object
emptyObj.schoolname='yourname'
