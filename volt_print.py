import time as t
import datetime as dt
from pathlib import Path

def volt_main(volt1,volt2):
    
        #format time
        def format_time(begin,str_len,s):
                time = dt.datetime.now()
                s = time.strftime('%Y-%m-%d %H{}%M{}%S.%f'.format(s,s))
                return s[begin:-(26-str_len)]
        # generate file names
        def gen_file_names():
                v1_time = Path("C:/Users/Angus/Desktop/voltage logs/{} v1_time.txt".format(format_time(0,13,'-')))
                v1_value = Path("C:/Users/Angus/Desktop/voltage logs/{} v1_value.txt".format(format_time(0,13,'-')))
                v2_time = Path("C:/Users/Angus/Desktop/voltage logs/{} v2_time.txt".format(format_time(0,13,'-')))
                v2_value = Path("C:/Users/Angus/Desktop/voltage logs/{} v2_value.txt".format(format_time(0,13,'-')))               
                return (v1_time,v1_value,v2_time,v2_value)

        i = 0
        print("{:>3}\t{:>3}".format('primary','secondary'))
        while True:
                #print voltage values
                print("{:>3.1f}\t{:>3.1f}".format(volt1.value,volt2.value))
                
                #get file names
                v1_time, v1_value, v2_time, v2_value = gen_file_names()

                #log to files
                if i%12 == 0 and i != 0:
                        with open(v1_time, "a") as v1_t:
                                v1_t.write(format_time(11,19,':')+"\n")
                        with open(v1_value, "a") as v1_v:
                                v1_v.write(str(volt1.value)+"\n")
                        with open(v2_time, "a") as v2_t:
                                v2_t.write(format_time(11,19,':')+"\n")
                        with open(v2_value, "a") as v2_v:
                                v2_v.write(str(volt2.value)+"\n")       
                
                i+=1
                t.sleep(300)

        

