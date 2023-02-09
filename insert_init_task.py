import database
import os


project_name = "commons-text"
db = database.DataBase()

for _ in os.listdir(project_name):
    if _ == ".DS_Store":
        continue
    # print(os.path.exists(os.path.join(os.getcwd(), project_name, _, _ + ".java")))
    db.insert_task(_, os.path.join(os.getcwd(), project_name, _, _ + ".java"))
