import os
from chat_api import ask
from database import DataBase

question = "Generate java unit test code for the following code, \"{}\""
db = DataBase()

for task in db.query_task():
    code_path = task[2]
    code = ""
    source_file_name = code_path.split("/")[-1]
    source_class_name = code_path.split("/")[-2]

    with open(code_path, "r", encoding="utf8") as f:
        for _ in f.readlines():
            code += _

    result = ask(question.format(code))
    print(result)

    if result != "too many tokens":
        with open(os.path.join(code_path.replace(source_file_name, ""),
                               "chatgpt_" + source_class_name + "Test.java"), "w", encoding="utf8") as f:
            f.write(result)
        break
