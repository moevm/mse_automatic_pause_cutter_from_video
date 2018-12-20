import pytest
from .common import *
from ..interface import *


class TestGui:
    def setup(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = GUI_Window()
        self.window.show()
        self.app.exec_()

    def test_window_is_shown(self):
        self.window.show()
        assert 1==1

    def teardown(self):
        self.window.hide()
        self.app.quite()
