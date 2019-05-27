#import all files
import multiprocessing
from tcp_client import tcp_client_main
from volt_print import volt_main
from actuator_power_graph import actuator_power_graph_main
from motor_power_graph import motor_power_graph_main
from print_out_test import print_main
import time

if __name__ == "__main__":
    
    #initialize global variables
    volt1 = multiprocessing.Value('d', 0.0)
    volt2 = multiprocessing.Value('d', 0.0)
    actuator_amp = multiprocessing.Value('d',0.0)
    motor_amp = multiprocessing.Value('d',0.0)
    
    #create processes
    p_tcp_client = multiprocessing.Process(target=tcp_client_main, args=(volt1,volt2,actuator_amp,motor_amp))
    p_volt_print = multiprocessing.Process(target=volt_main, args=(volt1,volt2))
    p_actuator_power_graph = multiprocessing.Process(target=actuator_power_graph_main, args=(actuator_amp,volt1))
    p_motor_power_graph = multiprocessing.Process(target=motor_power_graph_main, args=(motor_amp,volt1))
    p_print_out_test = multiprocessing.Process(target=print_main, args=(volt1,volt2,actuator_amp,motor_amp))
    
    #start processes
    p_tcp_client.start()
    time.sleep(2)
    p_volt_print.start()
    p_actuator_power_graph.start()
    p_motor_power_graph.start()
    #p_print_out_test.start()
    
    #end processes
    p_tcp_client.join()
    p_volt_print.terminate()
    p_actuator_power_graph.terminate()
    p_motor_power_graph.terminate()
    #p_print_out_test.terminate()
    
