import subprocess

teste=0

def run_command(command):
    resultado=subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    err_text=resultado.stderr.decode("utf-8")
    out_text=resultado.stdout.decode("utf-8")
    if(len(resultado.stderr)>0):
        return 0,err_text
    else:
        return 1,out_text