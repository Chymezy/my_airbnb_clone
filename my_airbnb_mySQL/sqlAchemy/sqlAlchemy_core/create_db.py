from connect import create_connection
from tables import users_table, comments_table, metadata


print(">>> CREATE DATABASE <<<")
metadata.create_all(bind=create_connection())