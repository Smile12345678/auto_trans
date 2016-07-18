#--------------------------------------------123-
from PyQt5.QtCore import QThread,pyqtSignal
import util.utils as utils
import data.xml_writer as XW

#业务工作线程
class WorkThread(QThread):
    transXml_trigger = pyqtSignal(int) #SQLite刷库的发射器

    def __init__(self):
        super(WorkThread,self).__init__()
        self.m_state = -1

    def setXlsPath(self, path):
        self.m_state = 1
        self.m_xlsPath = path

    #state 工作类型: == 1 SQLite刷库
    def run(self):
        if self.m_state == 1:
            self.parseXls()
        else:
            return

    def parseXls(self):
        for item in utils.read_excel(self.m_xlsPath):
            if item[1] == "lang":
                self.excel_info = utils.read_sheet(item)
        self.writeXml()
        self.transXml_trigger.emit(1)

    def writeXml(self):
        temLangPath = "data/lang.xml"
        outputLangPath = "output/lang.xml"
        utils.copyFiles(temLangPath, outputLangPath)
        self.m_xmlWriter = XW.XmlData(outputLangPath)
        for i in range(len(self.excel_info.row_lists)):
            if i == 0:
                #第一行不解析
                continue
            row = self.excel_info.row_lists[i]
            if len(row) == 3:
                self.m_xmlWriter.insert_data(row[0], row[2])
        self.m_xmlWriter.sava_data()



