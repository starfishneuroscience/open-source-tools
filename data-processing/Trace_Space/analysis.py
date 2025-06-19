import sys
import os
import json
import cv2
from PyQt6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, QPointF

template = cv2.imread("Origin.jpg", cv2.IMREAD_GRAYSCALE)
template_h, template_w = template.shape


class MainWindow(QMainWindow):
    def __init__(self, results_location):
        super().__init__()

        with open(results_location, "r") as f:
            data = json.load(f)

        self.setWindowTitle("Trace Image Viewer")
        self.wafer_data = data
        self.wafer_index = 1
        self.device_index = 0
        self.pixel_to_um = None
        self.rectangles = []  # stores: {'index': i, 'rect': (x1, y1, x2, y2), 'active': True}

        # UI elements
        self.header_label = QLabel()
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.installEventFilter(self)

        self.log_label = QLabel()
        self.log_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.log_label.setStyleSheet("font-size: 14px; color: gray;")

        # Navigation buttons
        prev_button = QPushButton("Previous")
        next_button = QPushButton("Next")
        prev_button.clicked.connect(self.show_previous_image)
        next_button.clicked.connect(self.show_next_image)

        button_layout = QHBoxLayout()
        button_layout.addWidget(prev_button)
        button_layout.addWidget(next_button)

        # Layout setup
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header_label)
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.log_label)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show_image()
        self.showMaximized()

    def log_message(self, message):
        print(message)
        self.log_label.setText(message)

    def eventFilter(self, source, event):
        if source == self.image_label and event.type() == event.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.handle_click(event)
            return True
        return super().eventFilter(source, event)

    def show_image(self):
        wafer_name = self.wafer_data["wafers"][self.wafer_index]["name"]
        self.pixel_to_um = self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["pixel_to_um_scale"]
        device_name = self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["device_name"]
        image_path = self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["image_location"]
        origin_pixel_offset = self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index].get("origin_pixel_offset", [])

        self.header_label.setText(f"{wafer_name} — {device_name}")

        # Compute offset if missing
        if not origin_pixel_offset:
            self.log_message("Computing Origin Offset...")
            self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["origin_pixel_offset"] = self.get_origin_pixel_offset(image_path)
            origin_pixel_offset = self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["origin_pixel_offset"]
            self.log_message(f"Computed offset: {origin_pixel_offset}")

        if os.path.exists(image_path):
            image = cv2.imread(image_path)

            # Draw rectangle if offset found
            if origin_pixel_offset:
                x, y = origin_pixel_offset
                x_offset = round(100/self.pixel_to_um)
                y_offset = round(350/self.pixel_to_um)
                self.rectangles.clear()

                for trace_index, trace in enumerate(self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["traces"]):
                    col_index = (trace_index // 9)
                    row_index = (trace_index % 9)
                    row = 9 - row_index
                    col = 4 - col_index
                    x1 =  x - 25 + row_index*x_offset
                    y1 = y - col_index*y_offset
                    x2 = x+template_w + row_index*x_offset
                    y2 = y + template_h - col_index*y_offset +25
                    rect = (x1,y1,x2,y2)
                    self.rectangles.append({'index': trace_index,'trace':f"{row} x {col}", 'rect': rect, 'result': trace.get("result", True)})

                    # Draw rectangle
                    color = (0, 255, 0)
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, 1)

                    # Draw label
                    cv2.putText(image, f"{row} x {col} : {trace_index}", (x1, y2 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                    # Draw X if active
                    if not self.rectangles[-1]["result"]:
                        cv2.putText(image, "X", (x1, y1 + (template_h // 2)+75), cv2.FONT_HERSHEY_SIMPLEX, 7.0, (0, 0, 255), 2)
                        # cv2.putText(image,"X", (x - 25 + row_index*x_offset,round(y + template_h/2 - col_index*y_offset +50)),cv2.FONT_HERSHEY_SIMPLEX, 7, (0, 0, 255), 3)

            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText(f"Image not found:\n{image_path}")

    def handle_click(self, event):
        pos: QPointF = event.position()
        label_size = self.image_label.size()
        pixmap = self.image_label.pixmap()
        if not pixmap:
            return

        x_ratio = pixmap.width() / label_size.width()
        y_ratio = pixmap.height() / label_size.height()
        x_click = int(pos.x() * x_ratio)
        y_click = int(pos.y() * y_ratio)

        for rect in self.rectangles:
            x1, y1, x2, y2 = rect["rect"]
            if x1 <= x_click <= x2 and y1 <= y_click <= y2:
                rect["result"] = not rect["result"]
                trace_index = rect["index"]
                self.wafer_data["wafers"][self.wafer_index]["devices"][self.device_index]["traces"][trace_index]["result"] = rect["result"]
                self.log_message(f"Toggled trace {rect['trace']} to {'active' if rect['result'] else 'inactive'}")
                self.show_image()
                break

    def show_next_image(self):
        self.save_data()
        # print(f"{self.device_index}:{len(self.wafer_data['wafers'][self.wafer_index]['devices'])-1}")
        # self.log_message(f"{self.device_index}:{len(self.wafer_data['wafers'][self.wafer_index]['devices'])-1}")
        if(self.device_index < len(self.wafer_data["wafers"][self.wafer_index]["devices"])-1):
            self.device_index += 1
        else:
            if self.wafer_index < len(self.wafer_data['wafers'])-1:
                print("Next Wafer: ", self.wafer_index)
                self.wafer_index +=1
            else:
                self.wafer_index = 0
            self.device_index = 0
        self.show_image()

    def show_previous_image(self):
        self.save_data()
        if self.device_index > 0:
            self.device_index -= 1
        else:
            if self.wafer_index == 0:
                self.wafer_index = len(self.wafer_data['wafers'])-1
            else:
                self.wafer_index -= 1
            self.device_index = len(self.wafer_data['wafers'][self.wafer_index]['devices'])-1
            self.show_image()

    def save_data(self):
        self.log_message("Data Saved")
        with open("results.json", "w") as f:
            json.dump(self.wafer_data, f, indent=4)

    def get_origin_pixel_offset(self, image_path):
        self.log_message("Finding Origin Offset")
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            self.log_message(f"Could not load image: {image_path}")
            return []

        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        return max_loc

    def closeEvent(self, event):
        self.save_data()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow("results.json")
    sys.exit(app.exec())
