import logging
import datetime

logger=logging.getLogger("simple_logger")

current_time=datetime.datetime.now().strftime("%I-%M%p-%B-%d-%Y")
log_path="./logs/"+current_time

handler=logging.FileHandler(log_path+".log")
handler.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.setLevel(level=logging.DEBUG)
logger.addHandler(handler)

