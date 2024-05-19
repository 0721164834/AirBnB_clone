#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
Defines a BaseModel class for managing common attributes and methods.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class for other classes in the AirBnb clone project.
    Attributes;
        id (str): Unique identifier for each instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last.
    """

    def __init__(self):
        """
        Initializes a new instance of baseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the Public instance attribute 'updated_at' with the current         """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instances to dictionary reprentation.

        Returns:
            dict: dictionary cantaing all keys of the instance __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a strign represnation of the instance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
        )
