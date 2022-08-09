#!/usr/bin/python3
# Update models/__init__.py 2 create unique FileStorage instnce 4 yo applcation
# import file_storage.py,create  variable storage, an instance of FileStorage
# call reload() method on this variable
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
