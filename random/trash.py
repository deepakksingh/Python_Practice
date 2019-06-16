# import os
# import shutil


# #pathToEdit = '/ssd_scratch/cvit/dksingh/cityscapes/leftImg8bit/val/lindau/lindau_000006_000019_leftImg8bit.png'
# pathToEdit = '/home/deepak/Desktop/trash/trash3/val/lindau/prediction_44_2.png'


# print("before: ",pathToEdit)
# splitPath = pathToEdit.split('/')
# splitPath[-3] = 'train'
# trainDirPath = splitPath[0:-1]
# trainDirPath = "/{0}".format(os.path.join(*trainDirPath))
# print('after:  ',trainDirPath)

# #create the directory in training directory location
# os.makedirs(trainDirPath, exist_ok=True)

# #move the file from val to training directory location
# shutil.move(pathToEdit,trainDirPath)








def mutiply(*args):
    temp = 1
    for num in args:
        temp = temp*num
    return temp


a = [1,2,3,4,5]
res = mutiply(*a)
print(res)


def print_kwargs(**kwargs):
    for key,val in kwargs.items():
        print("The value of {} is {}".format(key,val))
        print("The type of {} is {}".format(key,type(key)))
        print("The type of {} is {}".format(val,type(val)))
        print("---")

print_kwargs(kw2=1,kw1=2.3,kw3=True,kw4='hello')

print(r"\
this\
        is a test\
                    message\
")