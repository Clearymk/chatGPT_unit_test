import os
import shutil

code_path = "C:\\Users\\10952\\Desktop\\commons-lang-master\\src"
project_name = "commons-lang"

source_codes = set()
test_codes = set()

for root, dirs, files in os.walk(os.path.join(code_path, "main")):
    for name in files:
        if name.endswith(".java"):
            source_codes.add(os.path.join(root, name))

for root, dirs, files in os.walk(os.path.join(code_path, "test")):
    for name in files:
        if name.endswith(".java"):
            test_codes.add(os.path.join(root, name))

for test_code in test_codes:
    test_name = test_code.split("\\")[-1][:-9]
    for source_code in source_codes:
        source_name = source_code.split("\\")[-1][:-5]
        if source_name.strip() == test_name.strip():
            if not os.path.exists(os.path.join(project_name, test_name)):
                os.mkdir(os.path.join(project_name, test_name))
            shutil.copy(test_code, os.path.join(project_name, test_name))
            shutil.copy(source_code, os.path.join(project_name, test_name))
