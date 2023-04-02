#导入模块

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import *
from PySide6.QtDesigner import *
from translate_model import translate
from read_connfig import data_config  



#设置窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        #加载ui文件
        qfile = QFile("project\\ui\\littleapp_translate.ui")   
        qfile.open(QFile.ReadOnly)
        qfile.close()
        
        #创建ui窗口对象
        self.ui = QUiLoader().load(qfile)
        #创建标题
        self.ui.setWindowTitle("百度翻译api调用小程序")
        self.ui.setWindowIcon(QIcon("pic/105771494_p0_master1200.png"))
        
        
        
        
        #逻辑连结
        self.ui.comboBox.addItems(["中文","英文","日语"])
        self.ui.comboBox_2.addItems(["中文","英文","日语"])
        
        self.ui.pushButton.clicked.connect(self.clicked_translate)
        self.ui.pushButton_2.clicked.connect(self.clear_text)
        
    
        
    def clicked_translate(self):
        from_lang=self.ui.comboBox.currentText()
        
        to_lang=self.ui.comboBox_2.currentText()
        q=self.ui.plainTextEdit.toPlainText()
        if from_lang=="中文":
            from_lang = "zh"
        elif from_lang=="英文":
            from_lang = "en"
        elif from_lang=="日语":
            from_lang = "jp"

        if to_lang=="中文":
            to_lang = "zh"
        elif to_lang=="英文":
            to_lang = "en"
        elif to_lang=="日语":
            to_lang = "jp"

                    
        result_translate = translate(q=q,from_lang=from_lang,to_lang=to_lang)
        self.result = self.ui.textEdit.append(result_translate)
        
    def clear_text(self):
        self.ui.textEdit.clear()    
    
    

class use_path:
    def __init__(self):
        data_config.get_data_config()
        self.imagePath=data_config.config_dict["imagePath"]     
imagePath_bulid=use_path()
imagePath=imagePath_bulid.imagePath

if __name__=="__main__":
    
    app = QApplication([])
    
    with open("style.qss","r") as f:
        style = f.read()
    style = style.replace("@impage_path","url("+imagePath+")")   
    app.setStyleSheet(style)    
    window = MainWindow()
    window.ui.show()
    app.exec()