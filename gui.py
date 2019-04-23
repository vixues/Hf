# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import math
from tkinter import ttk
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename
from tkinter import messagebox
import sys
from calculation import Hf


class Mainwindow():
    
    def __init__(self,master):
        self.master = master
        self.master.resizable(0,0)
        pan_frame = Frame(self.master, width = 185.5, height = 600)
        pan_frame.grid(row = 0, column = 0, padx = 5, pady = 3,sticky=(N, S, E, W))
        pan_frame.grid_propagate(0)
        res_frame = Frame(self.master, width = 600, height = 600)
        res_frame.grid(row = 0,column = 1, padx = 5,pady = 3,sticky=(N, S, E, W))
        hflist = ['beta23', '2se', 'beta79', '2se',
        '176Yb/177Hf(corr)', '2se', '176Lu/177Hf(corr)',
        '2se', '176Hf*/177Hf', '2se', 'Cycle_get']
        self.re = pd.DataFrame()
        self.filename = StringVar()
        self.filename.set('Open Floder')
        self.hf180 = StringVar()
        self.pathlabel = Label(pan_frame, text='Data Location：', background='#2F2F2F', foreground='White')
        self.pathlabel.pack(side=TOP, padx=5, pady=3, fill=X)
        Button(pan_frame,text = 'Choose Data Floder',
        command = lambda:self.choose_path(self.filename,self.pathlabel)).pack(side=TOP, padx=5, pady=3, fill=X)
        Label(pan_frame,text = 'Data to delete：Hf180 <', background = '#2F2F2F',
        foreground='White').pack(side=TOP, padx=5, pady=3, fill=X)
        Entry(pan_frame,textvariable = self.hf180).pack(side=TOP, fill=X, padx=5, pady=3)
        Button(pan_frame, text='Calculation',
        command=self.calculation, background='#B13254', foreground='White').pack(side=TOP,
        padx = 5,pady = 3,fill = X)
        self.text = Text(pan_frame,width=30, height=5, bd=1)
        self.text.pack(side=TOP, padx=5, pady=3, fill=X)
        Button(pan_frame, text='Save Date', command=self.save).pack(side=TOP, padx=5, pady=3, fill=X)
        Button(pan_frame, text='Exit', command=self.exit).pack(side=BOTTOM, padx=5,pady=3, fill=X)

        bary = Scrollbar(res_frame)
        bary.pack(side=RIGHT, fill=Y)
        self.resultList = ttk.Treeview(res_frame, columns=hflist, height=30)
        self.resultList.column(column='#0', width=140)
        self.resultList.heading('#0', text="Sample")
        for i in range(len(hflist)):
            self.resultList.heading(i, text=hflist[i], anchor=E)
            self.resultList.column(i, minwidth=20, width=80, anchor=E)
        self.resultList.pack(side=TOP, fill=BOTH, expand=YES)
        bary.config(command=self.resultList.yview)
        self.resultList.config(yscrollcommand = bary.set)

    def choose_path(self, filename, label):
        fdir = askdirectory()
        filename.set(fdir)
        fn = fdir.split("/")
        label.config(text = "Work Floder:%s" % fn[-1])

    def calculation(self):
        hfdir = self.filename
        hf180 = float(self.hf180.get())
        hffilelist_unsorted = self.scan_file(hfdir.get(), postfix = '.exp')
        hffilelist = sorted(hffilelist_unsorted)
        i = 0
        table_tmp = pd.DataFrame()
        for items in hffilelist:
            filename = str(items)
            tmp = items.split('.')
            name = tmp[0]
            hffile = os.path.join(hfdir.get(),filename)
            df = Hf(hffile, hf180)
            resultname = os.path.join(hfdir.get(), name + '.xls')
            num = df.datanumber
            try:
                df2 = df.cal()
                r = df.report(name)
                table_tmp = table_tmp.append(r, ignore_index=True)
                datatoshow = r.iloc[0].tolist()[1:]
                dataf = list(map(lambda x:'%2.7f' % x, datatoshow[0:-1]))
                dataf.append(num)
                self.resultList.insert('', i, text=name, values=tuple(dataf))
            except:
                data = ['some', 'thing', 'wrong', '', '', '', '', '', '', '', '']
                self.resultList.insert('', i, text=name, values=tuple(data))
        self.re = table_tmp
        spl = ('', '', '', '', '', '', '', '', '', '', '')
        self.resultList.insert('', 0, text='↘︎', values=spl, tags='head')
        self.resultList.tag_configure('head', background='#FF7349')
        table_tmp = pd.DataFrame()

    def save(self):
        file = asksaveasfilename(defaultextension = '.xls')
        self.re.to_excel(str(file))

    def exit(self):
        self.master.destroy()

    def scan_file(self, directory, postfix = None):
        file_list = [file for file in os.listdir(directory) if file.endswith(posfix)]
        return files_list