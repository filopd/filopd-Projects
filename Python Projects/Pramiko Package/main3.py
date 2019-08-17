    def execute_single_sudo_command(self, command):
        result = ""
        try:
            self.global_var = GlobalVariables()
            self.global_var.set_linux_variables()
            commands = []
            commands.append(str(command[0]))
            commands.append(str(self.global_var.linux_password))
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(str(self.global_var.linux_server), username=str(self.global_var.linux_username), password=str(self.global_var.linux_password))
            channel = client.invoke_shell()
            time.sleep(1)
            channel.recv(9999)
            channel.send("\n")
            time.sleep(1)
            cmdNo = 0
            for command in commands:
                channel.send(command + "\n")
                while not channel.recv_ready():  # Wait for the server to read and respond
                    time.sleep(2)
                time.sleep(2)  # wait enough for writing to (hopefully) be finished
                output = channel.recv(9999)  # read in
                op = str(output.decode('utf-8'))
                time.sleep(2)
                if cmdNo == 1:
                    result = str(op)
                cmdNo += 1
            channel.close()
        except Exception as inst:
            log.error("x [E: Unable to execute sudo command on Linux Server!")
            log.error("x [" + str(type(inst)))
            log.error("x [" + str(inst.args))
        finally:
            client.close()
            return result