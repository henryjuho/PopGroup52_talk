from __future__ import print_function
import sys


def res2dict(header, data):

    if 'del' in header:
        return None

    header = header.rstrip().split(',')
    data = data.rstrip().split(',')

    res_dict = {}

    for i in range(0, len(header)):

        col_name = header[i]
        col_value = data[i]

        if 'mean' in col_name or 'sim' in col_name:
            try:
                param, c, data_type = col_name.split('_')[0:3]
            except ValueError:
                param, c, data_type = [col_name.split('_')[0], '1', col_name.split('_')[1]]

            if param not in res_dict.keys():
                res_dict[param] = {}

            if c not in res_dict[param].keys():
                res_dict[param][c] = [float('NaN'), float('NaN')]

            if data_type == 'mean':
                res_dict[param][c][1] = float(col_value)

            else:
                res_dict[param][c][0] = float(col_value)

        else:
            continue

    return res_dict


def main():

    for res_file in sys.stdin:

        res = open(res_file.rstrip()).readlines()[0:2]
        print(res_file.rstrip())
        print(res2dict(res[0], res[1]))

    sim_res = ''


if __name__ == '__main__':
    main()
