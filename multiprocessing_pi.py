from adc import adc_main
from tcp_server import tcp_server_main
import multiprocessing

#if running directly
if __name__ == "__main__":
    
    #create shared memory value to store voltage read by adc
    volt1 = multiprocessing.Value('d', 0.0)
    volt2 = multiprocessing.Value('d',0.0)
    motor_amp = multiprocessing.Value('d',0.0)
    actuator_amp = multiprocessing.Value('d',0.0)    
    
    # create processes
    p_adc = multiprocessing.Process(target=adc_main,args=(volt1,volt2,motor_amp,actuator_amp))
    p_tcp_server = multiprocessing.Process(target=tcp_server_main,args=(volt1,volt2,motor_amp,actuator_amp))
    
    # start processes
    p_adc.start()
    p_tcp_server.start()
    
    # wait for processes to end
    p_tcp_server.join()
    p_adc.terminate()
    p_adc.join()
