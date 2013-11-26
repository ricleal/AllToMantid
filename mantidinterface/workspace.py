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
import string
import random
import datetime

class Workspace(object):
    '''
    classdocs
    '''
    

    thisWs = None
    
    def __init__(self, wsName=None):
        '''
        Constructor
        '''
        if wsName is None:
            self.name = self._generateStringFromTime()
        else:
            self.name = wsName
    
    def _generateRandomString(self, prefix='ws_', length=4):
        return prefix+"".join(random.sample(string.letters*5,length))
    
    def _generateStringFromTime(self, prefix='ws_'):
        now = datetime.datetime.now()
        t = now.time()
        return prefix+"%02d%02d%02d"%(t.hour,t.minute,t.second)
    
    def _calculateEnergy(self,wavelength):
        h = 6.62606896e-34
        neutronMass = 1.674927211e-27
        meV = 1.602176487e-22
        e = (h * h) / (2 * neutronMass * wavelength * wavelength * 1e-20) / meV
        return e;
    
    def createFromData(self,data,xAxis,unitX="Wavelength",yUnitLabel='Counts'):
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

        thisWs = CreateWorkspace(DataX=xAxisClonedNRowsTimes, DataY=dataFlat, DataE=np.sqrt(dataFlat),
                                              NSpec=nRows,UnitX=unitX,YUnitLabel=yUnitLabel,OutputWorkspace=self.name)
        
    
    
    def _valid(self):
        '''
        Make sure the ws exists.
        Don't know why mantid looses it...
        '''
        if self.thisWs is None:
            print "Warning: self.thisWs is None"
            self.thisWs = mtd[self.name]
            if self.thisWs is None:
                print "ERROR: self.thisWs is still None"
                return False
        return True
    
    def setProperties(self,propertyDic):
        """
        @param propertyDic: must be pair of string:string
        
        """
        if self._valid() == False:
            sys.exit(-1)
        
        r = self.thisWs.run()
        
        for key, value in propertyDic.iteritems():
            r.addProperty(key,value,True)
        
        
    def setAndCorrectProperties(self,propertyDic):    
        """
        
        """
        if self._valid() == False:
            sys.exit(-1)
        r = self.thisWs.run()
        
        
        import re
        wavelengthRE = re.compile(".+Wavelength.+angstroms.+")
        for key, value in propertyDic.iteritems():
            print key, ":", value
            if key is not None and value is not None and len(key) > 0 and len(value) > 0 :
                if wavelengthRE.match(key) is not None:
                    r.addProperty("wavelength",float(value),True)
                    r.addProperty("Ei",self._calculateEnergy(float(value)),True)
                else :
                    try: 
                        r.addProperty(key,float(value),True)
                    except:
                        r.addProperty(key,value,True)
        
    
        
        