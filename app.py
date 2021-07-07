# -*- coding: utf-8 -*-

from flask import Flask
import os
from bb_aerospike_wrappers.configs import Config as BBAeroConfig
from logging.config import dictConfig
import logging
import newrelic.agent


def get_app():
    try:
        newrelic.agent.initialize("/payment_svc/devops/conf/newrelic/newrelic.ini",
                                  os.getenv("ENVIRONMENT"))
    except:
        pass
    app = Flask(__name__)
    app.config.from_object("settings")
    return app


app = get_app()
BBAeroConfig('settings')

dictConfig(app.config.get('LOGGER_CONFIG'))
logger = logging.getLogger('PaymentLogger')

from web.urls import *  # noqa
from web.views import *  # noqa
from web.models import *  # noqa
from web.utils import create_db_engine


engine = create_db_engine()

if __name__ == "__main__":
    logger.info("Starting Payment Service")
    app.run()
