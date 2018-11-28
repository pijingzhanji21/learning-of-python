import os
def file_size(fname):   #该函数传入一个fname
    return os.stat(fname).st_size    #返回该文件的大小

ll=[]
def file_list(path = None):
    for root,dir,file in os.walk(path):
        for f in file:
            ll.append(os.path.join(root,f))
    return ll      #此句为file_list的测试语句

def total_size(path = None):    #计算总计大小
    '''if path == None:
        path = os.getcwd()
    os.chdir(path)'''
    total = 0
    for name in file_list(path):  #从file_lsit函数中获取到各个文件
        total = total + file_size(name)   #使用file_size函数计算各个文件的大小，并求和
    return total   #返回计算后的总计大小
if __name__=='__main__':
    print(total_size(os.getcwd()))  #调用核心函数
    print(os.getcwd())