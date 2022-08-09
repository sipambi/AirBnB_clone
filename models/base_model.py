#usr/bin/python3
"""
    Docstring for my project
"""
    
from uuid import uuid4
import datetime
import models

class BaseModel:
    """ 
        Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            BaseModel Constructor
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
            
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """
            Return string of info about model
        """
        return ('[] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))
    
    def __repr__(self): 
        """
            Returns string representation
        """
        return (self.__str__)
    
    def save(self):
        """
            updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now
        models.storage.save()
        
    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of the dict instance
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic