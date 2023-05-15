#!/usr/bin/python3
"""
Fabric script that generate tgz archieve
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generate .tgz archive from the content of web static folder
    """
    dtime = datetime.now()
    now = dtime.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
