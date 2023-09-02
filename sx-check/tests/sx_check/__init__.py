import logging

FORMAT = "\n".join(
    [
        "%(levelname)-4s  %(message)s",
        "      %(asctime)s %(module)-15s %(lineno)-8s",
    ]
)

logging.basicConfig(format=FORMAT, level=logging.DEBUG)
