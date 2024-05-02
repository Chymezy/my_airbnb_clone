#!/bin/bash/python3

from models.engine.file_storage import FileStorage

''' This linking between models and storage file '''
storage = FileStorage()
storage.reload()
