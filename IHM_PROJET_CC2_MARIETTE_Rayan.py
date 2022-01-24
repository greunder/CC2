import sys
from PyQt5.QtWidgets import QMainWindow, QLabel,QApplication, QSpinBox,QPushButton, QWidget, QTabWidget,QVBoxLayout,QLineEdit


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PROJET #2'

        self.width = 600
        self.height = 500
        self.setWindowTitle(self.title)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()

        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Optimisation")

        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.l0= QLabel("Exemple de polynome : x**5-5x**3-20x+5")

        self.l= QLabel(" 1 - Pas Fixe \n 2 - Pas Accéléré \n 3 - Bissection \n 4 -  Newton-Raphson")
        self.choix= QSpinBox(self)
        self.choix.setRange(1, 4)
        self.tab1.layout.addWidget(self.l0)
        self.x01 = QLineEdit("Entrez le polynome")
        self.pas = QLineEdit("Entrez le pas")
        self.pushButton2 = QPushButton("Valider Choix")
        self.pushButton1 = QPushButton("Calculer")

        self.tab1.layout.addWidget(self.x01)
        self.tab1.layout.addWidget(self.l)
        self.tab1.layout.addWidget(self.choix)
        self.tab1.layout.addWidget(self.pushButton2)
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.pas)

        self.pushButton2.clicked.connect(lambda :print(self.choix.value()))
        
        if self.choix.value()==1 : 
            self.pushButton2.clicked.connect(lambda :print("Pas Simple"))
        elif self.choix.value()==2 : 
            self.pushButton2.clicked.connect(lambda :print("Pas Accéléré"))
        elif self.choix.value()==3 : 
            self.pushButton2.clicked.connect(lambda :print("Pas Accéléré"))
        else:
            self.pushButton2.clicked.connect(lambda :print("Newton-Raphson"))


        self.tab1.setLayout(self.tab1.layout)
        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
   