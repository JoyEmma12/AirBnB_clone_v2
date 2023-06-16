import fabric.api as fab

def test():
   fab.local("ls -l /")
