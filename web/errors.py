from web.consts import DisplayMsg, ErrorType, ErrorCode

PAYMENT_ERROR_PREFIX = "PAY"


class BaseException(Exception):
    code = None
    code_str = None
    display_msg = None
    err_type = None
    msg = None

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        self.code = code
        self.code_str = PAYMENT_ERROR_PREFIX + str(code)
        self.display_msg = display_msg
        self.err_type = err_type
        self.msg = msg


class RequestParamNotAvailable(BaseException):
    code = ErrorCode.MISSING_INPUT_PARAMS
    display_msg = DisplayMsg.OOPS_ERROR_OCCURRED
    err_type = ErrorType.MISSING_INPUT_PARAMS
    msg = "Invalid request"

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        super(RequestParamNotAvailable, self).__init__(code, display_msg, err_type, msg)


class SQLException(BaseException):
    code = ErrorCode.SQL
    display_msg = DisplayMsg.OOPS_ERROR_OCCURRED
    err_type = ErrorType.SQL
    msg = "Error in fetching from DB"

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        super(SQLException, self).__init__(code, display_msg, err_type, msg)


class GenericException(BaseException):
    code = ErrorCode.GENERIC
    display_msg = DisplayMsg.OOPS_ERROR_OCCURRED
    err_type = ErrorType.GENERIC_ERROR
    msg = "Exception occurred while processing"

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        super(GenericException, self).__init__(code, display_msg, err_type, msg)


class AuthenticationError(BaseException):
    code = ErrorCode.AUTHENTICATION
    display_msg = DisplayMsg.OOPS_ERROR_OCCURRED
    err_type = ErrorType.AUTHENTICATION
    msg = "Request could not be authenticated"

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        super(AuthenticationError, self).__init__(code, display_msg, err_type, msg)
