#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

s = "123*&sadf sdf13770976666Aa13770976677df12ssdf"

match_re = ".*?((13|15)\d{9}).*"

phone = re.match(match_re, s)
type(phone)
for i in phone.group:
    print i
# if phone:
#     phone = phone.group(1)
#     print phone.group(2)

# print phone