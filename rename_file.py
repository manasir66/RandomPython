import os
#import the os module

#index is used to rename file in numerical order 
#file is the full name of the orginial files

for index, file in enumerate(os.listdir()):

    file_name, file_extension = os.path.splitext(file)
    
    print(file) #old file
    
    number = str(index+1)
    
    #the {}{} allows us to place values respectively 
    
    new_name = '{}{}'.format(number, file_extension)
    os.rename(file, new_name)
    
    print(file) #new renamed file
