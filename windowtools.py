def incenter(w1,h1):
	import tkinter
	tk=Toplevel()
	w=tk.winfo_screenwidth()
	h=tk.winfo_screenheight()
	w=w-w1/2
	h=h-h1/2
	tk.destroy()
	return w,h
def qtmainwindow(windowclass):
	import sys
	from PyQt5 import QtWidgets
	app=QtWidgets.QApplication(sys.argv)
	main=windowsclass()
	main.show()
	sys.exit(app.exec_())
