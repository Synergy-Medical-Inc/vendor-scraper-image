from Cleaning import *

def mpl_runner():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "test1-312816-9663bb495e7d.json"
    client = sm.SecretManagerServiceClient()
    secrets = f"projects/481475670378/secrets/MPL-select-list/versions/1"
    response = client.access_secret_version(request={"name": secrets})
    payload = response.payload.data.decode('UTF-8')
    payload = payload.replace('"S', 'S').rstrip('"')
    name = payload.replace('",', '",').split('", ')
    return name

def mpl_df():
    ls = []
    for i in mpl_runner():
        ls.append(i)

    print(ls[0])


    camplex= pd.read_gbq(str(ls[0]))

    delvcam = pd.read_gbq(ls[1])

    laird = pd.read_gbq(ls[2])

    medplus = pd.read_gbq(ls[3])

    ocean_matrix = pd.read_gbq(ls[4])

    sescom = pd.read_gbq(ls[5])

    spider = pd.read_gbq(ls[6])

    synnex_ava = pd.read_gbq(ls[7])

    tecnec = pd.read_gbq(ls[8])

    ingram = pd.read_gbq(ls[9])

    master_product_list = pd.concat([camplex, delvcam, laird, medplus,ocean_matrix, sescom, spider, synnex_ava, ingram, tecnec], axis=0, join='outer')

    return master_product_list


def mpl_to_gbq():
    mpl_df().to_gbq('daily_vendor_data.master_product_list',
                      'test1-312816',
                      if_exists='replace'
                      )
