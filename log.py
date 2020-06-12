import datetime
import logging

class CrawlerLog():

    def __init__(self, name):

        # create console handler and set level to debug
        stram_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f'./log/{datetime.datetime.now()}.log')

        # create formatter
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        stram_handler.setFormatter(logging.Formatter('%(message)s'))

        # create logger
        logger = logging.getLogger('log')
        logger.setLevel(logging.DEBUG)

        # add handler
        logger.addHandler(stram_handler)
        logger.addHandler(file_handler)

        self.logger = logger
