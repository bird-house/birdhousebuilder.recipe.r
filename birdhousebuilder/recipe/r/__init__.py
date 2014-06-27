# -*- coding: utf-8 -*-
# Copyright (C)2014 DKRZ GmbH

"""Recipe r"""

import os
from mako.template import Template

from birdhousebuilder.recipe import conda

templ_config = Template(
"""
[unix_http_server]
file=${prefix}/var/run/supervisor.sock

[inet_http_server]
port = ${host}:${port}

[supervisord]
childlogdir=${prefix}/var/log/supervisor
logfile=${prefix}/var/log/supervisor/supervisord.log
pidfile=${prefix}/var/run/supervisord.pid
logfile_maxbytes=50MB
logfile_backups=10
loglevel=info
nodaemon=false
minfds=1024
minprocs=200

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///${prefix}/var/run/supervisor.sock

[include]
files = conf.d/*.conf
"""
)

class Recipe(object):
    """This recipe is used by zc.buildout"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        b_options = buildout['buildout']
        self.anaconda_home = b_options.get('anaconda-home', conda.anaconda_home)

        
        self.program = options.get('program', name)

    def install(self):
        installed = []
        installed += list(self.install_supervisor())
        installed += list(self.install_config())
        installed += list(self.install_program())
        installed += list(self.install_start_stop())
        return installed

    def install_supervisor(self):
        script = conda.Recipe(
            self.buildout,
            self.name,
            {'pkgs': 'supervisor'})
        return script.install()
        
       
    def install_program(self):
        """
        install supervisor program config file
        """
        result = templ_program.render(
            program=self.program,
            command=self.command,
            directory=self.directory,
            priority=self.priority,
            environment=self.environment)

        output = os.path.join(self.anaconda_home, 'etc', 'supervisor', 'conf.d', self.program + '.conf')
        conda.makedirs(os.path.dirname(output))
        
        try:
            os.remove(output)
        except OSError:
            pass

        with open(output, 'wt') as fp:
            fp.write(result)
        return [output]

    def update(self):
        return self.install()

def uninstall(name, options):
    pass

