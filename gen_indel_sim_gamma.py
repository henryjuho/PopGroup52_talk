#!/usr/bin/env python

from __future__ import print_function
from numpy.random import gamma

cats = ['simulated', 'mean', 'lower', 'upper']
del_scale = [50, 51.201563118, 33.3006675592, 73.9240043467]
del_shape = [0.25, 0.250623830162, 0.223724811743, 0.28095764812]

del_gamma = zip(del_scale, del_shape)

ins_scale = [10, 10.4465253707, 6.44548347542, 16.4478735062]
ins_shape = [0.5, 0.507890462401, 0.397948954934, 0.635674792664]

ins_gamma = zip(ins_scale, ins_shape)

print('gamma', 'var_type', 'data_type', sep='\t')
for x in [['del', del_gamma], ['ins', ins_gamma]]:

    var_type = x[0]
    dataset = x[1]

    for i in range(0, len(dataset)):

        data_type = cats[i]

        sim_gamma = list(gamma(dataset[i][1], dataset[i][0], 10000))

        for y in sim_gamma:
            print(y, var_type, data_type, sep='\t')
