'''
Created on Oct 17, 2013

@author: leal
'''

import mantidinterface.workspace as mtdi
import numpy as np




"""
this can be run inside mantid with (e.g. in my computer):

run /home/leal/git/AllToMantid/testMantid.py


"""


def testMantid():
    '''
    
    '''
    m =  mtdi.Workspace()
    
    # (n_rows, n_collumns)
    data = np.random.random((10,10))*100
    xAxis = np.arange(1,11)
    
    
    m.createFromData(data, xAxis)
    #m.setProperties( {"p1":"1","p2":"2", "p3": "string 11212"} )
    m.setAndCorrectProperties({"p1":"1","p2":"2", "p3": "string 11212",'15) Wavelength (angstroms)': 5.23})
    

if __name__ == '__main__':
    testMantid()