#!/usr/bin/python3


import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for other classes, defines common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    settattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_instances = self.__dict__.copy()
        dict_instances['__class__'] = self.__class__.__name__
        dict_instances['created_at'] = self.created_at.isoformat()
        dict_instances['updated_at'] = self.updated_at.isoformat()

        return dict_instances


