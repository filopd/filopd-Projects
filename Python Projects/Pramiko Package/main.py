import paramiko

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("filopd_server", port=22, username="filopd", password="filopd_pwd")
stdin, stdout, stderr = p.exec_command("ls -ltr")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)

