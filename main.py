import Cleaning.cleaning_runner
import Downloaders.downloader_runner
import os

def vendor_run():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/test1-312816-0263182f1b1e.json"
    Downloaders.downloader_runner.dRunner()
    Cleaning.cleaning_runner.cRunner()
    print('Done.')

if __name__ == '__main__':
    vendor_run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
