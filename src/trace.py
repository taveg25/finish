#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime


def trace(function):
    def traced_function(*args, **kwargs):
        t0 = datetime.now()
        result = function(*args, **kwargs)
        delta_t = datetime.now() - t0
        delta_t = delta_t.total_seconds()
        name = function.__name__
        logging.debug(f'Функция {name} выполнялась {delta_t} скунд')
        return result
    return traced_function