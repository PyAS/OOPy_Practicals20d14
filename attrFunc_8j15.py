Created on 08-Jan-2015

@author: pavan
'''
from string import upper

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self,*args):
        '''
        pass
        '''
        super(MyClass,self).__setattr__('a',args[0])
        super(MyClass,self).__setattr__('b',args[1])
        
        
        
        
    def __setattr__(self,name,value):
        raise Exception
        
    def __getattribute__(self,name):
        if name.starts_with('__'):raise Exception
        #return super(MyClass,self).__setattr__()
    

a=MyClass(10,20)

object.__setattr__(a,'c',30)

a.__dict__['d']=40


print a.d