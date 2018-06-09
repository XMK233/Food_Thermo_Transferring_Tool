# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit, QFileDialog
from math import pi, ceil
import os
import csv

from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #初始化所有表格
        self.initializeTableDir()
        self.initializeTable1()
        self.initializeTable2()
        self.initializeTable3()
        self.initializeOtherList()
        self.initializeExportDir()

        #监听一些点击动作
        self.MingQueRecord.itemClicked.connect(self.removeMingQue)
        self.BMingQueRecord.itemClicked.connect(self.removeBMingQue)
        self.otherList.itemClicked.connect(self.displayOther)

    # ---------------初始化附录表---------------------
    #创建表格目录
    def initializeTableDir(self):
        tabDir = os.path.join(os.getcwd(), "Table")
        if not os.path.exists(tabDir):
            os.mkdir(tabDir)
        return

    # 第一张表
    def initializeTable1(self):
        tabName = os.path.join(os.getcwd(), "Table", "Table1.csv")
        if os.path.exists(tabName):  # 如果表存在
            f = open(tabName, "r", encoding="utf-8")  # 打开文件
            lines = csv.reader(f)  # 读取文件
            n = 0
            for line in lines:  # 读文件的每一行，然后一行一行设置进表
                self.Table1.insertRow(n)
                self.Table1.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table1.setItem(n, 1, QTableWidgetItem(line[1]))
                n += 1
        else:  # 表不存在，就什么也不做
            pass

    # 第二张表
    def initializeTable2(self):
        tabName = os.path.join(os.getcwd(), "Table", "Table2.csv")

        if os.path.exists(tabName):  # 如果表存在
            f = open(tabName, "r", encoding="utf-8")  # 打开文件
            lines = csv.reader(f)
            n = 0
            for line in lines:
                self.Table2.insertRow(n)
                self.Table2.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table2.setItem(n, 1, QTableWidgetItem(line[1]))
                self.Table2.setItem(n, 2, QTableWidgetItem(line[2]))
                self.Table2.setItem(n, 3, QTableWidgetItem(line[3]))
                self.Table2.setItem(n, 4, QTableWidgetItem(line[4]))
                self.Table2.setItem(n, 5, QTableWidgetItem(line[5]))
                n += 1
        else:
            pass

    # 第三张表
    def initializeTable3(self):
        tabName = os.path.join(os.getcwd(), "Table", "Table2.csv")

        if os.path.exists(tabName):  # 如果表存在
            f = open(tabName, "r", encoding="utf-8")  # 打开文件
            lines = csv.reader(f)
            n = 0
            for line in lines:
                self.Table3.insertRow(n)
                self.Table3.setItem(n, 0, QTableWidgetItem(line[0]))
                self.Table3.setItem(n, 1, QTableWidgetItem(line[1]))
                self.Table3.setItem(n, 2, QTableWidgetItem(line[2]))
                self.Table3.setItem(n, 3, QTableWidgetItem(line[3]))
                self.Table3.setItem(n, 4, QTableWidgetItem(line[4]))
                self.Table3.setItem(n, 5, QTableWidgetItem(line[5]))
        else:
            pass

    #其他附录
    def initializeOtherList(self):
        recDir = os.path.join(os.getcwd(), "otherRecord")
        if not os.path.exists(recDir):
            os.mkdir(recDir)
        for file in os.listdir(recDir):
            self.otherList.addItem(file[4:-4])
        return

    #导出记录单独放在一个目录里面。
    def initializeExportDir(self):
        recDir = os.path.join(os.getcwd(), "Export")
        if not os.path.exists(recDir):
            os.mkdir(recDir)
        return

    # -------------------计算--------------------------
    # 增加一项明确纪录
    @pyqtSlot()
    def on_MingQueAdd_clicked(self):
        tnt = float(self.MingQueTNT.text())
        qty = float(self.MingQueQuantity.text())

        self.MingQueRecord.addItem("%.2f,%d" % (tnt, qty))

        self.MingQueTNT.clear()
        self.MingQueQuantity.clear()

        return

    # 增加一项不明确记录
    @pyqtSlot()
    def on_BMingQueAdd_clicked(self):

        d = float(self.BMingQueDiameter.text())
        l = float(self.BMingQueLength.text())
        lr = float(self.BMingQueHeadLength.text())
        n = float(self.BMingQueQuantity.text())

        self.BMingQueRecord.addItem("%.2f,%.2f,%.2f,%d" % (d, l, lr, n))

        self.BMingQueDiameter.clear()
        self.BMingQueLength.clear()
        self.BMingQueHeadLength.clear()
        self.BMingQueQuantity.clear()

        return

    # 计算按钮对应的计算，只是结果计算而已。
    def calculate(self):
        totalMass = 0.0
        for i in range(self.MingQueRecord.count()):
            line = [float(i) for i in self.MingQueRecord.item(i).text().split(",")]
            totalMass += line[0] * line[1]

        for i in range(self.BMingQueRecord.count()):
            k = [float(i) for i in self.BMingQueRecord.item(i).text().split(",")]
            totalMass += (pi * (k[0] ** 4) * (k[1] + k[2]) * 1.75 * 1.8 / 94 / 51) * k[3]

        # 总量
        resultTotal = round(totalMass)

        # zk个数
        holeQuantity = ceil(float(resultTotal) / 25)

        # dk当量
        Q = ceil(float(resultTotal) / holeQuantity)

        # 每zk建议xh用量
        resultAdvice = 0.0
        if Q <= 2:
            resultAdvice = 0.2
        elif Q > 2 and Q <= 4:
            resultAdvice = 0.4
        elif Q > 4 and Q <= 10:
            resultAdvice = 1.0
        elif Q > 10 and Q <= 20:
            resultAdvice = 2.0
        elif Q > 20 and Q <= 30:
            resultAdvice = 3.0
        else:
            resultAdvice = 4.0

        # yt安全距离
        resultBarrier = round(20 + 6.5 * Q)

        # jjaq距离
        resultAlert = 0
        if Q <= 1:
            resultAlert = 200
        elif Q > 1 and Q <= 5:
            resultAlert = 500
        elif Q > 5 and Q <= 15:
            resultAlert = 1000
        elif Q > 15 and Q <= 25:
            resultAlert = 1500
        else:
            resultAlert = 2000

        return resultTotal, holeQuantity, Q, resultAdvice, resultBarrier, resultAlert

    # 显示出来
    @pyqtSlot()
    def on_Calculate_clicked(self):
        resultTotal, holeQuantity, Q, resultAdvice, resultBarrier, resultAlert = self.calculate()

        self.ResultTotal.setText(str(resultTotal))
        self.ResultHoleNumber.setText(str(holeQuantity))
        self.ResultHoleDangliang.setText(str(Q))
        self.ResultTNT.setText(str(resultAdvice))
        self.ResultBarrier.setText(str(resultBarrier))
        self.ResultAlert.setText(str(resultAlert))

        return

    # 导出记录
    @pyqtSlot()
    def on_Export_clicked(self):
        rec = os.path.join(os.getcwd(), "Export", "历史纪录.txt")
        f = open(rec, "a")
        import datetime
        f.write("时间： %s\n" % (datetime.datetime.now().strftime('%Y/%m/%d, %H:%M')))
        f.write("dy情况: \n")

        for i in range(self.MingQueRecord.count()):
            line = [float(i) for i in self.MingQueRecord.item(i).text().split(",")]
            f.write("\t  卡路里(k): %.1f   数量: %d\n" % (line[0], line[1]))

        for i in range(self.BMingQueRecord.count()):
            k = [float(i) for i in self.BMingQueRecord.item(i).text().split(",")]
            tmp = (pi * (k[0] ** 2) * (k[1] - k[2]) * 1.35 * 1 / 4 / 1000) * k[3]
            f.write("\t  直径: %.1f\n\t  长: %.1f\n\t  头长: %.1f\n\t  热量: %.1f\n\t  数量:%d\n" % (
                k[0], k[1], k[2], tmp, k[3]))

        resultTotal, holeQuantity, Q, resultAdvice, resultBarrier, resultAlert = self.calculate()
        f.write("总量（kg TNT）: %d\n" % (resultTotal))
        f.write("111（kg TNT）: %d\n" % (resultAdvice))
        f.write("距离1（m）: %d\n" % (resultBarrier))
        f.write("距离2（m）: %d\n" % (resultAlert))
        f.write("个数（个）: %d\n" % (holeQuantity))
        f.write("单个卡路里量（kg）: %d\n\n" % (Q))

        f.close()
        QMessageBox.information(self, "导出信息",
                                "已完成",
                                QMessageBox.Yes | QMessageBox.No)
        return

    # 清除功能
    @pyqtSlot()
    def on_MingQueClear_clicked(self):
        self.MingQueRecord.clear()
        return

    # 清除功能
    @pyqtSlot()
    def on_BMingQueClear_clicked(self):
        self.BMingQueRecord.clear()
        return

    def removeMingQue(self):
        self.MingQueRecord.takeItem(self.MingQueRecord.currentRow())  ##删除一行
        return

    def removeBMingQue(self):
        self.BMingQueRecord.takeItem(self.BMingQueRecord.currentRow())  ##删除一行
        return

    # -------------附录-------------------------
    # 附录1
    # 给表增加行。可以选择在哪里加行。
    @pyqtSlot()
    def on_ThermoAdd_clicked(self):
        numOfRaw = self.Table1.rowCount()
        newPlace, ok = QInputDialog.getText(self, "加入条目", "在该行加入(1-%d):" % (numOfRaw + 1), QLineEdit.Normal,
                                            str(numOfRaw + 1))
        if ok:
            newRaw = int(newPlace) - 1
            self.Table1.insertRow(newRaw)
            self.Table1.setItem(newRaw, 0, QTableWidgetItem("--请修改--"))
            self.Table1.setItem(newRaw, 1, QTableWidgetItem("--请修改--"))

        return

    # 删除某一行
    @pyqtSlot()
    def on_ThermoRemove_clicked(self):
        self.Table1.removeRow(self.Table1.currentRow())
        return

    # 保存表格记录
    @pyqtSlot()
    def on_ThermoSave_clicked(self):
        table = os.path.join(os.getcwd(), "Table", "Table1.csv")

        f = open(table, "w", encoding="utf-8")
        for i in range(self.Table1.rowCount()):
            tmp = []
            for j in range(2):
                tmp.append(self.Table1.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()

        QMessageBox.information(self, "保存信息",
                                "文字信息已保存完成",
                                QMessageBox.Yes | QMessageBox.No)
        return

    # 附录2
    @pyqtSlot()
    def on_AnimalAdd_clicked(self):
        numOfRaw = self.Table2.rowCount()
        newPlace, ok = QInputDialog.getText(self, "加入条目", "在该行加入(1-%d):" % (numOfRaw + 1), QLineEdit.Normal,
                                            str(numOfRaw + 1))
        if ok:
            newRaw = int(newPlace) - 1
            self.Table2.insertRow(newRaw)

            self.Table2.setItem(newRaw, 0, QTableWidgetItem("--请修改--"))
            self.Table2.setItem(newRaw, 1, QTableWidgetItem("--请修改--"))
            self.Table2.setItem(newRaw, 2, QTableWidgetItem("--请修改--"))
            self.Table2.setItem(newRaw, 3, QTableWidgetItem("--请修改--"))
            self.Table2.setItem(newRaw, 4, QTableWidgetItem("--请修改--"))
            self.Table2.setItem(newRaw, 5, QTableWidgetItem("--请修改--"))
        return

    @pyqtSlot()
    def on_AnimalRemove_clicked(self):
        self.Table2.removeRow(self.Table2.currentRow())
        return

    @pyqtSlot()
    def on_AnimalSave_clicked(self):
        table = os.path.join(os.getcwd(), "Table", "Table2.csv")
        f = open(table, "w", encoding="utf-8")

        for i in range(self.Table2.rowCount()):
            tmp = []
            for j in range(6):
                tmp.append(self.Table2.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()

        QMessageBox.information(self, "保存信息",
                                "文字信息已保存完成",
                                QMessageBox.Yes | QMessageBox.No)
        return

    # 附录3
    @pyqtSlot()
    def on_SvvAdd_clicked(self):
        numOfRaw = self.Table3.rowCount()
        newPlace, ok = QInputDialog.getText(self, "加入条目", "在该行加入(1-%d):" % (numOfRaw + 1), QLineEdit.Normal,
                                            str(numOfRaw + 1))
        if ok:
            newRaw = int(newPlace) - 1
            self.Table3.insertRow(newRaw)
            self.Table3.setItem(newRaw, 0, QTableWidgetItem("--请修改--"))
            self.Table3.setItem(newRaw, 1, QTableWidgetItem("--请修改--"))
            self.Table3.setItem(newRaw, 2, QTableWidgetItem("--请修改--"))
            self.Table3.setItem(newRaw, 3, QTableWidgetItem("--请修改--"))
            self.Table3.setItem(newRaw, 4, QTableWidgetItem("--请修改--"))
            self.Table3.setItem(newRaw, 5, QTableWidgetItem("--请修改--"))
        return

    @pyqtSlot()
    def on_SvvRemove_clicked(self):
        self.Table3.removeRow(self.Table3.currentRow())
        return

    @pyqtSlot()
    def on_SvvSave_clicked(self):
        table = os.path.join(os.getcwd(), "Table", "Table3.csv")
        f = open(table, "w", encoding="utf-8")

        for i in range(self.Table3.rowCount()):
            tmp = []
            for j in range(6):
                tmp.append(self.Table3.item(i, j).text())
            f.write(",".join(tmp) + "\n")

        f.close()

        QMessageBox.information(self, "保存信息",
                                "文字信息已保存完成",
                                QMessageBox.Yes | QMessageBox.No)
        return

    #附录4
    #新增一条记录
    @pyqtSlot()
    def on_otherAddRec_clicked(self):
        newRec, ok = QInputDialog.getText(self, "新增记录", "记录名称:", QLineEdit.Normal,
                                            "新记录")
        if not ok:
            return
        #创造同名文件
        f = open("otherRecord\\rec_%s.txt" %(newRec), "w")
        f.write("picture: \n\ncontent: \n")
        f.close()
        #记录表增加一条
        self.otherList.addItem(newRec)
        #清空图文
        self.textEdit.clear()
        self.otherPic.setText("(图片)")

        return

    #选中一行记录
    def displayOther(self):
        recName = self.otherList.item(self.otherList.currentRow()).text()
        f = open("otherRecord\\rec_%s.txt" % (recName), encoding="utf-8")
        lines = f.readlines()

        n = 0
        for n in range(len(lines)):
            if lines[n] == "picture: \n":
                if lines[n + 1] == "\n":
                    self.otherPic.setText("(图片)")
                    continue
                tt = lines[n + 1].split("*")
                picName = tt[1]
                if picName != "":
                    self.otherPic.setText("")
                    self.otherPic.setPixmap(QtGui.QPixmap(picName))
                    self.otherPic.setScaledContents(True)
            elif lines[n] == "content: \n":
                self.textEdit.setText("".join(lines[n + 1:]))
            n += 1
        f.close()

        #点击了之后，按钮才可用
        self.otherAddPic.setEnabled(True)
        self.OtherSave.setEnabled(True)
        self.OtherDelete.setEnabled(True)

        return

    @pyqtSlot()
    def on_otherAddPic_clicked(self):
        #图片的名字
        picName = QFileDialog.getOpenFileName(self, "打开文件", os.getcwd())[0]

        #读相应文档里面的信息
        recName = self.otherList.item(self.otherList.currentRow()).text()
        f = open("otherRecord\\rec_%s.txt" %(recName), encoding="utf-8")
        lines = f.readlines()
        #把图片放到记录信息里面去
        n = 0
        for n in range(len(lines)):
            if lines[n] == "picture: \n":
                lines.insert(n + 1, "pic*%s*\n"%(picName))
            n += 1
        f.close()

        #把记录信息重新写到文件里
        f = open("otherRecord\\rec_%s.txt" %(recName), "w",encoding="utf-8")
        f.writelines(lines)
        f.close()

        #设置图片
        self.otherPic.setText("")
        self.otherPic.setPixmap(QtGui.QPixmap(picName))
        self.otherPic.setScaledContents(True)

        return

    @pyqtSlot()
    def on_OtherSave_clicked(self):
        recName = self.otherList.item(self.otherList.currentRow()).text()
        f = open("otherRecord\\rec_%s.txt" %(recName), encoding="utf-8")
        lines = f.readlines()
        # 把图片放到记录信息里面去
        n = 0
        for n in range(len(lines)):
            if lines[n] == "content: \n":
                text = self.textEdit.toPlainText()
                lines.insert(n + 1, "%s\n" % (text))
            n += 1
        f.close()

        # 把记录信息重新写到文件里
        f = open("otherRecord\\rec_%s.txt" % (recName), "w", encoding="utf-8")
        f.writelines(lines)
        f.close()
        #提示窗口
        QMessageBox.information(self, "保存信息",
                                "文字信息已保存完成",
                                QMessageBox.Yes | QMessageBox.No)
        return

    #删除记录
    @pyqtSlot()
    def on_OtherDelete_clicked(self):
        #recName = self.otherList.item(self.otherList.currentRow()).text()
        ret = QMessageBox.question(self, "删除记录",
                                "确定要删除？",
                                QMessageBox.Yes | QMessageBox.No)
        if ret == 16384:
            recName = self.otherList.item(self.otherList.currentRow()).text()
            self.otherList.takeItem(self.otherList.currentRow())  ##删除一行
            os.remove(os.path.join(os.getcwd(), "otherRecord", "rec_%s.txt" %(recName)))

        QMessageBox.information(self, "删除记录",
                                   "已删除",
                                   QMessageBox.Yes | QMessageBox.No)
        return
        #

# ---------------------------主函数---------------------------------------
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
