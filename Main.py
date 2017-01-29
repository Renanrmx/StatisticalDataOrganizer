# coding: utf-8
__author__ = 'Renan'

import time
import sys

from PyQt4.QtGui import *

import Window


class Main(QMainWindow, Window.Ui_MainWindow):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.arrangedData = []

        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)

        self.btnClean.clicked.connect(self.cleanValues)
        self.btnPath.clicked.connect(self.output)
        self.btnGen.clicked.connect(self.processing)

        self.txtValues.textChanged.connect(self.activeButtons)
        self.txtPath.textChanged.connect(self.activeButtons)
        self.txtExclude.textChanged.connect(self.activeButtons)
        self.chrSplit.textChanged.connect(self.activeButtons)
        self.chrDecimal.textChanged.connect(self.activeButtons)

        self.activeButtons()

    def activeButtons(self, process=True):
        if process is False:
            self.btnGen.setDisabled(True)
            self.btnPath.setDisabled(True)
            self.btnClean.setDisabled(True)
            self.txtValues.setDisabled(True)
            self.txtPath.setDisabled(True)
            self.txtExclude.setDisabled(True)
            self.chrSplit.setDisabled(True)
            self.chrDecimal.setDisabled(True)

        else:
            self.txtValues.setEnabled(True)
            self.txtPath.setEnabled(True)
            self.txtExclude.setEnabled(True)
            self.chrSplit.setEnabled(True)
            self.chrDecimal.setEnabled(True)
            self.btnPath.setEnabled(True)

            if self.txtValues.toPlainText() and self.txtPath.text() and self.chrSplit.text() and self.chrDecimal.text():
                self.btnGen.setEnabled(True)

            else:
                self.btnGen.setDisabled(True)

            if self.txtValues.toPlainText() or self.txtPath.text() or self.chrSplit.text() or self.chrDecimal.text():
                self.btnClean.setEnabled(True)

            else:
                self.btnClean.setDisabled(True)

    def cleanValues(self):
        self.txtValues.clear()
        self.txtPath.clear()
        self.txtExclude.clear()
        self.chrSplit.clear()
        self.chrDecimal.clear()

        self.txtValues.setFocus()
        self.activeButtons()

    def output(self):
        folder = QFileDialog.getExistingDirectory()
        if folder:
            folder = unicode(folder)
            self.txtPath.setText(folder)

    def processing(self):
        self.activeButtons(False)
        self.fileGen()
        self.activeButtons()

    def sort(self):

        unsortedList = unicode(self.txtValues.toPlainText())

        excludeList = unicode(self.txtExclude.text()).split(' ')
        for exclude in excludeList:
            unsortedList = unsortedList.replace(exclude, '')

        unsortedList = unsortedList.replace(unicode(self.chrDecimal.text()), '.')
        unsortedList = unsortedList.split(unicode(self.chrSplit.text()))

        sortedList = []
        for value in unsortedList:
            try:
                int(value)
            except ValueError:
                try:
                    float(value)
                except ValueError:
                    if value != '':
                        QMessageBox.critical(self, u'Erro', u'There are one or more non-numeric values \n' +
                                                            u'or inappropriate separator: \n' + value)
                        return False
                else:
                    sortedList.append(float(value))

            else:
                sortedList.append(int(value))

        del unsortedList

        self.arrangedData = []
        uniqueValues = list(set(sortedList))
        uniqueValues.sort()
        for value in uniqueValues:
            self.arrangedData.append((value, sortedList.count(value)))

        del sortedList

        return True

    def dist(self):
        result = ''''''
        for value in self.arrangedData:
            for count in xrange(value[1]):
                if count == 0:
                    result += str(value[1]) + ' | '
                result += str(value[0])

                if count+1 != value[1]:
                    result += ', '
            result += '\n'

        return result

    def rol(self):
        sortedString = []
        for value in self.arrangedData:
            for count in xrange(value[1]):
                sortedString.append(value[0])

        sortedString = str(sortedString)[1:-1]
        nose = 70

        result = ''''''
        while True:
            if len(sortedString) <= nose:
                result += sortedString + '\n'
                break

            else:
                for i in range(nose, -1, -1):
                    if sortedString[i] == ' ':
                        result += sortedString[:i] + '\n'
                        sortedString = sortedString[i+1:]
                        break

        return result

    def fileGen(self):
        if self.sort():
            try:
                textFile = open(self.txtPath.text() + '/' + 'OrganizedData_' + str(time.time()) + ".txt", "w")
            except IOError:
                QMessageBox.critical(self, u'Erro', u'Output directory is invalid or unavailable')
            else:
                textFile.write(self.dist())
                textFile.write('\n\n\n\n')
                textFile.write(self.rol())
                textFile.close()

    def about(self):
        QMessageBox.about(self, u'About', u'''

        Statistical Data Organizer 0.1.3 Alpha
        Built on Dec 10, 2016
        Powered by Renanrmx

        github.com/Renanrmx

        ''')

    def help(self):
        QMessageBox.about(self, u'Help', u'''

        This program serves to organize a set of numerical data
        for better statistical visualization.

        Its use is simple, it is only necessary to fill in the
        required fields correctly as informed in their descriptions,
        after this by clicking on the generate button a file
        containing the ordered values will be created in the
        indicated location.

        ''')


def main():
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
