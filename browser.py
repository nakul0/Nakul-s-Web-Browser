import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize the browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Update window title when page title changes
        self.browser.titleChanged.connect(self.update_title)
        self.browser.urlChanged.connect(self.update_url)
        self.browser.loadProgress.connect(self.update_progress)

        # Navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Stop loading button
        stop_btn = QAction('Stop', self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)

    def navigate_home(self):
        """Navigate to the homepage."""
        self.browser.setUrl(QUrl('https://github.com/nakul0'))

    def navigate_to_url(self):
        """Navigate to the URL entered in the URL bar."""
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        """Update the URL bar when the URL changes."""
        self.url_bar.setText(q.toString())

    def update_title(self, title):
        """Update the window title."""
        self.setWindowTitle(f'{title} - Nakuls browser')

    def update_progress(self, progress):
        """Update the status bar with the loading progress."""
        self.status.showMessage(f'Loading... {progress}%')
        if progress == 100:
            self.status.clearMessage()


# Main application
app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()
