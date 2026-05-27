"""Plugin: custom Jinja2 filters for date formatting and utilities."""

import datetime

from pelican import signals


def english_date(dt):
    """Format a datetime as 'Mon YYYY' in English, regardless of system locale."""
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    ]
    if isinstance(dt, datetime.datetime):
        return f"{months[dt.month - 1]} {dt.year}"
    return str(dt)


def english_date_full(dt):
    """Format a datetime as 'Month DD, YYYY' in English."""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    if isinstance(dt, datetime.datetime):
        return f"{months[dt.month - 1]} {dt.day}, {dt.year}"
    return str(dt)


def add_filters(generator):
    env = generator.env
    env.filters["eng_date"] = english_date
    env.filters["eng_date_full"] = english_date_full


def register():
    signals.generator_init.connect(add_filters)
