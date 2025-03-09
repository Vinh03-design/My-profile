import sys
import cv2
import numpy as np


from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from Gui import Ui_MainWindow  # Đảm bảo bạn đã import đúng giao diện


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.khungCamera.setFixedSize(476, 388)

        # Kết nối tín hiệu từ SwitchControl đến hàm toggle_capture_video
        self.uic.switch_control.stateChanged.connect(self.toggle_capture_video)

        # Kết nối tín hiệu từ stackedWidget đến cái màn hình driving
        self.uic.stackedWidget.setCurrentWidget(self.uic.driving)

        self.uic.driving_btn.clicked.connect(self.showScreen_1)
        self.uic.map_btn.clicked.connect(self.showScreen_2)

        self.thread = {}


    # Kết nối nút bấm với màn hình cần hiện
    def showScreen_1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.driving)

    # Kết nối nút bấm với màn hình cần hiện
    def showScreen_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.map)


    def closeEvent(self, event):
        """Xử lý khi cửa sổ đóng"""
        self.stop_capture_video()

    def stop_capture_video(self):
        """Dừng video capture"""
        if 1 in self.thread:
            self.thread[1].stop()

    def start_capture_video(self):
        """Bắt đầu video capture"""
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)

    def show_wedcam(self, cv_img):
        """Cập nhật label với hình ảnh mới từ webcam"""
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.khungCamera.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Chuyển đổi hình ảnh OpenCV sang QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def toggle_capture_video(self, state):
        """Kích hoạt hoặc dừng video capture khi trạng thái của SwitchControl thay đổi"""
        if state == Qt.Checked:  # Khi bật
            self.start_capture_video()
        else:  # Khi tắt
            self.stop_capture_video()


class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv2.VideoCapture(0)  # Chế độ lấy ảnh từ webcam
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.signal.emit(cv_img)

    def stop(self):
        print("stop threading", self.index)
        self.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
