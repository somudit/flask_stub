import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

SECRET_KEY = os.getenv("SECRET_KEY", "QZSDKFMNSEKFN")
WTF_CSRF_SECRET_KEY = os.getenv("WTF_CSRF_SECRET_KEY", 'uiiojnklnjjjhh')
DEBUG = os.getenv("DEBUG", True)
SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", False)
DBUSER = os.getenv("DBUSER", "root")
DBPASSWORD = os.getenv("DBPASSWORD", "root")
DBHOST = os.getenv("DBHOST", "localhost")
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DBUSER}:{DBPASSWORD}@{DBHOST}/test"
PERMANENT_SESSION_LIFETIME = 15780000
SESSION_TYPE = "filesystem"

LOGS_DIR = os.path.join(os.path.abspath(os.path.join(ROOT_DIR, os.pardir)),
                        'logs')
DEFAULT_LOG_LEVEL = os.getenv('DEFAULT_LOG_LEVEL', 'INFO')
CONSOLE_LOGGER = 'console_logger'
PAYMENT_LOG_LEVEL = os.getenv('PAYMENT_LOG_LEVEL', 'INFO')
PAYMENT_LOGGER = 'PaymentLogger'
PAYMENT_REQ_LOGGER = 'PaymentReqLogger'
PAYMENT_SERVICE_LOG = 'payment_service.log'

LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    },
    'handlers': {
        'consolehandler': {
            'level': DEFAULT_LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'console_format',
            'stream': "ext://sys.stdout",
        },
        'payment_log_handler': {
            'level': PAYMENT_LOG_LEVEL,
            'class': os.getenv('LOGGING_CLASS', 'logging.StreamHandler'),
            'formatter': 'bbloggerformat',
        },
        'payment_req_log_handler': {
            'level': PAYMENT_LOG_LEVEL,
            'class': os.getenv('LOGGING_CLASS', 'logging.StreamHandler'),
            'formatter': 'bbreqloggerformat',
        },
    },
    'loggers': {
        CONSOLE_LOGGER: {
            'handlers': ['consolehandler'],
            'level': DEFAULT_LOG_LEVEL,
            'propagate': True
        },
        PAYMENT_LOGGER: {
            'handlers': ['payment_log_handler'],
            'level': PAYMENT_LOG_LEVEL,
            'propagate': True
        },
        PAYMENT_REQ_LOGGER: {
            'handlers': ['payment_log_handler'],
            'level': PAYMENT_LOG_LEVEL,
            'propagate': True
        },

    },
    'formatters': {
        'console_format': {
            'format': '[%(asctime)s CID:%(context_id)s LL:%(levelname)s T:%(threadName)s] %(message)s'
        },
        'bbloggerformat': {
            'format': '[%(asctime)s LL:%(levelname)s T:%(threadName)s F:%(funcName)s'
                      'PID:%(process)d] %(message)s'
        },
        'bbreqloggerformat': {
            # TODO queue name, partition name should log as well
            'format': '[%(asctime)s LL:%(levelname)s T:%(threadName)s F:%(funcName)s'
                      ' Q:%(queue)s T:%(task_id) PID:%(process)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    }
}

CACHE_TTL = int(os.getenv("CACHE_TTL", 72000))

DOMAIN_URL = os.getenv('DOMAIN_URL', 'http://127.0.0.1:5000')

MICRO_SERVICE_BASE_URL = os.getenv('MICRO_SERVICE_BASE_URL',
                                   "http://dev-svc.bigbasket.com")
