import numpy as np
import math

def normalize_1d_array(arr):
    mydim = np.shape(arr)
    if mydim[0] ==1:
        mymean = arr.mean(axis = 1)
        mystd = arr.std(axis = 1)
        return (arr - mymean)/ mystd
    elif mydim[1] == 1:
        mymean = arr.mean(axis = 0)
        mystd = arr.std(axis = 0)
        return (arr - mymean)/ mystd
    else:
        return None
    #return((arr -arr.mean())/arr.std())

def normalize_2d_array(arr):
    return((arr -arr.mean(axis = 0))/arr.std(axis = 0))

def create_matrix(num_rows,num_cols,fill_value):
    return np.ones((num_rows,num_cols)) * fill_value

def my_matrix_operations(arr,value,operator):
    if operator == '+':
        return arr + value
    if operator == '*':
        return arr * value
    if operator == '-':
        return arr - value
    if operator == '/':
        return arr / value
    if operator == '%':
        return arr % value
    if operator == '//':
        return arr // value

def create_1D_random_array(value):
    return np.random.random(size = (value))

def create_2D_random_array(row_count,col_count):
    return np.random.random(size = (row_count,col_count))

def array_random_sample(arr,value):
    return np.random.choice(arr,value)

def reaplace_max_element_in_array(arr):
    idx = np.argmax(arr)
    arr[idx] = 0
    return arr

def create_new_random_1D_array(value):
    newarr = np.arange(value+1)
    return newarr.sum()

def my_matrix_operations_2(arr,arr2):
    mydim = np.shape(arr)
    mydim2 = np.shape(arr2)
    if mydim[1] == mydim2[0]:
        #return arr @ arr2
        return np.dot(arr,arr2)
    return None

def my_matrix_element_multiply(arr,arr2):
    mydim = np.shape(arr)
    mydim2 = np.shape(arr2)
    if mydim == mydim2:
        #return arr @ arr2
        return arr * arr2
    return None

def return_top5_array(arr):
    idx = (-arr).argsort()[:5]
    return arr[idx]

def return_bottom5_columnwise_array(arr):
    newarr = np.sort(arr,axis=0)
    return newarr[:5]

def ec(value):
    n = math.floor(math.sqrt(value))
    value = n **2
    newarr = np.arange(value).reshape(n,n)
    mymeans = np.mean(newarr,axis=0)
    mysums = np.sum(mymeans)
    return mysums

#oneDtestarr = np.array([1,6,3,4,7,2,9,1,3,2,7,1,9,32])
#testarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#testarr = np.random.randint(9,size = (1,10))
#print(testarr)
#print(create_matrix(50,3,5))
#print(my_matrix_operations(oneDtestarr,3,'-'))
#print(create_1D_random_array(40))
#print(create_2D_random_array(9,4))
#print(array_random_sample(oneDtestarr,4))
#print(oneDtestarr)
#print(reaplace_max_element_in_array(oneDtestarr))
#print(create_new_random_1D_array(4))
#arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#arr2 = np.array([[1,2,3],[5,6,7],[9,10,11],[1,2,3]])
#print(my_matrix_operations_2(arr,arr2))
#arr = np.array([[1,7,3],[2,6,1],[1,3,5],[7,4,2],[2,6,8],[9,3,2],[6,1,7]])
#arr2 = np.array([[1,2,3],[5,6,7],[9,10,11]])
#print(my_matrix_element_multiply(arr,arr2))
#print(return_top5_array(oneDtestarr))
#print(return_bottom5_columnwise_array(arr))
print(ec(147))
#from pprint import pprint

#myarray = np.random.randint(7,size = 10)
#myarray2 = np.random.randint(7,size = (2,3)) #([[1,2],[3,4]])
#X = np.zeros([3,4])
#Y = np.ones([34])
#print(myarray)
#print(myarray2)
#pprint(Y)
'''
columnheaders = np.array([['Gene name','4h','12h','24h','48h']])
genelist = np.array([['A2M','FOS','BRCA2','CPOX']])
values0  = np.array([[0.12,0.08,0.06,0.02]])
values1  = np.array([[0.01,0.07,0.11,0.09]])
values2  = np.array([[0.03,0.04,0.04,0.02]])
values3  = np.array([[0.05,0.09,0.11,0.14]])

myarr = np.vstack((values0,values1,values2,values3))
meanpergene = myarr.mean(axis=1)
meanpertime = myarr.mean(axis=0)
print(myarr)
print(meanpergene)
print(meanpertime)
print(np.amax(myarr))
'''
#print(np.identity(4))
