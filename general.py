import os


def mkdir(path):
    if os.path.exists(path):
        if not os.isdir(os.path.exists):
            os.mkdir(path)
    else:
        os.mkdir(path)

