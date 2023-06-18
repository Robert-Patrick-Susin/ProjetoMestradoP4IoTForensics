#Tentativa de automatizar envio de pacotes a múltiplos hosts de uma vez
#!/usr/bin/env python3
import pexpect
import argparse
import subprocess
import os
import sys

MAKEFILE_PATH = "/home/p4/ProjetoMestradoP4IoTForensics/exercises/no-pre-processing/Makefile"

class MininetAuto:
    def __init__(self) -> None:
        self.proc = pexpect.spawn("make run", cwd=os.path.dirname(MAKEFILE_PATH), encoding="utf-8")
        self.proc.logfile_read = sys.stdout

    def run_plano_de_controle(self):
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h42 python3 receive_noagg.py &")

    def run_dispositivos_iot(self):
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h1 python3 send.py 10.0.41.41 teste")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h2 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h3 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h4 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h5 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h6 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h7 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h8 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h9 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h10 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h11 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h12 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h13 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h14 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h15 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h16 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h17 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h18 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h19 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h20 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h21 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h22 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h23 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h24 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h25 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h26 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h27 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h28 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h29 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h30 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h31 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h32 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h33 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h34 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h35 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h36 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h37 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h38 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h39 python3 send.py 10.0.41.41 teste &")
        self.proc.expect("mininet> ", timeout=None)
        self.proc.sendline(f"h40 python3 send.py 10.0.41.41 teste &")

        # self.proc.sendline(f"h"+str(id)+" python3 application.py "+str(id)+" &")

    def wait(self):
        self.proc.expect("mininet> ", timeout=None)
        x = input()


def main():
    mininet_auto = MininetAuto()
    mininet_auto.run_plano_de_controle()
    mininet_auto.run_dispositivos_iot()

    # for i in range(1,9):
    #     if(i != 3):  #3 is the coordinator
    #         mininet_proc.run_server(id=i)

    mininet_auto.wait()

if __name__ == "__main__":
    main()