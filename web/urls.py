from flask import request
from app import app
from app import logger
from .adapter import DBAdapter


@app.before_request
def before_request_handler():
    request.db_adapter = DBAdapter()


@app.after_request
def after_request_handler(response):
    logger.info(f"response sent {response.status_code}, {response.get_data()}, "
                f"{request.tracker_id}")
    request.db_adapter.close_session()
    return response

