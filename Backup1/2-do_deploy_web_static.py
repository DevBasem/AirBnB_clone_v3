#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
using the function do_deploy.
"""

from fabric.api import env, run, put
from os.path import exists
import os

env.hosts = ['54.157.152.252', '54.82.119.92']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_filename)[0]
        release_path = '/data/web_static/releases/{}'.format(
            archive_name_no_ext
        )
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move contents of web_static/ to web_static/releases/<archive name>
        run('mv {}/web_static/* {}/'.format(release_path, release_path))

        # Remove the now empty web_static/ directory
        run('rm -rf {}/web_static'.format(release_path))

        # Delete the existing symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
