#Tentativa de automatizar envio de pacotes a múltiplos hosts de uma vez
#!/usr/bin/env python3
import pexpect
# import argparse
# import subprocess
import os
import sys

MAKEFILE_PATH = "/home/p4/ProjetoMestradoP4IoTForensics/exercises/pre-processing/Makefile"

class MininetAuto:
    def __init__(self) -> None:
        self.proc = pexpect.spawn("make run", cwd=os.path.dirname(MAKEFILE_PATH), encoding="utf-8")
        self.proc.logfile_read = sys.stdout

    def run_dispositivos_iot(self):
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h1 python3 send.py 10.0.2.2 &")

    def run_plano_de_controle(self):
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h5 python3 receive_agg.py &")

        # self.proc.sendline(f"h"+str(id)+" python3 application.py "+str(id)+" &")

    def wait(self):
        self.proc.expect("mininet> ", timeout=None)
        x = input()


def main():
    mininet_auto = MininetAuto()
    mininet_auto.run_dispositivos_iot()
    mininet_auto.run_plano_de_controle()

    # for i in range(1,9):
    #     if(i != 3):  #3 is the coordinator
    #         mininet_proc.run_server(id=i)

    mininet_auto.wait()

if __name__ == "__main__":
    main()