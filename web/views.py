from flask import jsonify, request
from flask.views import MethodView
from flask import Response
import json

from app import logger
from .errors import BaseException, GenericException


class BasePaymentView(MethodView):

    @staticmethod
    def return_json_response(response, status, message):
        resp = dict(response=response, status=status, message=message)
        return jsonify(resp)

    def return_success_response(self, response):
        logger.info(f"Success response {response}")
        return self.return_json_response(response, 0, "success")

    def return_failure_response(self, status=1, message="error", response={}):
        logger.info(f"Failure response status : {status}, error: {message}")
        return self.return_json_response(response, status, message)

    @staticmethod
    def return_response_with_status_code(payload={}, status_code=502):
        return Response(json.dumps(payload), status=status_code)

    @staticmethod
    def return_error_response_with_status_code(base_exception, status_code=500):
        # in case of any generic exception which is not mentioned in errors.py
        if not isinstance(base_exception, BaseException):
            base_exception = GenericException(msg=str(base_exception))

        payload = {"errors": [{"code": base_exception.code, "code_str": base_exception.code_str,
                               "display_msg": base_exception.display_msg, "type": base_exception.err_type,
                               "msg": base_exception.msg}]}
        logger.info(f"Error response : {payload}")
        return Response(json.dumps(payload), status=status_code, mimetype="application/json")

    @staticmethod
    def return_success_response_with_status_code(response, status_code=200):
        logger.info(f"Success response : {response}")
        return Response(json.dumps(response), status=status_code, mimetype="application/json")