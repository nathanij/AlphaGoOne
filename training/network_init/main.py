import os


dir_path = '<insert path here>'
for name in os.listdir(dir_path):
    if name.endswith('.sgf'):
        fname = os.path.join(dir_path, name)
        with open(fname) as f:
            