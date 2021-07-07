from .models import get_session


class DBAdapter(object):
    def __init__(self, session=None):
        self._db_session = session or get_session()