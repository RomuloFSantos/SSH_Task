import sys
from SSH_util import run_command, get_credentials, connect_to_client


def main():

    credentials = get_credentials.get_credentials(sys.argv[1])

    command = str(sys.argv[2])

    client = connect_to_client.connect_to_client(credentials)

    run_command.run_command(client, command)




if __name__ == '__main__':
    main()