import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')

#recent_tableの記事番号を更新
def update_recent_table(table_num):
    with open('config.ini', 'r') as f:
        lines = f.readlines()
    with open('config.ini', 'w') as f:
        for line in lines:
            if re.match(r'(recent_table = )', line):
                f.write("recent_table = {}".format(table_num))
                continue
            f.write(line)
