import time
import json
import filehandler
import rockBlock
import sys
import struct

from rockBlock import rockBlockProtocol
 
class Sensors (rockBlockProtocol):
	
	SLEEP_INTERVAL = 60
    
    def main(self):
      
         = rockBlock.rockBlock("/dev/ttyUSB0", self)
	
    while True:
	
	value = td.obtain() 
	
        self.emit(value)   
        
	time.sleep(self.SLEEP_INTERVAL)
	
     def emit(self, value):
            
        rb = rockBlock.rockBlock("/dev/ttyUSB1", self)
        
        rb.sendMessage("Td:" + str(time.time()) + ":" + str(value) )
                                                                                  
        rb.close()
        
        
    def rockBlockTxStarted(self):
        print "rockBlockTxStarted"
        
    def rockBlockTxFailed(self):
        print "rockBlockTxFailed"
        
    def rockBlockTxSuccess(self,momsn):
        print "rockBlockTxSuccess " + str(momsn)
        
if __name__ == '__main__':
	Sensors().main()

	
	
	
	
	
