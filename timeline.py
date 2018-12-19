from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsSceneWheelEvent, QGraphicsRectItem, QGraphicsView
from PyQt5.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen


class Timeline(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(GraphicsScene(self))
        a = self.mapToScene(self.viewport().geometry()).boundingRect()
        self.scale((a.width() / 12000) - 0.0005, 1)
        self.currentScale = a.width() / 12000
        self.scaleFactor = 1.05

    def wheelEvent(self, event):
        zoomInFactor = self.scaleFactor
        zoomOutFactor = 1 / zoomInFactor
        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0 and self.currentScale < 1.0:
            zoomFactor = zoomInFactor
            self.currentScale *= zoomFactor
        else:
            zoomFactor = zoomOutFactor
            self.currentScale *= zoomFactor
        self.scale(zoomFactor, 1)
        print(self.currentScale)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())


class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(QtCore.QRectF(0, 0, 120000, 30), parent)
        self._start = QtCore.QPointF()
        self._current_rect_item = None
        rect = Rect()
        self.addItem(rect)


class Rect(QGraphicsRectItem):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        painter.setBrush(QBrush(QColor(255, 0, 0, 100)))
        # painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 0, 0, 255)))

        pen = QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.drawRect(0, 0, 20, 30)

    # def mousePressEvent(self, event):
    #     if self.itemAt(event.scenePos(), QtGui.QTransform()) is None:
    #         self._current_rect_item = QtWidgets.QGraphicsRectItem()
    #         self._current_rect_item.setBrush(QtCore.Qt.red)
    #         self._current_rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
    #         self.addItem(self._current_rect_item)
    #         self._start = event.scenePos()
    #         r = QtCore.QRectF(self._start, self._start)
    #         self._current_rect_item.setRect(r)
    #     super(GraphicsScene, self).mousePressEvent(event)
    #
    # def mouseMoveEvent(self, event):
    #     if self._current_rect_item is not None:
    #         r = QtCore.QRectF(self._start, event.scenePos()).normalized()
    #         self._current_rect_item.setRect(r)
    #     super(GraphicsScene, self).mouseMoveEvent(event)
    #
    # def mouseReleaseEvent(self, event):
    #     self._current_rect_item = None
    #     super(GraphicsScene, self).mouseReleaseEvent(event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        timeline = Timeline(self)
        self.setCentralWidget(timeline)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 100)
    w.show()
    sys.exit(app.exec_())
