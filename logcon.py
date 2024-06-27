import logging as log

log.basicConfig(
    level=log.ERROR,
    format="%(asctime)s : %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
    datefmt="%I %S %M %p",
    handlers=[log.FileHandler("log.txt"), log.StreamHandler()],
)

if __name__ == "__main__":
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
