#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from datetime import datetime
from fabric.api import env, put, run, local, sudo
from os.path import exists

env.hosts = ['54.157.152.252', '54.82.119.92']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_name_no_ext = archive_name.split(".")[0]
        release_path = '/data/web_static/releases/{}'.format(
            archive_name_no_ext
        )
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_path))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception as e:
        return False


def deploy():
    """Deploys the web_static content to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
