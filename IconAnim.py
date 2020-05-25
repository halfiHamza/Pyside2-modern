# Example from iconify Quick start
# Iconify web page link: https://pypi.org/project/iconify/


from iconify.qt import QtCore, QtGui
from iconify.qt import QtWidgets as icoWidget

class IconifyLabel(icoWidget.QLabel):

    def __init__(self, pixmapGenerator):
        super(IconifyLabel, self).__init__()
        self._pixmapGenerator = pixmapGenerator

        # Ensure this label updates when the animation ticks.
        self._pixmapGenerator.anim().tick.connect(self.update)

    def paintEvent(self, event):
        super(IconifyLabel, self).paintEvent(event)

        rect = event.rect()

        if rect.width() > rect.height():
            size = QtCore.QSize(rect.height(), rect.height())
        else:
            size = QtCore.QSize(rect.width(), rect.width())

        pixmap = self._pixmapGenerator.pixmap(size)

        painter = QtGui.QPainter(self)
        halfSize  = size / 2
        point = rect.center() - QtCore.QPoint(halfSize.width(), halfSize.height())
        painter.drawPixmap(point, pixmap)
        painter.end()
