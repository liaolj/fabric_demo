from fabric.api import *

env.hosts=["10.1.55.137"]
env.user="csns"
env.password = "csns"
def hostname_check():
    run("hostname")