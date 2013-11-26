'''
Created on Oct 17, 2013

@author: leal
'''

import asynccall.communicate as scall
import sys


tempFilePath="'/tmp/in6_161193.nxs'"
def testIfit():
    '''
    Uses asynccall.communicate to call ifit executable.
    Launch a few Lamp commands and saves a nexus file.
    '''
    
    executable = '/usr/local/bin/ifit'
    prompt = "iFit:1"
    exitCommand = "exit"
    
    ifit = scall.Communicate(executable, prompt, exitCommand)
    
    print ifit.communicate("a = iData('/net/serdon/illdata/data/in6/internalUse/rawdata/161193.nxs')")
    print ifit.communicate("saveas(a,%s,'mantid')"%tempFilePath)
    

    import time
    time.sleep(0.5)
    
    ifit.exit()


if __name__ == '__main__':
    testIfit()
    mantidBinDir    = '/opt/Mantid/bin'
    sys.path.append(mantidBinDir)
    from mantid.simpleapi import *
    Load(Filename=tempFilePath,OutputWorkspace='in6_161193')
    