import csv,sys
import os
from os import listdir
from os.path import isfile, join


dir_path = os.path.dirname(os.path.realpath(__file__))
onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

print(onlyfiles)

for afile in onlyfiles:
    if (afile.endswith('.csv')):
        with open(afile, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count = len(data)
            print('file %s, row count is %d' % (afile, row_count))
            f.seek(0)
            try:
                for row in reader:
                    print(row)
            except csv.Error as e:
                print('file %s, line %d: %s' % (afile, reader.line_num, e))
                continue


