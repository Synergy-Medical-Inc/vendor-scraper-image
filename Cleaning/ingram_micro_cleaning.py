from Cleaning import *


def ingram():
    ingram_new = pd.read_csv('/home/filestore/PRICE.TXT', delimiter='\t', usecols=[0, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 16], names=['STATUS', 'MANUFACTURER_NAME', 'DESCRIPTION', 'DESCRIPTION_2', 'SKU', 'WEIGHT', 'UPC', 'LENGTH', 'WIDTH', 'HEIGHT', 'COST', 'AVAILABILITY'])
    ingram_new = ingram_new[ingram_new['STATUS'].str.contains("D") == False]
    ingram_new = ingram_new[ingram_new['AVAILABILITY'].str.contains("N") == False]
    ingram_new.drop(columns=['STATUS','AVAILABILITY'], axis=1, inplace=True)
    ingram_new.insert(0, 'TIMESTAMP', pd.to_datetime('now').replace(microsecond=0))
    ingram_new.insert(0, 'VENDOR', 'INGRAM_MICRO')
    # data upload shit
    ingram_new.to_gbq('daily_vendor_data.ingram',
                      kp()[11],
                      if_exists='replace'
                      )