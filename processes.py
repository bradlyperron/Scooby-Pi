from adc import adc_main
from pi_socket import pi_socket_main
from transducer import transducer_main
from  multiprocessing import Process, Value, Lock

#if running directly
if __name__ == "__main__":
    
    #create locks
    transducer_lock = Lock()
    adc_lock = Lock()

    # create processes
    p_adc = Process(target=adc_main,args=(adc_lock,))
    p_pi_socket = Process(target=pi_socket_main,args=(transducer_lock,adc_lock))
    p_transducer = Process(target=transducer_main,args=(transducer_lock,))
    
    # start processes
    p_adc.start()
    p_transducer.start()
    p_pi_socket.start()
    
    # wait for processes to end
    p_pi_socket.join()
    p_adc.terminate()
    p_transducer.terminate()
