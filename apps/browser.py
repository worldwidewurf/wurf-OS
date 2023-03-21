# from contextlib import redirect_stdout
# from io import StringIO
# from PyQt6.QtCore import QUrl
# from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
# from PyQt6.QtWebEngineWidgets import *
# import sys

# with redirect_stdout(StringIO()) as out:
    

#     class MainWindow(QMainWindow):
#         def __init__(self, *args, **kwargs):
#             super(MainWindow,self).__init__(*args, **kwargs)
#             self.browser = QWebEngineView()
#             self.setCentralWidget(self.browser)
#             self.browser.setUrl(QUrl("https://www.google.com"))
#             self.browser.urlChanged.connect(self.update_urlbar)
#             self.browser.loadFinished.connect(self.update_title)
#             self.setCentralWidget(self.browser)
#             self.status = QStatusBar()
#             self.setStatusBar(self.status)
#             navtb = QToolBar("Navigation")
#             self.addToolBar(navtb)
#             # back button
#             back_btn = QAction("Back", self)
#             back_btn.setStatusTip("Back to previous page")
#             back_btn.triggered.connect(self.browser.back)
#             navtb.addAction(back_btn)

#             # forward button
#             forwd_btn = QAction("Forward", self)
#             forwd_btn.setStatusTip("Forward to next page")
#             forwd_btn.triggered.connect(self.browser.forward)
#             navtb.addAction(forwd_btn)

#             # reload button

#             reload_btn = QAction("Reload", self)
#             reload_btn.setStatusTip("Reload page")
#             reload_btn.triggered.connect(self.browser.reload)
#             navtb.addAction(reload_btn)

#             #home btn
#             home_btn = QAction("Home", self)
#             home_btn.setStatusTip("Go home")
#             home_btn.triggered.connect(self.navigate_home)
#             navtb.addAction(home_btn)

#             navtb.addSeparator()
#             self.urlbar = QLineEdit()

#             self.urlbar.returnPressed.connect(self.navigate_to_url)
#             navtb.addWidget(self.urlbar)

#             stop_btn = QAction("Stop", self)
#             stop_btn.setStatusTip("Stop loading current page")
#             stop_btn.triggered.connect(self.browser.stop)
#             navtb.addAction(stop_btn)

#             hstry_btn = QAction("History", self)
#             hstry_btn.setStatusTip("History")
#             hstry_btn.triggered.connect(self.browser.history)
#             navtb.addAction(hstry_btn)


#         def navigate_home(self):
#             self.browser.setUrl(QUrl("https://github.com/worldwidewurf"))

#         def update_urlbar(self, q):
#             self.urlbar.setText(q.toString())
#             self.urlbar.setCursorPosition(0)
        
#         def update_title(self):
#             title = self.browser.page().title()
#             self.setWindowTitle("% s -Worldwidesurf" % title)

#         def navigate_to_url(self):
 
#             q = QUrl(self.urlbar.text())
 
#             if q.scheme() == "":
#                 # set url scheme to html
#                 q.setScheme("http")
    
#             self.browser.setUrl(q)

#     def start_browser():
#         app = QApplication(sys.argv)
#         window = MainWindow()
#         window.show()  
#         sys.exit(app.exec())   
        
#     if __name__ == "__main__":
#         start_browser()