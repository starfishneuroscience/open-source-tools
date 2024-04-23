import sys
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel,QHBoxLayout, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.widgets import RangeSlider, CheckButtons
from draggableLine import DraggableLine
from dataSelectSlider import DataSelectSlider

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.load_button = QPushButton('Load Data')
        self.load_button.clicked.connect(self.load_data)

        #Side Bar Data
        self.file_title_label = QLabel("No file loaded")
        self.file_title_label.setWordWrap(True)

        self.wafer_id_label = QLabel("Wafer ID:")
        self.input_text_box_wafer_id= QLineEdit()

        self.test_id_label = QLabel("Test ID:")
        self.input_text_box_test_id = QLineEdit()

        self.section_id_label = QLabel("Section ID:")
        self.input_text_box_section_id = QLineEdit()

        self.level_button = QPushButton('Level')
        self.level_button.clicked.connect(self.level_data)
        self.level_button.setEnabled(False)

        self.split_button = QPushButton('Split and Export')
        self.split_button.clicked.connect(self.split_data)
        self.split_button.setEnabled(False)

        # Create a vertical layout for the plot and the load button
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.load_button)
        plot_layout.addWidget(self.canvas)
        
        #Sliders Layout
        self.sliders_layout = QVBoxLayout()
        #New Slider Button
        self.create_slider_button = QPushButton('Create Highlight Slider')  # Create the button
        self.create_slider_button.clicked.connect(self.create_highlight_slider)  # Connect the button to the method
        self.sliders_layout.addWidget(self.create_slider_button)
        plot_layout.addLayout(self.sliders_layout)  
        
        #Action Buttons
        action_buttons_layout = QHBoxLayout()
        action_buttons_layout.addWidget(self.level_button)
        action_buttons_layout.addWidget(self.split_button)
        plot_layout.addLayout(action_buttons_layout)
        
        # Create Wafer ID Input:
        wafer_id_layout = QHBoxLayout()
        wafer_id_layout.addWidget(self.wafer_id_label)
        wafer_id_layout.addWidget(self.input_text_box_wafer_id)

        # Create Test ID Input:
        test_id_layout = QHBoxLayout()
        test_id_layout.addWidget(self.test_id_label)
        test_id_layout.addWidget(self.input_text_box_test_id)

        # Create Wafer ID Input:
        section_id_layout = QHBoxLayout()
        section_id_layout.addWidget(self.section_id_label)
        section_id_layout.addWidget(self.input_text_box_section_id)

        # Create a vertical layout for the label and input text boxes
        label_layout = QVBoxLayout()
        label_layout.addWidget(self.file_title_label)
        label_layout.addLayout(wafer_id_layout)
        label_layout.addLayout(test_id_layout)
        label_layout.addLayout(section_id_layout)


        # Create a horizontal layout for the label and the plot
        main_layout = QHBoxLayout()
        main_layout.addLayout(label_layout)  # Add the Label layout to the main layout
        main_layout.addLayout(plot_layout)  # Add the plot layout to the main layout
        main_layout.setStretch(0, 1)  # Set the label to take up 10% of the width
        main_layout.setStretch(1, 9)  # Set the plot to take up 90% of the width

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.df = None
        self.sliders = []
        self.sliders_index = 0
        self.draggable_lines = []
        self.draggable_lines_index = 0
        self.file_title = None
        self.wafer_id = None
        self.test_id = None
        self.section_id = None
        self.header = None

        self.showMaximized()
        
    def create_highlight_slider(self):
        print("Create New Slider")
        slider = DataSelectSlider(self,self.sliders_index,0,1)
        self.sliders_index = self.sliders_index + 1
        self.sliders_layout.insertWidget(self.sliders_layout.count()-1,slider)
        slider.closed.connect(self.handle_slider_closed)
        slider.slider_changed.connect(self.handle_slider_changed)

    def handle_slider_closed(self, slider_index):
        print("Slider closed:", slider_index)
        self.sliders = [s for s in self.sliders if s.index != slider_index]
    
    def handle_slider_changed(self,lower_bound,upper_bound):
        print("Slider Updated: ",lower_bound,upper_bound)


    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', 'C:\\Users\\Alex\\Desktop\\Implant\\Implant\\Electrodes\\Fabrication\\Metrology\\Raw Data\\DektakXT\\W-000008\\Test 01', 'CSV Files (*.csv)')
        if file_path:
            self.file_title = file_path.split('/')[-1]
            self.file_path = '/'.join(file_path.split('/')[0:-1])
            split_file_title = self.file_title.split('-')
            self.wafer_id = split_file_title[0]+'-'+split_file_title[1]
            self.test_id = split_file_title[2]+'-'+split_file_title[3]
            self.section_id = split_file_title[4]+'-'+split_file_title[5].split('.')[0]
            self.input_text_box_wafer_id.setText(self.wafer_id)
            self.input_text_box_test_id.setText(self.test_id)
            self.input_text_box_section_id.setText(self.section_id)
            
            # Find "Data" line
            self.header, row = self.get_cvs_header(file_path)
            #Pull in data skipping header
            self.df = pd.read_csv(file_path, skiprows=row)
            self.df.rename(columns={'Lateral(µm)': 'X', 'Height Data(µm)': 'Y'}, inplace=True)
            self.ax.clear()
            self.ax.plot(self.df['X'], self.df['Y'], '-o', label='Loaded Data')
            self.ax.set_title('Line Plot Example')
            self.ax.set_xlabel('X axis')
            self.ax.set_ylabel('Y axis')
            self.ax.legend()
            self.canvas.draw()

            # Set the text of the label to the file title
            self.file_title_label.setText(f"<b>File</b>:{file_path}")

    def get_cvs_header(self,file_path):
        header = []
        # Open the CSV file
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            # Create a CSV reader object
            csvreader = csv.reader(csvfile)
            row_num = 0
            # Iterate through each row in the CSV file
            for row in csvreader:
                row_num = row_num + 1
                header.append(row)
                # Check if the word "Data" is in the row
                if "Data" in row:
                    return header, row_num
                else:
                    pass
            return header,0

    def update_highlight(self, val):
        if self.df is not None:
            self.ax.clear()
            self.ax.plot(self.df['X'], self.df['Y'], '-o', label='Loaded Data')
            self.ax.fill_betweenx([self.ax.get_ylim()[0], self.ax.get_ylim()[1]], self.slider.val[0], self.slider.val[1], color='red', alpha=0.5, label='Selected Range')
            
            # Redraw all lines
            for draggable_line in self.draggable_lines:
                self.ax.axvline(x=draggable_line.line.get_xdata()[0], color='red', linestyle='--')
            
            self.ax.set_title('Line Plot Example')
            self.ax.set_xlabel('X axis')
            self.ax.set_ylabel('Y axis')
            self.ax.legend()
            self.canvas.draw()

            #Activate Level Button
            self.level_button.setEnabled(True)

    def on_click(self, event):
        if event.button == 3:  # Right-click
            if event.inaxes == self.ax and self.df is not None:
                line = self.ax.axvline(x=event.xdata, color='red', linestyle='--')
                draggable_line = DraggableLine(line, self, self.draggable_lines_index)
                self.draggable_lines_index = self.draggable_lines_index + 1
                self.draggable_lines.append(draggable_line)
                self.canvas.draw()
                #Activate Split Button
                self.split_button.setEnabled(True)

    def remove_line(self, index):
        line = [line for line in self.draggable_lines if line.index == index][0]
        self.draggable_lines.remove([line for line in self.draggable_lines if line.index == index][0])
        line.line.remove()
        self.canvas.draw()

    def remove_selection(self,index):
        print('Remove selection: ',index)

    def level_data(self,event):
        pass

    def split_data(self,event):
        minimum_x = 0
        
        for i,line in enumerate(self.draggable_lines):
            maximum_x = float(line.line.get_xdata()[0])
            export_file_name = self.input_text_box_wafer_id.text() + "-" + self.input_text_box_test_id.text() + "-" + self.input_text_box_section_id.text() + "_" + str(i) + ".csv"
            with open(self.file_path + '/' + export_file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(self.header)
                writer.writerow(["Lateral(µm)","Height Data(µm)","",""])
                for index, row in self.df.iterrows():
                    if row["X"] > minimum_x and row["X"] <= maximum_x:
                        writer.writerow([row["X"],row["Y"],"",""])
            minimum_x = maximum_x
        i = i + 1
        export_file_name = self.input_text_box_wafer_id.text() + "-" + self.input_text_box_test_id.text() + "-" + self.input_text_box_section_id.text() + "_" + str(i) + ".csv"
        with open(self.file_path + '/' + export_file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.header)
            writer.writerow(["Lateral(µm)","Height Data(µm)","",""])
            for index, row in self.df.iterrows():
                if row["X"] > minimum_x:
                    writer.writerow([row["X"],row["Y"],"",""])
        self.close()





def main():
    app = QApplication(sys.argv)
    main_window = PlotWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
