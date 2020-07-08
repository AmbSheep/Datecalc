#!/usr/bin/env python3
import sys
import datetime
from dateutil.parser import parse


def datecalc(start_date, days):
    """
    function to add days to specified date
    :param start_date: date in any format
    :param days: days to add
    :return: returns date after days addition
    """
    date_1 = parse(start_date)
    end_date = date_1 + datetime.timedelta(days=days)
    return end_date


if __name__ == "__main__":
    start_date = input()
    days = int(input())
    print(datecalc(start_date, days).date())
