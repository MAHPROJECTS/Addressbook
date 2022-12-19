from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

#Create a database or connnect to one
conn = sqlite3.connect('ab.db')
#Create a cursor
c = conn.cursor()

#Create a table
c.execute("""CREATE TABLE if not exists adbb(
    first_name text,
    last_name text,
    phone_number integer,
    email_address  text,
    address text
    )""")

#Commit the changes
conn.commit()

#Close our connection
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fn_label = QtWidgets.QLabel(self.centralwidget)
        self.fn_label.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fn_label.setFont(font)
        self.fn_label.setObjectName("fn_label")
        self.ln_label = QtWidgets.QLabel(self.centralwidget)
        self.ln_label.setGeometry(QtCore.QRect(40, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ln_label.setFont(font)
        self.ln_label.setObjectName("ln_label")
        self.ea_label = QtWidgets.QLabel(self.centralwidget)
        self.ea_label.setGeometry(QtCore.QRect(40, 350, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ea_label.setFont(font)
        self.ea_label.setObjectName("ea_label")
        self.pn_label = QtWidgets.QLabel(self.centralwidget)
        self.pn_label.setGeometry(QtCore.QRect(40, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pn_label.setFont(font)
        self.pn_label.setObjectName("pn_label")
        self.i_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.i_listwidget.setGeometry(QtCore.QRect(270, 70, 391, 521))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.i_listwidget.setFont(font)
        self.i_listwidget.setObjectName("i_listwidget")
        self.fn_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.fn_lineedit.setGeometry(QtCore.QRect(40, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fn_lineedit.setFont(font)
        self.fn_lineedit.setObjectName("fn_lineedit")
        self.ln_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_lineedit.setGeometry(QtCore.QRect(40, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_lineedit.setFont(font)
        self.ln_lineedit.setObjectName("ln_lineedit")
        self.pn_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.pn_lineedit.setGeometry(QtCore.QRect(40, 280, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pn_lineedit.setFont(font)
        self.pn_lineedit.setObjectName("pn_lineedit")
        self.i_label = QtWidgets.QLabel(self.centralwidget)
        self.i_label.setGeometry(QtCore.QRect(270, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.i_label.setFont(font)
        self.i_label.setObjectName("i_label")
        self.add_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.add_pushbutton.setGeometry(QtCore.QRect(30, 640, 111, 71))
        self.add_pushbutton.setObjectName("add_pushbutton")
        self.delete_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.delete_pushbutton.setGeometry(QtCore.QRect(290, 640, 111, 71))
        self.delete_pushbutton.setObjectName("delete_pushbutton")
        self.close_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.update_it())
        self.close_pushbutton.setGeometry(QtCore.QRect(420, 640, 111, 71))
        self.close_pushbutton.setObjectName("close_pushbutton")
        self.update_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_it())
        self.update_pushbutton.setGeometry(QtCore.QRect(160, 640, 111, 71))
        self.update_pushbutton.setObjectName("update_pushbutton")
        self.save_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.close_it())
        self.save_pushbutton.setGeometry(QtCore.QRect(550, 640, 111, 71))
        self.save_pushbutton.setObjectName("save_pushbutton")
        self.ea_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.ea_lineedit.setGeometry(QtCore.QRect(40, 390, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ea_lineedit.setFont(font)
        self.ea_lineedit.setObjectName("ea_lineedit")
        self.a_label = QtWidgets.QLabel(self.centralwidget)
        self.a_label.setGeometry(QtCore.QRect(40, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.a_label.setFont(font)
        self.a_label.setObjectName("a_label")
        self.a_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.a_textedit.setGeometry(QtCore.QRect(40, 500, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.a_textedit.setFont(font)
        self.a_textedit.setObjectName("a_textedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Grab all the items from the database
        self.everything()
        self.grab_all()
        self.close_pushbutton.setEnabled(False)
        self.save_pushbutton.setEnabled(False)

    def cls(self):
        self.save_pushbutton.setEnabled(False)
        self.close_pushbutton.setEnabled(False)

    def clearclear(self):
        self.i_listwidget.clear()


    
    #Grab items from database
    def grab_all(self):
        
        conn = sqlite3.connect('ab.db')

        #Create a cursor
        c = conn.cursor()
        
        #creating the sql statement which is select all from a_b table
        c.execute("SELECT * FROM adbb")

        records = c.fetchall()


        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()

        #Loop though records and add to screen
        for record in records:
            self.i_listwidget.addItem(str(record[0]))
            

        print(records)


    def everything(self):

        conn = sqlite3.connect('ab.db')

        #Create a cursor
        c = conn.cursor()
        
        #creating the sql statement which is select all from a_b table
        c.execute("SELECT * FROM adbb")

        records = c.fetchall()


        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()

        if not records:
            self.delete_pushbutton.setEnabled(False)
        else:
            pass

        if not records:
            self.save_pushbutton.setEnabled(False)
        else:
            pass

        if not records:
            self.update_pushbutton.setEnabled(False)
        else:
            pass

        if not records:
            self.close_pushbutton.setEnabled(False)
        else:
            pass


    #AddItemToList
    def add_it(self):


                #Create a database or connnect to one
        conn = sqlite3.connect('ab.db')
        #Create a cursor
        c = conn.cursor()

        item1 = self.fn_lineedit.text()
        item2 = self.ln_lineedit.text()
        item3 = self.pn_lineedit.text()
        item4 = self.ea_lineedit.text()
        item5 = self.a_textedit.toPlainText()

        if self.fn_lineedit.text() == '':
            msg = QMessageBox()
            msg.setWindowTitle("Your silly")
            msg.setText("The first name is mandatory pls note this in your head so we do not have to go through this inconvenience again *>_<*")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        else:
            self.i_listwidget.addItem(item1)
            self.fn_lineedit.setText("")
            self.ln_lineedit.setText("")
            self.pn_lineedit.setText("")
            self.ea_lineedit.setText("")
            self.a_textedit.setText("")


            items = []
            for index in range(self.i_listwidget.count()):
                items.append(self.i_listwidget.item(index))


            c.execute('''INSERT INTO adbb(first_name, last_name, phone_number, email_address, address)
                                       VALUES (?, ?, ?, ?, ?)''', 
                                       ( item1,
                                         item2,
                                         item3,
                                         item4,
                                         item5)
                                   )  

            self.update_pushbutton.setEnabled(True)
            self.close_pushbutton.setEnabled(False)
            self.delete_pushbutton.setEnabled(True)
            self.save_pushbutton.setEnabled(False)
              
            

            conn.commit()

            conn.close()


                    #pop up box
            msg = QMessageBox()
            msg.setWindowTitle("Saved To Database")
            msg.setText("Your contact Has Been added!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        

        


    def open_it(self):

        #Create a database or connnect to one
        conn = sqlite3.connect('ab.db')
        #Create a cursor
        c = conn.cursor()

        global symbol
        symbol = self.i_listwidget.currentItem().text()

        c.execute("SELECT * FROM adbb WHERE first_name = '%s'" % symbol)


        result = c.fetchall()

        self.everything()




        for results in result:
            a = (results[0])
            b = (results[1])
            c = (results[2])
            d = (results[3])
            e = (results[4])

        self.fn_lineedit.setText(str(a))
        self.ln_lineedit.setText(str(b))
        self.pn_lineedit.setText(str(c))
        self.ea_lineedit.setText(str(d))
        self.a_textedit.setText(str(e))

        self.close_pushbutton.setEnabled(True)
        self.save_pushbutton.setEnabled(True)


        self.everything()


        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()

        

    def delete_it(self):
        something = self.i_listwidget.currentItem()
        symbol = self.i_listwidget.currentItem().text()

        if something== None:
            msg = QMessageBox()
            msg.setWindowTitle("NO")
            msg.setText("You have not selected anything to be deleted")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("rusureee")
            msgBox.setText("Are you sure you want to delete " + symbol)
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.addButton(QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)
            if(msgBox.exec() == QMessageBox.Yes):

                print("1")

                # create a data base or connect to one
                conn = sqlite3.connect('ab.db')
                # create a cursor
                c = conn.cursor()

                symbol = self.i_listwidget.currentItem().text()
                clicked = self.i_listwidget.currentRow()
                self.i_listwidget.takeItem(clicked)

                c.execute("DELETE FROM adbb WHERE first_name = '%s'" % symbol)

                # commit the changes
                conn.commit()

                # close our connection
                conn.close()

                # clear the item box
                self.fn_lineedit.setText("")
                self.ln_lineedit.setText("")
                self.pn_lineedit.setText("")
                self.ea_lineedit.setText("")
                self.a_textedit.setText("")


                self.close_pushbutton.setEnabled(False)
                self.save_pushbutton.setEnabled(False)

                self.everything()
            else:

                pass

    def close_it(self):
        #Create a database or connnect to one
        conn = sqlite3.connect('ab.db')
        #Create a cursor
        c = conn.cursor()

        self.fn_lineedit.setText("")
        self.ln_lineedit.setText("")
        self.pn_lineedit.setText("")
        self.ea_lineedit.setText("")
        self.a_textedit.setText("")

        self.close_pushbutton.setEnabled(False)
        self.cls()
        self.everything()
        conn.commit()

        conn.close()

    def update_it(self):

        conn = sqlite3.connect('ab.db')

        c = conn.cursor()

        aa= self.fn_lineedit.text()
        bb= self.ln_lineedit.text()
        cc= self.pn_lineedit.text()
        dd= self.ea_lineedit.text()
        ee= self.a_textedit.toPlainText()

        print(aa, bb, cc, dd, ee, symbol)
        
        c.execute("""
            UPDATE adbb
            SET first_name=?, last_name=?, phone_number=?, email_address=?, address=?
            WHERE first_name=?
            """, (aa, bb, cc, dd, ee, symbol))

        self.everything()
        self.clearclear()

        conn.commit()

        conn.close()
        self.grab_all()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fn_label.setText(_translate("MainWindow", "First Name"))
        self.ln_label.setText(_translate("MainWindow", "Last Name"))
        self.ea_label.setText(_translate("MainWindow", "Email Address"))
        self.pn_label.setText(_translate("MainWindow", "Phone Number"))
        self.i_label.setText(_translate("MainWindow", "Information"))
        self.add_pushbutton.setText(_translate("MainWindow", "Add"))
        self.delete_pushbutton.setText(_translate("MainWindow", "Delete"))
        self.close_pushbutton.setText(_translate("MainWindow", "Update"))
        self.update_pushbutton.setText(_translate("MainWindow", "Open"))
        self.save_pushbutton.setText(_translate("MainWindow", "Close"))
        self.a_label.setText(_translate("MainWindow", "Address"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
