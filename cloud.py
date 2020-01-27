from binaryninjaui import DockContextHandler, DockHandler
from PySide2.QtCore import Qt
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget

class CloudDockWidget(QWidget, DockContextHandler):
    def __init__(self, parent, name, view):
        QWidget.__init__(self, parent)
        DockContextHandler.__init__(self, self, name)
        layout = QGridLayout(self)
        webview = QWebEngineView()
        webview.load("https://cloud.binary.ninja")
        layout.addWidget(webview, 0, 0)

    def notifyViewChanged(self, view_frame):
        self.view_frame = view_frame

    @staticmethod
    def create_widget(name, parent, data=None):
        return CloudDockWidget(parent, name, data)

def addDockWidget():
    if len(QApplication.allWidgets()) == 0:
        return
    w = QApplication.allWidgets()[0].window()
    w.findChild(DockHandler, '__DockHandler').addDockWidget("Cloud", CloudDockWidget.create_widget)
