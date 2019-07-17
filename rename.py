import os

for files in os.listdir():
    print(files)
    f_name, f_ext = os.path.splitext(files)

    to_add = 'ax'
    f_new_name = '{}{}{}'.format(to_add, f_name, f_ext) 
    os.rename(files, f_new_name)

    print(files)
    print("\n")