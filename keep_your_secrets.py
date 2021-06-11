import os

from google.cloud import secretmanager


def keep_your_secrets():

    #Get Secrets
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "test1-312816-9663bb495e7d.json"
    client = secretmanager.SecretManagerServiceClient()
    secrets = f"projects/481475670378/secrets/name-list-test-two/versions/1"
    response = client.access_secret_version(request={"name": secrets})
    payload = response.payload.data.decode('UTF-8')
    name = payload.replace('f"', '')
    name = name.replace('"', '')
    name = name.strip('][').split(',')

    payload_list = []


    for i in name:
        response = client.access_secret_version(request={"name": i})
        payload = response.payload.data.decode('UTF-8')
        payload_list.append(payload)
    return payload_list


def tsdf():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/test1-312816-9663bb495e7d.json"
    client = secretmanager.SecretManagerServiceClient()
    secrets = f"projects/481475670378/secrets/linux-home-filestore-downloader-list/versions/1"
    response = client.access_secret_version(request={"name": secrets})
    payload = response.payload.data.decode('UTF-8')
    name = payload.replace('),', ')|,').split('|, ')
    return name


