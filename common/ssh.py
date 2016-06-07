#!/usr/bin/env python
#-- coding:utf-8 --
import paramiko

class SSHClient(object):
	def __init__(self, hostname, command, port=50000):
		self.hostname = hostname
		self.port = port
		self.command = command

	def execute(self):
		with paramiko.SSHClient() as client:
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname=self.hostname, port=self.port)
			stdin, stdout, stderr = client.exec_command(self.command)
			stdout = stdout.readlines()
			stderr = stderr.readlines()
			return stdout, stderr
