import os
import shutil

for root, folders, files in os.walk('./exam/exam2017'):
    for file in files:
        if file.endswith('.txt'):
            path = os.path.join(root, file)
            shutil.move(path, './exam/exam2017')