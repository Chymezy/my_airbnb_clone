#!/usr/bin/python3

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Call reload() method on the storage variable
storage.reload()
