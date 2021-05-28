import zipfile
import paramiko
from keep_your_secrets import keep_your_secrets as kp

def ingram():
    #SFTP Time

    paramiko.util.log_to_file("paramiko.log")

    # Open a transport
    host, port = kp()[0], 22
    transport = paramiko.Transport((host, port))

    # Auth
    username, password = kp()[1], kp()[2]
    transport.connect(None, username, password)

    # Go!
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Download
    filepath = "/PRICE.ZIP"
    localpath = "/home/filestore/PRICE.ZIP"
    sftp.get(filepath, localpath)
    # Close
    if sftp: sftp.close()
    if transport: transport.close()

    with zipfile.ZipFile("/home/filestore/PRICE.ZIP","r") as zip_ref:
             zip_ref.extractall("/home/filestore")