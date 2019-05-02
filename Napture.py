# -*- coding: UTF-8 -*-
import pandas as pd


class Napture(object):

    def __init__(self):
        self.filename = None
        self.file = None
    
    def open(self, filename, encoding=None):
        self.filename = filename
        self.file = open(self.filename, 'r', buffering= -1, encoding = encoding)

    def getdata(self):
        tmp = open(self.filename, 'r', buffering= -1, encoding = 'ascii')
        count = -1
        for count,line in enumerate(tmp):
            index = line.split()[:10]
            if 'Cycle' in index: # save the position of data in count, the index will be the column name.
                break
            count += 1
        i = 0
        tmp.close()
        dataframe = pd.DataFrame(data = None,index = None,columns = index)
        for line in open(self.filename,'r',buffering = -1,encoding = 'ascii'):
            if i >= count + 1: # skip the header and read from count
                data = line.split()[:10]
                if '***' in data: # read until the end of data
                    break
                dataframe = dataframe.append(pd.DataFrame(data = [data], columns = index), ignore_index = True)
            i += 1
        return dataframe.iloc[:,2:].astype(float)
