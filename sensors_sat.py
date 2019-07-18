import time
import json
import filehandler
import rockBlock
import sys
import struct

from rockBlock import rockBlockProtocol
 
class MoExample (rockBlockProtocol):
    
    def main(self):
      
        rb = rockBlock.rockBlock("/dev/ttyUSB0", self)
        
        rb.sendMessage("Hello World RockBLOCK!")      
        
	rb.close()
        
    def rockBlockTxStarted(self):
        print "rockBlockTxStarted"
        
    def rockBlockTxFailed(self):
        print "rockBlockTxFailed"
        
    def rockBlockTxSuccess(self,momsn):
        print "rockBlockTxSuccess " + str(momsn)
        
if __name__ == '__main__':
    MoExample().main()
