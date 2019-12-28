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
		self.timer_work = False
		self.timer_rest = False
		self.ui.pushButton.clicked.connect(self.stopwatch)

	def closeEvent(self, event):
		self.timer_work = False
		self.timer_rest = False
		print('GOING UNDER')
		event.accept()
		

	def start_timer(self):
		timer_start = datetime.datetime.now()
		# print(this.stopped())
		if self.running:
			while self.timer_work:
				# time.sleep(1)
				self.delta=datetime.datetime.now()-timer_start
				self.ui.label_current_info.setText(str(self.delta).split('.')[0])
				time.sleep(1)
		else:
			while self.timer_rest:
				# time.sleep(1)
				self.delta=datetime.datetime.now()-timer_start
				self.ui.label_current_info.setText(str(self.delta).split('.')[0])
				time.sleep(1)
			# print(self.delta)
		
	def stopwatch(self):
		self.timer = False
		# self.t.end()
		if self.running:
			self.ui.label_current.setText('Отдыхаем')
			self.ui.pushButton.setText('START')
			self.running=False
			self.timer_work = False
			self.timer_rest = True
			self.total+=self.delta
			self.ui.label_total_info.setText(str(self.total).split('.')[0])
			t = StoppableThread(target=self.start_timer)
			t.start()
			# self.start_timer()
			
		else:
			self.ui.label_current.setText('Работаем')
			self.ui.pushButton.setText('STOP')
			self.running=True
			self.timer_work = True
			self.timer_rest = False
			self.time_start=datetime.datetime.now()
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