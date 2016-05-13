from fabric.api import *

env.hosts=["10.1.55.137"]
env.user="csns"
env.password = "csns"
def hostname_check():
    run("hostname")

def command(cmd):
	run(cmd)

def sudo_command(cmd):
	sudo(cmd)

def test():
    with settings(user="csns",host_string="10.1.55.137"):
        run("whoami")
    run("pwd")

def ssh_conf_backup():
    with cd("/etc/ssh/"):
        sudo("cp -b ssh_config ssh_config")