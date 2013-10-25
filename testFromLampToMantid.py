'''
Created on Oct 18, 2013

@author: leal
'''

import asynccall.communicate as scall
import mantidcall.communicate as mcall

import tempfile
import lamp.lamp as lamp
import os

"""

In mantid ipython console type:
run /home/leal/git/AllToMantid/testFromLampToMantid.py

"""
def runCommandInLamp(tempFileNamePrefix):
    executable = '/net/serhom/home/cs/richard/Free_Lamp81/START_lamp -nws'
    prompt = "DataPath is:"
    exitCommand = "exit"
    
    lamp = scall.Communicate(executable, prompt, exitCommand)  
    
    print lamp.communicate("rdset, inst='d22'")
    print lamp.communicate("rdset, cycle='133', proposal='internalUse'")
    print lamp.communicate("w2 = rdrun(84452)")
    print lamp.communicate("write_lamp, '"+tempFileNamePrefix+"', w=2, format='HDF'")
        
    import time
    time.sleep(0.5)    
    lamp.exit()

    return tempFileNamePrefix + "_LAMP.hdf"

def convertLampWorkspaceToNumpy(filename): 
    l = lamp.Lamp()
    l.importNexus(filename)
    return l

def importWSInLampToMantid(lampws):
    m =  mcall.Communicate()
    data = lampws.data
    xAxis = lampws.xAxis
    m.createWorkspaceHistogram(data, xAxis,outputWorkspaceName='LampToMantid')

if __name__ == '__main__':
    tempFileNamePrefix = tempfile.NamedTemporaryFile(delete=False)
    hdfFile = runCommandInLamp(tempFileNamePrefix=tempFileNamePrefix.name)
    lampWS = convertLampWorkspaceToNumpy(hdfFile)
    importWSInLampToMantid(lampWS)
    os.remove(hdfFile)
