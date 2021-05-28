from Cleaning import *

def resources():
    ls=[]
    for i in tsdf():
        ls.append(eval(i))
    return ls


def tecnec():
    df_list_cleaned = []
    table_names = ["TECNEC", "SPIDER", "SESCOM", "OCEAN_MATRIX", "LAIRD", "DELVCAM", "CAMPLEX"]
    for i, v in zip(resources(), table_names):
        if "MFG PART NUMBER" in i.columns:
            i.rename(columns={"MFG PART NUMBER": "SKU"}, inplace=True)
        if "PART NUMBER" in i.columns:
            i.rename(columns={"PART NUMBER": "SKU"}, inplace=True)
        if "MFG" in i.columns:
            i.rename(columns={"MFG": "MANUFACTURER_NAME"}, inplace=True)

        i.rename(columns={"DEALER": "COST"}, inplace=True)
        i['STATUS'].fillna("ACTIVE", inplace=True)
        i['STATUS'] = i['STATUS'].str.upper()
        rmv = ['EOL', '**']
        i = i[i['STATUS'].isin(rmv) == False]
        i.columns = i.columns.str.replace(" ", "_")

        if 'MANUFACTURER_NAME' not in i.columns:
            i.insert(0, 'MANUFACTURER_NAME', v)

        i.insert(0, 'TIMESTAMP', pd.to_datetime('now').replace(microsecond=0))
        i.insert(0, 'VENDOR', 'TECNEC')
        i.drop(columns=['STATUS'], axis=1, inplace=True)
        df_list_cleaned.append(i)
    return df_list_cleaned

def gbq():
    table_names = ["tecnec", "spider", "sescom", "ocean_matrix", "laird", "delvcam", "camplex"]

    # data upload shit
    for df, name in zip(tecnec(), table_names):
        full_name = 'daily_vendor_data.' + name
        df.to_gbq(full_name, kp()[11], if_exists='replace')

gbq()