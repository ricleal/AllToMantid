'''
Created on Oct 17, 2013

@author: leal
'''

import asynccall.communicate as call

def testLamp():
    executable = '/net/serhom/home/cs/richard/Free_Lamp81/START_lamp -nws'
    prompt = "DataPath is:"
    exitCommand = "exit"
    
    lamp = call.Communicate(executable, prompt, exitCommand)
    for i in range(10):
        print lamp.communicate('print, "Hello, Python %i!"'%i, waitTimeForTheCommandToGiveOutput=0.2)
    
    lamp.exit()

if __name__ == '__main__':
    testLamp()