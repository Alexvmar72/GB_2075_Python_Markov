import os


def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
        for el in lst_fold:
            el = os.path.join(name, el)
            os.mkdir(el)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fold_main = os.path.join(BASE_DIR, 'my_project')
lst_fold = ['settings', 'mainapp', 'adminapp', 'authapp']
create_folder(fold_main)