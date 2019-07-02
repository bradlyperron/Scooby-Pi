from adc import adc_main
from pi_socket import pi_socket_main
from transducer import transducer_main
from  multiprocessing import Process

#if running directly
if __name__ == "__main__":

    # create processes
    p_adc = Process(target=adc_main)
    p_pi_socket = Process(target=pi_socket_main)
    p_transducer = Process(target=transducer_main)
    
    # start processes
    p_adc.start()
    p_transducer.start()
    p_pi_socket.start()
    
    # wait for processes to end
    p_pi_socket.join()
    p_adc.terminate()
    p_transducer.terminate()
