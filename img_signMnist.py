import sys
import os
import pandas as pd
import numpy as np
import scipy.misc

path_dataset = sys.argv[1]
output_dir = 'hands'

train = pd.read_csv(path_dataset+'/sign_mnist_train.csv')
test = pd.read_csv(path_dataset+'/sign_mnist_test.csv')

train.drop('label', axis = 1, inplace = True)
test.drop('label', axis = 1, inplace = True)

x_train = train.values
x_test = test.values
x_train = x_train.reshape(x_train.shape[0], 28, 28)
x_train = x_test.reshape(x_test.shape[0], 28, 28)

if not os.path.exists(output_dir):
  os.makedirs(output_dir)

i = 1
for elem in x_train:
  print(i)
  scipy.misc.imsave('hands/'+str(i)+'.jpg', elem)
  i += 1
  
for elem in x_test:
  print(i)
  scipy.misc.imsave('hands/'+str(i)+'.jpg', elem)
  i += 1


