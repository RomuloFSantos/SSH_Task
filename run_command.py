import paramiko

def run_command(client, command):

    try:
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)

        error = ssh_stderr.read()

        if len(error) > 0:
            print(f'Command {command} hit this error:{error}')

        for i in ssh_stdout:
            print(i.strip())

    except paramiko.SSHException as e:
        print('Something went wrong with the command')
        raise e