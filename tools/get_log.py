import logging

def get_loging():
    fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
    logging.basicConfig(level=logging.INFO, filename="../log/log01.log", format=fm)
    return logging