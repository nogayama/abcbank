# -*- coding: utf-8 -*-

########################################################################################
# LOGGER
import logging
DEFAULT_LOG_LEVEL="INFO"

LOGGER = logging.getLogger("abcbank")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s p%(process)d %(threadName)s %(name)s %(levelname)s %(message)s (%(filename)s L%(lineno)s)'))
LOGGER.addHandler(handler)
if DEFAULT_LOG_LEVEL:
    LOGGER.setLevel(getattr(logging, DEFAULT_LOG_LEVEL.upper()))



########################################################################################
# Utilities for command

import subprocess

def execute_command(cmd, shell=False, encoding="UTF-8", errors="replace"):
    LOGGER.info("Executing command: %s", cmd)
    p = subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_bytes, stderr_bytes = p.communicate()
    status = p.returncode
    stdout_text = stdout_bytes.decode(encoding=encoding, errors=errors)
    stderr_text = stderr_bytes.decode(encoding=encoding, errors=errors)
    if status != 0:
        LOGGER.warning("Found non zero exit status: %s", status)
        LOGGER.info("Found exit status: %s, cmd:\n%s\nstdout:\n%s\nstderr:\n%s", status, cmd, stdout_text, stderr_text)
    if LOGGER.isEnabledFor(logging.DEBUG):
        LOGGER.info("Found exit status: %s, cmd:\n%s\nstdout:\n%s\nstderr:\n%s", status, cmd, stdout_text, stderr_text)
         
    return (status, stdout_text, stderr_text)



########################################################################################
# Web app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "cid==0001, John Doe\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
