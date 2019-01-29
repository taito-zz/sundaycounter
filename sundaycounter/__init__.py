import argparse
import logging

from logging.config import dictConfig


def days_of_month_of_year(year):
    """List days of months in a year

    :param int year: Year like 1900
    :rtype: list
    """
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # February has 29 days
        days_of_feb = 29
    else:
        days_of_feb = 28

    return [31, days_of_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_of_one_year(year):
    """Number of days in a year

    :param int year: Year like 1900
    :rtype: int
    """
    return sum(days_of_month_of_year(year))


def new_sunday(date):
    """Next sunday against a date

    :param tuple date: Date like: (1900, 1, 2)
    :rtype tuple: (1900, 1, 7)
    """
    year, month, day = date
    days_of_months = days_of_month_of_year(year)
    days_from_months = sum(days_of_months[:month - 1])
    days_from_years = sum([days_of_one_year(one_year) for one_year in range(1900, year)])
    days = day + days_from_months + days_from_years
    remain = 7 - days % 7
    days_in_month = days_of_months[month - 1]
    if day + remain <= days_in_month:
        day += remain
    elif month == 12:
        year += 1
        month = 1
        day = day + remain - days_in_month
    else:
        day = day + remain - days_in_month
        month += 1

    return (year, month, day)


def int_date(date):
    """
    :param str date: Date like: 25.1.2001
    :rtype tuple: (25, 1, 2001)
    """
    day, month, year = [int(part) for part in date.split('.')]
    return year, month, day


def list_sundays(start, end, reverse=False):
    """
    :param str start: Start date like: 25.1.2001
    :param str end: End date like: 25.1.2010
    :param bool reverse: Show Sundays in reverse order or not
    """
    sundays = []
    next_sunday = new_sunday(start)
    while next_sunday < end:
        sundays.append('{}.{}.{}'.format(next_sunday[2], next_sunday[1], next_sunday[0]))
        next_sunday = new_sunday(next_sunday)

    if reverse:
        sundays.reverse()

    return sundays


def countsundays():
    parser = argparse.ArgumentParser(description='Print date of Sundays between two dates')
    parser.add_argument(
        '-s', '--start',
        required=True,
        help='Start date (Not earlier than 1.1.1900)',
    )
    parser.add_argument(
        '-e', '--end',
        required=True,
        help='End date (Not later than 1.1.2500)',
    )
    parser.add_argument(
        '-r', '--reverse',
        required=False,
        default=False,
        action='store_true',
        help='Print in reverse order',
    )
    parser.add_argument(
        '-p', '--path',
        required=False,
        help='Print to this file path',
    )
    args = parser.parse_args()

    # Logging
    logger = logging.getLogger(__name__)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            __name__: {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            },
        },
    }

    if args.path:
        LOGGING['handlers']['file'] = {
            'class': 'logging.FileHandler',
            'filename': args.path,
        }
        LOGGING['loggers'][__name__]['handlers'] = ['file']

    dictConfig(LOGGING)

    start = int_date(args.start)
    end = int_date(args.end)
    warned = False

    if start < (1900, 1, 1):
        logger.warn('Start date must be between 1.1.1900 and 1.1.2500')
        warned = True
    if end > (2500, 1, 1):
        logger.warn('End date must be between 1.1.1900 and 1.1.2500')
        warned = True
    if end < start:
        logger.warn('End date must be later than start date')
        warned = True

    if warned is False:
        sundays = list_sundays(start, end, reverse=args.reverse)
        for sunday in sundays:
            logger.info(sunday)
