import sys
import os
import json
from PyQt6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, image_entries):
        super().__init__()
        self.setWindowTitle("Trace Image Viewer")
        self.image_entries = image_entries
        self.current_index = 0

        # UI elements
        self.header_label = QLabel()
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)

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
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show_image()
        self.showMaximized()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Right:
            self.show_next_image()
        elif event.key() == Qt.Key.Key_Left:
            self.show_previous_image()

    def show_image(self):
        entry = self.image_entries[self.current_index]
        wafer_name = entry["wafer_name"]
        device_name = entry["device_name"]
        image_path = entry["image_path"]

        self.header_label.setText(f"{wafer_name} — {device_name}")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText(f"Image not found:\n{image_path}")

    def show_next_image(self):
        if self.current_index < len(self.image_entries) - 1:
            self.current_index += 1
            self.show_image()

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()


def load_image_entries(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    entries = []
    for wafer in data.get("wafers", []):
        wafer_name = wafer.get("name")
        for device in wafer.get("devices", []):
            entries.append({
                "wafer_name": wafer_name,
                "device_name": device.get("device_name"),
                "image_path": device.get("image_location")
            })
    return entries


if __name__ == "__main__":
    entries = load_image_entries("results.json")  # Make sure the file is in the same directory
    app = QApplication(sys.argv)
    window = MainWindow(entries)
    sys.exit(app.exec())
