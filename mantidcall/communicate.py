'''
Created on Oct 17, 2013

@author: leal
'''
import sys
# try :
#     sys.modules['mantid']
# except:
mantidBinDir    = '/opt/Mantid/bin'
sys.path.append(mantidBinDir)
from mantid.simpleapi import *

#from mantid.simpleapi import *
import numpy as np

class Communicate(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def createWorkspaceHistogram(self,data,xAxis,outputWorkspaceName,unitX="Wavelength",yUnitLabel='Counts'):
        """
        
        @param data: Assuming for now the data is a numpy 2D array
        @param outWorkspaceName:
        """
        
        # http://www.mantidproject.org/Extracting_And_Manipulating_Data
        
        # Add last bin to X 
        lastBin = xAxis[-1] + (xAxis[-1]-xAxis[-2])
        xAxis = np.append(xAxis,lastBin)
        

        (nRows, nCollumns) = data.shape        
        dataFlat = data.flatten() # convert to 1D
        
        xAxisClonedNRowsTimes = np.tile(xAxis,nRows)

        CreateWorkspace(DataX=xAxisClonedNRowsTimes, DataY=dataFlat, DataE=np.sqrt(dataFlat),
                                              NSpec=nRows,UnitX=unitX,YUnitLabel=yUnitLabel,OutputWorkspace=outputWorkspaceName)
        
    
        
        