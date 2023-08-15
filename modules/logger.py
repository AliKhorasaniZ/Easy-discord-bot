import os
import datetime as dt
import logging

logModule = logging.getLogger(__name__)
logModule.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(message)s")

os.getcwd()
if not os.path.exists('Logs/'):
    os.makedirs('Logs/')


def log(message):

    fd = dt.date.today()
    date = (fd.year, fd.month, fd.day)
    date = str(date)

    os.chdir('Logs')
    filehandler = logging.FileHandler(
        filename=(date + ' Music_module.log'), encoding='utf-8')
    os.chdir("../")

    filehandler.setFormatter(formatter)
    logModule.addHandler(filehandler)
    logModule.info('\t' + message)
    logModule.removeHandler(filehandler)
