import sys
import errno
import numpy as np
from numpy import arange
import PyQt5
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import socket
import struct
import math 

class Plot2D():
    def __init__(self):
        self.traces = dict()

        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QtGui.QApplication([])
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win.resize(1000, 600)
        self.win.setWindowTitle('EMG')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        self.canvas = self.win.addPlot(title="EMG")
        self.canvas.setYRange(-3, 3, padding=0)
        self.canvas.addLegend(offset=(20, 20))
        self.canvas.setLabel('left', 'mV')
        self.canvas.hideAxis('bottom')



    def start(self):
#        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

    def trace(self, name, dataset_x, dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)

        elif name == "LE":
            self.traces[name] = self.canvas.plot(pen='r', name="Linear Envelope")
        
        elif name == "0.3MVC":
            self.traces[name] = self.canvas.plot(pen='g', name="=0.3 times the Maximum Voluntary Contraction")
        
        elif name == "EMG":
            self.traces[name] = self.canvas.plot(pen='y', fillLevel=20.0, fillOutline=True, name="EMG Biceps")
        
        elif name == "High th":
            self.traces[name] = self.canvas.plot(pen='b', name="High threshold")
            
        elif name == "Low th":
            self.traces[name] = self.canvas.plot(pen='y', name="Low threshold")

#        else:
#            self.traces[name] = self.canvas.plot(pen='y', fillLevel=20.0, fillOutline=True, name="EMG Biceps")