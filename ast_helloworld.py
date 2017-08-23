import ast
import os

obj = ast.AST()
path = os.path.join("/home", "bigbasket", "Desktop", "SqlMigrations_Automation", "helloworld.py")
file = open(path, "r")
parsed_object = ast.parse(file.read())


print parsed_object.body[0].body[1].body[1]
