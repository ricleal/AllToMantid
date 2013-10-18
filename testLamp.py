'''
Created on Oct 17, 2013

@author: leal
'''

import asynccall.communicate as scall

def testLamp():
    executable = '/net/serhom/home/cs/richard/Free_Lamp81/START_lamp -nws'
    prompt = "DataPath is:"
    exitCommand = "exit"
    
    lamp = scall.Communicate(executable, prompt, exitCommand)
    for i in range(10):
        print lamp.communicate('print, "Hello, Python %i!"'%i, waitTimeForTheCommandToGiveOutput=0.2)
    
    
    print lamp.communicate("rdset, inst='d22'")
    print lamp.communicate("rdset, cycle='133', proposal='internalUse'")
    print lamp.communicate("w2 = rdrun(84452)")
    print lamp.communicate("write_lamp, '/tmp/ricardo', w=2, format='HDF'")
    print lamp.communicate("see, w=2, /surface, /beside")
    print lamp.communicate("spawn, 'mv lamp.png /tmp/ricardo.png'")
    
#     Lamp> write_lamp, w=2, '/tmp/ricardo.txt', format='Ascii'
#     W2 saved in /tmp/ricardo.txt_LAMPascii
#     Lamp> write_lamp, w=2, '/tmp/ricardo.col', format='Column'

    import time
    time.sleep(0.5)
    
    lamp.exit()


if __name__ == '__main__':
    testLamp()