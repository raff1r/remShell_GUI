import paramiko
import getpass

class SSHClient:

    def __init__(self,host, user):
        self.hostname = host
        self.user = user
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()

    # Connect to server with password based auth
    def connect_password_based(self, password):
        self.password = password
        self.client.connect(
            hostname = self.hostname,
            username = self.user,
            password = self.password
        )
    
    # Connect to server with private key based auth
    # keyfile location, key password, and type of ssh algorithm
    def connect_key_based(self, keyfile, password, type="rsa"):
        self.password = password
        self.type = type
        if(self.type == "rsa"):
            self.key = paramiko.RSAKey.from_private_key_file(keyfile, self.password)
        elif(self.type == "dsskey"):
            self.key = paramiko.DSSKey.from_private_key_file(keyfile, self.password)
        elif(self.type == "ecdsa"):
            self.key = paramiko.ECDSAKey.from_private_key_file(keyfile, self.password)
        elif(self.type == "ed25519"):
            self.key = paramiko.Ed25519Key.from_private_key_file(keyfile, self.password)
        self.client.connect(
            hostname = self.hostname,
            username = self.user,
            pkey = self.key
        )

    # Execute list of command
    def exec(self,sudo,pty_boolean,*command):
        self.result = []
        self.error = []
        if(sudo==False):
            for i in command:
                self.stdin, self.stdout, self.stderr = self.client.exec_command(i,get_pty=pty_boolean)
                self.result.append(self.stdout.read().decode())
                self.error.append(self.stderr.readlines())
            self.client.close()
        elif(sudo==True):
            for i in command:
                self.stdin, self.stdout, self.stderr = self.client.exec_command(i,get_pty=pty_boolean)
                self.stdin.write(f"{self.password}\n")
                self.stdin.flush()
                self.result.append(self.stdout.read().decode())
                self.error.append(self.stderr.readlines())
            self.client.close()