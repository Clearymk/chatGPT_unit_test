import os

question = "Generate java unit test code for the following code, \"{}\""

project_name = "commons-io"


def get_chat_gpt_result(source_code):
    return ""


for code_dir in os.listdir(project_name):
    for code_file in os.listdir(os.path.join(project_name, code_dir)):
        if code_file.endswith("Test.java"):
            continue
        code = ""
        with open(os.path.join(project_name, code_dir, code_file), "r", encoding="utf8") as f:
            for _ in f.readlines():
                code += _

        print(question.format(code))
        # TODO 得到ChatGPT的结果
        result = get_chat_gpt_result(code)

        with open(os.path.join(project_name, "chatgpt_" + code_file[:-5])) as f:
            f.write(result)
        break
