import logging
import os
from pathlib import Path

import paramiko
from paramiko import SSHClient

"""
Connect to server with paramiko. 
"""


class Monitor:
    def __init__(self, server_ip_address, username, password):
        self.server_ip_address = server_ip_address
        self.client = SSHClient()
        self.port = 22
        self.username = username
        self.password = password

    def connect_ssh(self):
        try:
            # Open a transport
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.WarningPolicy())
            self.client.connect(self.server_ip_address, port=self.port, username=self.username, password=self.password)

            command = self.get_CPU()

            stdin, stdout, stderr = self.client.exec_command(command)

            output = ""
            for line in stdout:
                output += line
            if output != "":
                print(output)
            else:
                print("There was no output for this command")

        except paramiko.SSHException as e:
            # except Exception as e:
            str(e) + str(e.args) + str(e.with_traceback(e.__traceback__))
        finally:
            self.client.close()

    def get_CPU(self):
        with open('test_command.txt', 'r') as myfile:
            data = myfile.read()
        return data
