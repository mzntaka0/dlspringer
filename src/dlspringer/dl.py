# -*- coding: utf-8 -*-
"""
"""
import os
import subprocess
import requests
try:
    from bpdb import set_trace
except ImportError:
    from pdb import set_trace

from openpyxl import load_workbook
from tqdm import tqdm


def main(xlsx_path: str):
    output_dir = 'pdfs'
    wb = load_workbook(filename=xlsx_path)
    sheet = wb.active
    col = lambda colomn: ord(colomn) - 97
    for i, s in tqdm(enumerate(sheet)):
        if i == 0:
            continue
        title, category, url = s[col('a')].value, s[col('l')].value, s[col('s')].value
        print(url)
        title = title.lower().replace(' ', '_') + '.pdf'
        category = category.replace(' ', '_')
        r = requests.get(url)
        url = r.url
        url = url.replace('/book/', '/content/pdf/') + '.pdf'
        save_dir = os.path.join(output_dir, category)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        subprocess.run(['aria2c', '-x10', '-s10', '-k1M', url, '-o', os.path.join(save_dir, title)])



if __name__ == '__main__':
    xlsx_path = '../data/Free+English+textbooks.xlsx'
    main(xlsx_path)
