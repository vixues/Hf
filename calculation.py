# -*- coding: UTF-8 -*-
import pandas as pd
from Napture import Napture
import math


class Hf():

    def __init__(self, file, hf180):
        self.filename = file
        machine_type = Napture()
        machine_type.set_hf(hf180)
        machine_type.open(self.filename, encoding='ascii')
        self.df = machine_type.getdata()
        self.df = self.df[self.df.iloc[:, -1] > hf180]]
        self.datanumber = len(self.df)
    
    def cal(self):
        self.df['beta2/3'] = (self.df['172Yb']/self.df['173Yb']).apply(lambda x:math.log(1.35274/x))/math.log(171.936378/172.938208)
        self.df['beta7/9'] = (self.df['177Hf']/self.df['179Hf']).apply(lambda x:math.log(1/0.7325/x))/math.log(176.943217/178.945812)
        self.df['176Yb'] = self.df['172Yb'] * math.pow(171.936378/175.942564, self.df['beta2/3'].mean())*0.588596
        self.df['176Lu'] = self.df['175Lu'] * math.pow(174.94077/175.942679, self.df['beta2/3'].mean())*0.02658
        self.df['176Hf*'] = self.df['176Hf'] - self.df['176Yb'] - self.df['176Lu']
        self.df['176Yb/177Hf'] = self.df['176Yb']/self.df['177Hf'] * self.df['beta7/9'].apply(lambda x:math.pow(175.942564/176.943217,x))
        self.df['176Lu/177Hf'] = self.df['176Lu']/self.df['177Hf'] * self.df['beta7/9'].apply(lambda x:math.pow(175.946279/176.943217,x))
        self.df['176Hf*/177Hf'] = self.df['176Hf*']/self.df['177Hf'] * math.pow(175.941406/176.943217,self.df['beta7/9'].mean())
        mean = self.df.mean()
        sd = self.df.std()
        rsd = sd/mean
        count = self.df.count()
        count.astype(float)
        count_sqrt = count.apply(math.sqrt)
        se = 2 * sd / count_sqrt
        rse = se / mean
        self.df = self.df.append(pd.DataFrame(data = mean).rename(columns = {0:'Mean'}).T)
        self.df = self.df.append(pd.DataFrame(data = sd).rename(columns = {0:'SD'}).T)
        self.df = self.df.append(pd.DataFrame(data = rsd).rename(columns = {0:'RSD'}).T)
        self.df = self.df.append(pd.DataFrame(data = se).rename(columns = {0:'2SE'}).T)
        self.df = self.df.append(pd.DataFrame(data = rse).rename(columns = {0:'2RSE'}).T)
        return self.df 
    
    def report(self,filename):
        sample = str(filename)
        beta23 = self.df.loc['Mean','beta2/3']
        sigma1 = self.df.loc['2SE','beta2/3']
        beta79 = self.df.loc['Mean','beta7/9']
        sigma2 = self.df.loc['2SE','beta7/9']
        Yb176Hf177 = self.df.loc['Mean','176Yb/177Hf']
        sigma3 = self.df.loc['2SE','176Yb/177Hf']
        Lu176Hf177 = self.df.loc['Mean','176Lu/177Hf']
        sigma4 = self.df.loc['2SE','176Lu/177Hf']
        Hf176Hf177 = self.df.loc['Mean','176Hf*/177Hf']
        sigma5 = self.df.loc['2SE','176Hf*/177Hf']
        number = self.datanumber
        final = {
        'Sample':sample,
        '𝛽2/3':beta23,
        '2𝜎1':sigma1,
        '𝛽7/9':beta79,
        '2𝜎2':sigma2,
        '176Yb/177Hf(corr)':Yb176Hf177,
        '2𝜎3':sigma3,
        '176Lu/177Hf(corr)':Lu176Hf177,
        '2𝜎4':sigma4,
        '176Hf*/177Hf':Hf176Hf177,
        '2𝜎5':sigma5,
        'Cycle_get':number
        }
        result = pd.DataFrame(data=final, index=['0'], columns = [
            'Sample','𝛽2/3','2𝜎1','𝛽7/9','2𝜎2','176Yb/177Hf(corr)','2𝜎3',
            '176Lu/177Hf(corr)','2𝜎4','176Hf*/177Hf','2𝜎5','Cycle_get'])
        return result 