import logging

log_filename = 'loggingPractice.log'
log_format = '%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format, datefmt='%Y-%m-%d %H:%M:%S %p', level=logging.INFO,filename=log_filename)
logging.info("hello world")
logging.error("this is an error!!!")
