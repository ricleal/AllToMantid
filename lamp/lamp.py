'''
Created on Oct 17, 2013

@author: leal
'''

import nxs

class Lamp(object):
    '''
    Lamp object
    '''
    
    parameters = {}
    data = None
    xAxis = None
    yAxis = None
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def importNexus(self,filePath):
        '''
        Import LAMP generated Nexus file.
        Lamp generates nexus file with the command:
            write_lamp, '/tmp/ricardo', w=2, format='HDF'
        where w is the workspace number
        '''
        nexusFileHandler = self._openNexusFile(filePath)
        
        self.data = self._readData(nexusFileHandler)
        self.xAxis = self._readData(nexusFileHandler,dataFieldName = 'X')
        self.yAxis = self._readData(nexusFileHandler,dataFieldName = 'Y')
        
        params = self._readData(nexusFileHandler,dataFieldName = 'PARAMETERS')
        self.parameters = self._parametersToDict(params)
        
        self._closeNexusFile(nexusFileHandler)
    
    def _openNexusFile(self,filePath):
        nexusFileHandler = nxs.open(filePath)
        nexusFileHandler.opengroup('entry1')
        nexusFileHandler.opengroup('data1')
        return nexusFileHandler;
    
    def _closeNexusFile(self,nexusFileHandler):
        nexusFileHandler.closegroup()
        nexusFileHandler.closegroup()
        nexusFileHandler.close()
        
    def _readData(self,nexusFileHandler, dataFieldName = 'DATA'):
        nexusFileHandler.opendata(dataFieldName)
        a = nexusFileHandler.getdata()
        nexusFileHandler.closedata()
        return a

    
    def _parametersToDict(self,params):
        """
        @param params: string
        """
        paramsAsListOfLists = [ [j.strip() for j in i.split('=')] for i in params.split('\n')]
            
        return dict(paramsAsListOfLists)
    
    def showSnapShot(self,filename):
        """
        It prints the snapshot in the Lamp nexus file
        There's no really use for these...
        
        @param filename:
        """
        f = nxs.open(filename)
        f.opengroup('entry1')
        f.opengroup('data1')
        f.opendata('SNAPSHOT')
        a = f.getdata()
        f.closedata()
        f.closegroup()
        f.closegroup()
        f.close()
        import matplotlib.pyplot as plt
        plt.imshow(a)
        plt.show()


if __name__ == '__main__':
    l = Lamp()
    l.importNexus('/tmp/ricardo_LAMP.hdf')
    import pprint
    pprint.pprint(l.parameters)
    pprint.pprint(l.parameters.keys())
    pprint.pprint(l.xAxis)
    pprint.pprint(l.yAxis)
    print l.data.shape
    l.showSnapShot('/tmp/ricardo_LAMP.hdf')

    
        