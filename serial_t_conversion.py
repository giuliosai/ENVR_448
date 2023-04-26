#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:07:22 2023

@author: giuliosaibene
"""

import pandas as pd

#best method using a reference time and subtracting each time object by it
def date_to_serialtime(time):
    ref_datetime = pd.Timestamp("1970-01-01")
    return (time - ref_datetime).dt.total_seconds()
