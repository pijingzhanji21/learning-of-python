import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='1.1.1.1',port='22',username='root',password='Hello123')
std_in,std_out,std_error=ssh.exec_command('df -h')
result=std_out.readlines()
for i in result:
    print i
ssh.close()