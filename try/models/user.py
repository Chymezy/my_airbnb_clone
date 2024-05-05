#!/bin/bash/python3

from models.base_model import BaseModel

''' this contains the user model '''

class User(BaseModel):
    ''' class attributs '''
    email = " "
    password = " "
    first_name = " "
    last_name = " "