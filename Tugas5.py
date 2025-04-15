import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QFont

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font and Color Adjuster")

        self.label = QLabel("F1D022076", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 24))

        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(20)
        self.font_slider.setMaximum(60)
        self.font_slider.setValue(24)
        self.font_slider.valueChanged.connect(self.update_font_size)

        self.bg_slider = QSlider(Qt.Horizontal)
        self.bg_slider.setMinimum(0)
        self.bg_slider.setMaximum(255)
        self.bg_slider.setValue(255)
        self.bg_slider.valueChanged.connect(self.update_bg_color)

        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setMinimum(0)
        self.font_color_slider.setMaximum(255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_font_color)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)

        def create_slider_row(label_text, slider):
            h_layout = QHBoxLayout()
            label = QLabel(label_text)
            label.setFixedWidth(120)
            h_layout.addWidget(label)
            h_layout.addWidget(slider)
            return h_layout

        main_layout.addLayout(create_slider_row("Font Size", self.font_slider))
        main_layout.addLayout(create_slider_row("Background Color", self.bg_slider))
        main_layout.addLayout(create_slider_row("Font Color", self.font_color_slider))

        self.setLayout(main_layout)
        self.resize(500, 200)

    def update_font_size(self, value):
        self.label.setFont(QFont("Arial", value))

    def update_bg_color(self, value):
        palette = self.label.palette()
        palette.setColor(QPalette.Window, QColor(value, value, value))
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

    def update_font_color(self, value):
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor(value, value, value))
        self.label.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.show()
    sys.exit(app.exec_())
