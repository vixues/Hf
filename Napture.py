# -*- coding: UTF-8 -*-
import pandas as pd


class Napture(object):

    def __init__(self):
        self.filename = None
        self.file = None
        self.hf180 = 0
    
    def open(self, filename, encoding=None):
        self.filename = filename
        self.file = open(self.filename, 'r', buffering= -1, encoding = encoding)

    def set_hf(self, value):
        self.hf180 = value

    def getdata(self):
        tmp = open(self.filename, 'r', buffering= -1, encoding = 'ascii')
        count = -1
        num = 0
        for count,line in enumerate(tmp):
            index = line.split()[:10]
            if 'Cycle' in index:
                break
            count += 1
        i = 0
        tmp.close()
        dataframe = pd.DataFrame(data = None,index = None,columns = index)
        for line in open(self.filename,'r',buffering = -1,encoding = 'ascii'):
            if i >= count + 1:
                data = line.split()[:10]
                if '***' in data:
                    break
                if float(data[9]) > float(self.hf180): # Only value greater than the presetting Hf180 will be imported.
                    dataframe = dataframe.append(pd.DataFrame(data = [data], columns = index),ignore_index = True)
                    num += 1 # num: cycle get
            i += 1
        #print(dataframe)
        return dataframe.iloc[:,2:].astype(float), num
