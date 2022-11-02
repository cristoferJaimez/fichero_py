# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:19:09 2022

@author: cjaimez
"""

import os

class ListenDir:
    
    dirFile = []
    urlDir = []
    
    def listenDir(self):
        content = os.listdir('./')
        print('Select Documet:')
        for item in content:
            #self.dirFile.append(os.path.dirname(os.path.abspath(item)))
            root, ext = os.path.splitext(item)
            if ext == '.xlsx' or ext == '.csv':
                self.dirFile.append(item)
                self.urlDir.append(os.path.abspath(item))
            
        for i, item_ in enumerate(self.dirFile) :
            print(i, ':)', item_)
            
        option = input("Enter: ")
        option = option.strip()
        
        return self.urlDir[int(option)]
