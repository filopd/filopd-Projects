import paramiko

#iServer = input("Enter Server Name:")
#iPort = input("Enter Port Number:")
#iUserName = input("Enter your user name:")
iPassword = input("Enter your password:")
iCommand = "cd /root_folder/paramikoProject; pwd; python sample.py"


p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#p.connect(iServer, port=iPort, username=iUserName, password=iPassword)
p.connect("filopd_server", port=22, username="filopd", password=iPassword)
stdin, stdout, stderr = p.exec_command("pwd")

opt = stdout.readlines()
opt = "".join(opt)
print(opt)
#stdin, stdout, stderr = p.exec_command("cd /root_folder/paramikoProject; pwd; python sample.py")
stdin, stdout, stderr = p.exec_command(iCommand)
opt = stdout.readlines()
opt = "".join(opt)
print(opt)

