class DisplayMsg(object):
    OOPS_ERROR_OCCURRED = "Oops! An Error occurred while processing your request!"


class ErrorCode(object):
    MISSING_INPUT_PARAMS = 1000
    SQL = 1001
    GENERIC = 1002
    AUTHENTICATION = 1003


class ErrorType(object):
    GENERIC_ERROR = "Generic"
    SQL = "Sql"
    AEROSPIKE = "Aerospike"
    JSON = "Json"
    THIRD_PARTY_API = "ThirdPartyAPI"
    AUTHENTICATION = "Authentication"
    MISSING_INPUT_PARAMS = "MissingInputParams"