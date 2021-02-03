import subprocess
import time
while True:
    proc = subprocess.Popen(r"sudo python /home/ubuntu/nat-server/natsrv.py --mode server --secret s3cret --public 0.0.0.0:460 --admin 0.0.0.0:7600", shell=True)
    arg = ['sudo','kill','-9', str(proc.pid+2)]
    time.sleep(5)
    print(arg)
    subprocess.call(arg)
