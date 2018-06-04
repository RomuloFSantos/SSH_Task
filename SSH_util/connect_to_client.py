import paramiko

def connect_to_client(credentials):

    client = paramiko.SSHClient()   # instatiate object
    client.load_system_host_keys()  # Load known host keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto add a client that is not in your policy key

    try:
        client.connect(credentials['server'],
                   username=credentials['username'],
                   password=credentials['password'])


    except paramiko.AuthenticationException as e:
        print('ERROR TO AUTHENTICATE: Check your credentials')
        raise e

    return client