# -*- coding: utf-8 -*-

import re

SPECIAL_CHAR_RE = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+"
POSITIVE_NUMBER_RE = "\d+"


def valid_string(s):
    return s and s.strip()


def valid_name(s):
    s = re.sub(SPECIAL_CHAR_RE, "", s)
    return s


def valid_positive_number(s):
    return re.match(POSITIVE_NUMBER_RE, s)


