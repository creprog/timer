# -*- coding: utf-8 -*-
import sys
import datetime
import time
import threading
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QCalendarWidget

from ui.window_ui import Ui_MainWindow as window

#right_now=datetime.datetime.now()

class StoppableThread(threading.Thread):
	"""docstring for StoppableThread"""
	def __init__(self, *args, **kwargs):
		super(StoppableThread, self).__init__(*args, **kwargs)
		self._stop_event = threading.Event()

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()
		

total_seconds = 0

timer_stop = 0

class NKMTime(QtWidgets.QMainWindow):
	def __init__(self):
		super(NKMTime, self).__init__()
		self.ui = window()
		self.ui.setupUi(self)
		self.time_start = 0
		self.time_stop = 0
		self.delta = datetime.timedelta()
		self.total = datetime.timedelta()
		self.running = False
		self.timer = False
		self.ui.pushButton.clicked.connect(self.stopwatch)

	def closeEvent(self, event):
		self.timer = False
		print('GOING UNDER')
		event.accept()
		

	def start_timer(self):
		timer_start = datetime.datetime.now()
		self.timer = True
		print(this.stopped())
		while self.timer:
			# time.sleep(1)
			self.delta=datetime.datetime.now()-timer_start
			self.ui.label_current_info.setText(str(self.delta).split('.')[0])
			# print(self.delta)
		
	def stopwatch(self):
		self.timer = False
		# self.t.end()
		if self.running:
			self.running=False
			self.ui.pushButton.setText('START')
			# self.time_stop=datetime.datetime.now()
			# delta = self.time_stop-self.time_start
			self.total+=self.delta
			self.ui.label_total_info.setText(str(self.total))
			t = StoppableThread(target=self.start_timer)
			t.start()
			# self.start_timer()
			self.ui.label_current.setText('Отдыхаем')
		else:
			self.running=True
			self.ui.pushButton.setText('STOP')
			self.time_start=datetime.datetime.now()
			self.ui.label_current.setText('Работаем')
			t = StoppableThread(target=self.start_timer)
			t.start()
			# self.start_timer()

			
		

def main():
	app = QtWidgets.QApplication(sys.argv)
	application = NKMTime()
	application.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()