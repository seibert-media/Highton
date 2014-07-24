import re
import datetime


def to_datetime(datetime_string):
    match = re.match(
        '^(.*)-(.*)-(.*)( |T)(.*):(.*):(.*)(\+|Z).*$', datetime_string)
    if match:
        return datetime.datetime(
            year=int(match.group(1)),
            month=int(match.group(2)),
            day=int(match.group(3)),
            hour=int(match.group(5)),
            minute=int(match.group(6)),
            second=int(match.group(7)),
        )
    else:
        return None


def to_date(date_string):
    match = re.match('^(.*)-(.*)-(.*)$', date_string)
    if match:
        return datetime.datetime(
            year=int(match.group(1)),
            month=int(match.group(2)),
            day=int(match.group(3)),
        ).date()
