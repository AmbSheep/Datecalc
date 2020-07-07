#!/usr/bin/env python3
import sys
import datetime


def datecalc(start_date, days):
    date_1 = datetime.datetime.strptime(start_date, "%d-%m-%Y")
    end_date = date_1 + datetime.timedelta(days=days)
    return end_date.strftime("%d-%m-%Y")


if __name__ == "__main__":
    start_date = sys.argv[1]
    days = int(sys.argv[2])
    print(datecalc(start_date, days))
