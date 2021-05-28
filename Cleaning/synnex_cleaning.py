from Cleaning import *


def synnex():

    synnex_new = pd.read_csv('/home/filestore/558671.ap', delimiter="~", skiprows=1, usecols=[2, 4, 5, 6, 7, 9, 12], names=['SKU', 'SYNNEX_SKU', 'STATUS', 'DESCRIPTION', 'MANUFACTURER_NAME', 'QTY', 'COST'])
    rmv = ['D', 'NaN', 'NA']
    synnex_new['QTY'] = pd.to_numeric(synnex_new['QTY'], errors='coerce')
    synnex_new = synnex_new.dropna(subset=['QTY'])
    synnex_new['QTY'] = synnex_new['QTY'].astype(int)
    synnex_new = synnex_new[synnex_new['STATUS'].isin(rmv) == False]
    synnex_new.drop(columns=['STATUS'], axis=1, inplace=True)
    synnex_new.insert(0, 'VENDOR', 'SYNNEX')
    synnex_new.insert(0, 'TIMESTAMP', pd.to_datetime('now').replace(microsecond=0))


    #Filtered DF
    synnex_filt = synnex_new
    synnex_filt = synnex_filt[synnex_filt['COST'] <= 2500]
    synnex_filt = synnex_filt[synnex_filt['QTY'] >= 10]
    synnex_filt = synnex_filt[synnex_filt['QTY'] < 9999]

    # GBQ
    synnex_filt.to_gbq('daily_vendor_data.synnex_ava',
                       kp()[11],
                       if_exists='replace'
                       )

    #GBQ
    synnex_new.to_gbq('daily_vendor_data.synnex_full',
                          kp()[11],
                          if_exists='replace',
                      )

