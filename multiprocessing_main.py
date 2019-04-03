import multiprocessing
from tcp_client import tcp_client_main
from graphing_final import graphing_main
import time

if __name__ == "__main__":

    voltage = multiprocessing.Value('d', 0.0)

    p_tcp_client = multiprocessing.Process(target=tcp_client_main, args=(voltage,))
    p_graphing = multiprocessing.Process(target=graphing_main, args=(voltage,))

    p_tcp_client.start()
    time.sleep(2)
    p_graphing.start()

    p_tcp_client.join()
    p_graphing.terminate()

    