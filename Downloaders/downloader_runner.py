from Downloaders import tecnec_xls_downloader
from Downloaders import ingram_micro_downloader
from Downloaders import synnex_medplus_file_downloader

def dRunner():
    tecnec_xls_downloader.tecnec_dwnld()
    synnex_medplus_file_downloader.medplus_dwnld()
    synnex_medplus_file_downloader.synnex()
    ingram_micro_downloader.ingram()
    print("Done w/ Drunner")
