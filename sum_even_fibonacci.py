#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:25:51 2023

@author: jascha
"""

import numpy as np


def get_sum_even_fibonaccis_below_number(number):
    PHI = (1+np.sqrt(5))/2
    even_fibonacci_index_below_number = int(np.floor(np.floor(np.log(np.sqrt(5)*(number + 0.5))/np.log(PHI))/3))    
    return np.sum(np.round(np.cumprod(np.ones((even_fibonacci_index_below_number,))*PHI**3)/np.sqrt(5)))

    
if __name__=='__main__':
    number = 4000000
    print(get_sum_even_fibonaccis_below_number(number))