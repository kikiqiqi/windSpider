# -*-coding:utf-8 -*-
import pandas as pd
from wind_code import getWindCode

if __name__ == "__main__":
    bonds = pd.read_csv("bonds.csv")
    bonds_lst = bonds["债券名称"].tolist()

    offset = 0

    f = open("tag_code.txt", "a")
    for i in range(offset, len(bonds_lst)):
        tag_code = getWindCode(bonds_lst[i])
        if tag_code:
            f.write(bonds_lst[i] + "," + tag_code[0] + "\n")
        else:
            break

    print(i)
    f.close()
