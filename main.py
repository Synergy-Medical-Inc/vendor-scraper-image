import Cleaning.cleaning_runner
import Downloaders.downloader_runner

def vendor_run():
    print("Starting.")
    Downloaders.downloader_runner.dRunner()
    Cleaning.cleaning_runner.cRunner()
    print('Done.')


if __name__ == '__main__':

    vendor_run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
