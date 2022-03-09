import os
import shutil


def renam_dir(initial, ultimate, sample):
    BASE_DIR = os.path.join(os.path.dirname(__file__), initial)
    NEW_DIR = os.path.join(os.path.dirname(__file__), initial, ultimate)

    if not os.path.exists(NEW_DIR):
        os.mkdir(NEW_DIR)

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if sample in file:
                lst_dir = root.split('\\')
                name_dir = str(lst_dir[-1])
                dir_temp = os.path.join(os.path.dirname(__file__), initial, ultimate, name_dir)
                if not os.path.exists(dir_temp):
                    os.mkdir(dir_temp)
                os.chdir(dir_temp)
                if not os.path.exists(file):
                    os.chdir(root)
                    shutil.copy(file, dir_temp)

if __name__ == '__main__':
    renam_dir('my_project', 'templates', '.html')

