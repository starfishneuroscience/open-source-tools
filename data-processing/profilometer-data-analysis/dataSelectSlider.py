from PyQt5.QtCore import Qt, pyqtSignal
from superqt import QDoubleRangeSlider
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QColorDialog, QSizePolicy

color_list = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

class DataSelectSlider(QWidget):
    closed = pyqtSignal(int) 
    slider_changed = pyqtSignal(int)
    def __init__(self,parent,index,min_value,max_value):
        super().__init__()
        self.color = color_list[index]
        self.index = index
        self.min_value = min_value
        self.max_value = max_value
        self.visible = True
        self.lower_bound = None
        self.upper_bound = None
        self.lower_bound_input = None
        self.upper_bound_input = None
        
        self.initUI()

    def initUI(self):
        self.lower_bound = 0.2*(self.max_value-self.min_value)
        self.upper_bound = 0.8*(self.max_value-self.min_value)

        self.layout = QHBoxLayout()
        
        vis_button = QPushButton("eye")
        vis_button.clicked.connect(self.onVisButtonClicked)

        self.lower_bound_input = QLineEdit()
        self.lower_bound_input.setText(str(self.lower_bound))

        slider = QDoubleRangeSlider(Qt.Orientation.Horizontal)
        slider.setRange(self.min_value,self.max_value)
        slider.setValue((self.lower_bound, self.upper_bound))
        slider.setStyleSheet(f'''
        QSlider::handle {{
            background: {self.color}
        }}
        QRangeSlider {{
            qproperty-barColor: {self.color};
        }}
        ''')

        self.upper_bound_input = QLineEdit()
        self.upper_bound_input.setText(str(self.upper_bound))
        
        self.color_button = QPushButton()
        self.color_button.clicked.connect(self.onColorButtonClicked)
        self.color_button.setStyleSheet("background-color : "+self.color) 

        self.close_button = QPushButton("X")
        self.close_button.clicked.connect(self.onCloseButtonClicked)
        slider.valueChanged.connect(self.sliderChanged)

        fm = self.lower_bound_input.fontMetrics()
        width = fm.boundingRect('00000').width()
        self.lower_bound_input.setFixedWidth(width)
        self.upper_bound_input.setFixedWidth(width)

        self.layout.addWidget(vis_button)
        self.layout.addWidget(self.lower_bound_input)
        self.layout.addWidget(slider)
        self.layout.addWidget(self.upper_bound_input)
        self.layout.addWidget(self.color_button)
        self.layout.addWidget(self.close_button)
    
        self.setLayout(self.layout)

    def onVisButtonClicked(self):
        self.visible = not self.visible 
        print("Toggle Vis: ",self.index, self.visible)

    def onColorButtonClicked(self):
        color = QColorDialog.getColor()

    def onCloseButtonClicked(self):
        print("Close: ",self.index)
        self.closed.emit(self.index)
        self.deleteLater()

    def sliderChanged(self,t):
        self.lower_bound = t[0]
        self.upper_bound = t[1]
        self.lower_bound_input.setText(str(round(self.lower_bound,2)))
        self.upper_bound_input.setText(str(round(self.upper_bound,2)))
        self.slider_changed.emit(self.index)
        
        