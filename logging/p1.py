import logging
logging.basicConfig(filename='log.txt',level=10, filemode='w')

logging.debug('debug Message')
logging.info('info Message')
logging.warning('warning Message')
logging.error('error Message')
logging.critical('critical Message')