'''
Created on Oct 17, 2013

@author: leal
'''

import mantidcall.communicate as mcall
import numpy as np

import string
import random


"""
this can be run inside mantid with (e.g. in my computer):

run /home/leal/git/AllToMantid/testMantid.py


"""
def generateRandomString(prefix='ws', length=6):
    return ''.join(random.sample(string.letters*5,length))

def testMantid():
    m =  mcall.Communicate()
    
    # (n_rows, n_collumns)
    data = np.random.random((10,10))*100
    xAxis = np.arange(1,11)
    
    outputWorkspaceName = generateRandomString()
    m.createWorkspaceHistogram(data, xAxis,outputWorkspaceName)
    
    

if __name__ == '__main__':
    testMantid()