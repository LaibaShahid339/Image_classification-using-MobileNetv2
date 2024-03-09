import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QWidget, QLabel
import pp as p
from PyQt5.QtGui import QPixmap



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,800)
        self.setWindowTitle("Object Detection")
        self.setStyleSheet("background-color: #264653")
        layout = QVBoxLayout(self)

        self.picture = QLabel(self)
        self.picture.setGeometry(100, 100, 300,300)
        self.picture.setStyleSheet("background-color: white; border-radius: 10px")
        

        self.button_select = QPushButton("Select a Picture", self)
        self.button_select.setStyleSheet("background-color: #2a9d8f; border-radius: 5px; color:white; height: 30px; width: 50px; font-weight: bold;")
        self.button_select.clicked.connect(self.select_picture)
        self.button_select.setGeometry(180, 430,150,50)

        text = QLabel(self)
        text.setGeometry(130, 500, 250, 50)
        text.setStyleSheet("font-weight:bold; color: white; background-color: #2a9d8f; border-radius: 5px;")
        text.setText("The first three predictions are:")

        self.predictions = QLabel(self)
        self.predictions.setGeometry(130, 570, 250, 100)
        self.predictions.setStyleSheet("border-radius: 5px; color: white; background-color: #2a9d8f; font-size: 20px; font-weight: bold; text-transform: uppercase; ")
        

    def select_picture(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a Picture", "", "Image Files (*.png *.jpg *.jpeg *.gif)")
        print("Selected File:", file_path)

        if file_path:
            pix = QPixmap(file_path)
            resized = pix.scaled(self.picture.size(), aspectRatioMode=2)
            self.picture.setPixmap(resized)
            predictionsModel = p.make_predictions(file_path)

            prediction_text = "\n".join(predictionsModel)
            self.predictions.setText(prediction_text)



        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
