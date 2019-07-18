import rockBlock
import time
import filehandler
import json 
 
from rockBlock import rockBlockProtocol
 
class Sensor (rockBlockProtocol):
    
    SLEEP_INTERVAL = 60
            
    def main(self):
            
        while(True):
        
            depth = getJson('transducer', 'depth') 
            
            self.emit(value)
                        
            time.sleep( self.SLEEP_INTERVAL)
                                
    def emit(self, value):
            
        rb = rockBlock.rockBlock("/dev/ttyUSB1", self)
        
        rb.sendMessage("Td:" + str(time.time()) + ":" + str(depth) )
                                                                                  
        rb.close()
	
 
    def getJson (filename,value):
        
        try:
            data = fileHandler.read('/home/pi/logs/{}.json'.format(filename))
            data = json.loads(data)
            return data[value]
        except:
            return 0.0

	
	
	
	
