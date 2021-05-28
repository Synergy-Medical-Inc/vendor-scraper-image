from Cleaning import *



def medplus():
    medplus_new = pd.read_csv('/home/filestore/images.txt', usecols=['ManufacturerName', 'ManufacturerItemCode', 'ItemDescription', 'UnitPrice', 'Availability', 'ShippingWeight'], delimiter="\t")
    medplus_new.rename(columns={"ManufacturerItemCode": "SKU", "UnitPrice": "COST", "ShippingWeight": "UNIT_WT", "ItemDescription": "Description", "ManufacturerName":"Manufacturer_Name"}, inplace=True)
    medplus_new.columns = map(str.upper, medplus_new.columns)
    medplus_new.insert(0, 'TIMESTAMP', pd.to_datetime('now').replace(microsecond=0))
    medplus_new.insert(0, 'VENDOR', 'MEDPLUS')

    # data upload shit
    medplus_new.to_gbq('daily_vendor_data.medplus',
                      kp()[11],
                     if_exists='replace'
                     )