from main_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
import data.xml_reader as xmlReader
import data.excel_writer as excelWriter
import net.trans_tool as transTool
import work_thread as W

#主窗口
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        #绑定UI
        self.bindUi()
        self.initWorkThread()

    def bindUi(self):
        self.zhBtn.clicked.connect(lambda: self.openFiles(1))
        self.enBtn.clicked.connect(lambda: self.openFiles(2))
        self.jpBtn.clicked.connect(lambda: self.openFiles(3))
        self.xmlBtn.clicked.connect(self.taransXml)

    def initWorkThread(self):
        #读取的线程
        self.m_workThread = W.WorkThread()
        self.m_workThread.transXml_trigger.connect(self.transXmlResult)

    #选择lang.xml文件
    def openFiles(self,index):
        self.m_index = index
        self.m_openDir = QFileDialog.getOpenFileName(self,"选取文件","","Excel Files (*.xml)")
        if self.m_openDir[0] != '':
            self.readLangFile()

    #读取lang.xml文件
    def readLangFile(self):
        self.m_xmlData = xmlReader.XmlData(self.m_openDir[0])
        self.m_dataList = self.m_xmlData.saveToDataList()
        self.taransFiles()

    #翻译
    def taransFiles(self):
        index = self.m_index
        self.m_xmlData.transToDataList(index)
        self.m_excelWriter = excelWriter.ExcelWriter()
        self.m_excelWriter.setLangData(self.m_dataList)
        self.m_excelWriter.writeLangTable(self.m_index)
        print("翻译完成")

    #回刷xml
    def taransXml(self):
        self.m_openXlsDir = QFileDialog.getOpenFileName(self,"选取文件","","Excel Files (*.xls)")
        if self.m_openXlsDir[0] != '':
            self.readXlsFile(self.m_openXlsDir[0])

    #回刷xml
    def readXlsFile(self, path):
        self.m_workThread.setXlsPath(path)
        self.m_workThread.start()
        pass

    #回刷xml刷库结束
    def transXmlResult(self, ret):
        pass








if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainshow= MainWindow()
    mainshow.show()
    sys.exit(app.exec_())