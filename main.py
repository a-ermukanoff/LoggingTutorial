import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")  # по умолчанию используется именно этот уровень логирования
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
