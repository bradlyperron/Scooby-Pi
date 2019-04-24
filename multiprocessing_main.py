import multiprocessing
from tcp_client import tcp_client_main
from volt_graph import volt_main
#from amp_graph import amp_main
from prim_amp_graph import prim_amp_main
import time

if __name__ == "__main__":

    voltage = multiprocessing.Value('d', 0.0)
    amp = multiprocessing.Value('d',0.0)
    prim_amp = multiprocessing.Value('d',0.0)

    p_tcp_client = multiprocessing.Process(target=tcp_client_main, args=(voltage,amp,prim_amp)) #removed amp between voltage and prim_amp
    p_volt_graph = multiprocessing.Process(target=volt_main, args=(voltage,))
#   p_amp_graph = multiprocessing.Process(target=amp_main, args=(amp,))
    p_prim_amp_graph = multiprocessing.Process(target=prim_amp_main, args=(prim_amp,))


    p_tcp_client.start()
    time.sleep(2)
    p_volt_graph.start()
#    p_amp_graph.start()
    p_prim_amp_graph.start()

    p_tcp_client.join()
    p_volt_graph.terminate()
#    p_amp_graph.terminate()
    p_prim_amp_graph.terminate()

    