import os
import sys
import time

from PySide2.QtWidgets import QWidget as widget
from PySide2.QtWidgets import QFileDialog, QErrorMessage
from PySide2.QtMultimediaWidgets import QCameraViewfinder
from PySide2.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo


class Camera(widget):

    def __init__(self):
        super(Camera, self).__init__()
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            pass  # quit

        """
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        """

        self.save_path = ""

        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        #self.setCentralWidget(self.viewfinder)

        # Set the default camera.
        self.select_camera(0)

        """
        # Setup tools
        camera_toolbar = QToolBar("Camera")
        camera_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(camera_toolbar)

        photo_action = QAction(QIcon(os.path.join('images', 'camera-black.png')), "Take photo...", self)
        photo_action.setStatusTip("Take photo of current view")
        photo_action.triggered.connect(self.take_photo)
        camera_toolbar.addAction(photo_action)

        change_folder_action = QAction(QIcon(os.path.join('images', 'blue-folder-horizontal-open.png')),
                                       "Change save location...", self)
        change_folder_action.setStatusTip("Change folder where photos are saved.")
        change_folder_action.triggered.connect(self.change_folder)
        camera_toolbar.addAction(change_folder_action)

        camera_selector = QComboBox()
        camera_selector.addItems([c.description() for c in self.available_cameras])
        camera_selector.currentIndexChanged.connect(self.select_camera)

        camera_toolbar.addWidget(camera_selector)

        self.setWindowTitle("NSAViewer")
        self.show()
        """

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0

    def take_photo(self):
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        self.capture.capture(os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        )))
        self.save_seq += 1

    def change_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Snapshot save location", "")
        if path:
            self.save_path = path
            self.save_seq = 0

    def alert(self, s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)
