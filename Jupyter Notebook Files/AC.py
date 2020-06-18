# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:19:41 2019

@author: user
"""

import numpy as np
a = np.array([[1,2,3]])
arr2D = np.array([[1,2,3],[4,5,6]])
zeroes = np.zeros((2,4))
z_1 = np.zeros_like(arr2D)
ones = np.ones((3,3))
full = np.full((3,3),8) # 3X3 all  8's
f_1 = np.full_like(arr2D,90)
identity = np.eye(5)
trans = arr2D.T

lins = np.linspace(0,100,5)

arange = np.arange(0,12,3)


# 3X4 array of random data distribution
# b/w 0 and 1

rand = np.random.rand(3,4)

# b/w 0 and 100

rand1 = (np.random.rand(3,4)*100)

#randints

randint = np.random.randint(10,50,(3,4))

# normal data distribution
# Gaussian bell curve 

normal = np.random.normal(10,2,10)

#uniform 

uniform = np.random.uniform(-5,5,100)
