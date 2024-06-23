import sys
import random

# import serial
#
# ser = serial.Serial('com17', 9600, timeout=1)
# try:
#     while True:
#         if ser.in_waiting > 0:
#             # 读取串口数据
#             data = ser.readline()
#             print(data.decode('utf-8').strip())  # 打印数据（假设为ASCII编码）
#             # print(data.type)
#             if ser.readline() =='A6':
#                 print('111111')
#             else:
#                 print("不匹配")
#
# except KeyboardInterrupt:
#     pass
import serial

ser = serial.Serial('com17', 9600, timeout=1)
try:
    while True:
        if ser.in_waiting > 0:
            # 读取串口数据
            data = ser.readline().decode('utf-8').strip()
            print(data)

            if data == 'A6':
                print('匹配')
            else:
                print("不匹配")

except KeyboardInterrupt:
    pass

ser.close()



# from PyQt5.QtChart import QLineSeries
# from PyQt5.QtChart import QDateTimeAxis, QValueAxis, QSplineSeries, QChart, QChartView
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import QPainter
# from PyQt5.QtCore import QDateTime, Qt, QTimer
#
#
# class ChartView(QChartView, QChart):
#     def __init__(self, *args, **kwargs):
#         super(ChartView, self).__init__(*args, **kwargs)
#         self.serial = None
#         self.resize(800, 600)
#         self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
#         self.chart_init()
#         # self.timer_init()
#         # self.setupPrarmeters()
#         self.drawLine()

    # def setupPrarmeters(self):
    #     # 设置数据显示时间 1min
    #     self.showTime = 60 * 1
    #     # 设置数据刷新时间 1s
    #     self.flushTime = 1000 * 1
    #     # 设置显示数据量
    #     self.totalNum = self.showTime / self.flushTime * 1000
#     def timer_init(self):
#         # 使用QTimer，2秒触发一次，更新数据
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.drawLine)
#         self.timer.start(self.flushTime)
#
#     def chart_init(self):
#         self.dtaxisX = QDateTimeAxis()#初始化X轴
#         self.vlaxisY = QValueAxis()#初始化Y轴
#         self.chart = QChart()
#         self.series = QSplineSeries()
#         # 设置曲线名称
#         self.series.setName("实时数据")
#         # 把曲线添加到QChart的实例中
#         self.chart.addSeries(self.series)
#         # 声明并初始化X轴，Y轴
#         chartView = QChartView(self.chart)
#         chartView.setRenderHint(QPainter.Antialiasing)
#         # 设置坐标轴显示范围
#         self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-300* 1))
#         self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
#         self.vlaxisY.setMin(-300)
#         self.vlaxisY.setMax(300)
#         # 设置X轴时间样式
#         self.dtaxisX.setFormat("hh:mm:ss")
#         # 设置坐标轴上的格点
#         self.dtaxisX.setTickCount(6)
#         self.vlaxisY.setTickCount(11)
#         # 设置坐标轴名称
#         self.dtaxisX.setTitleText("时间")
#         self.vlaxisY.setTitleText("温度")
#         # 设置网格不显示
#         self.vlaxisY.setGridLineVisible(True)
#         # 把坐标轴添加到chart中
#         self.chart.addAxis(self.dtaxisX, Qt.AlignBottom)
#         self.chart.addAxis(self.vlaxisY, Qt.AlignLeft)
#         # 把曲线关联到坐标轴
#         self.series.attachAxis(self.dtaxisX)
#         self.series.attachAxis(self.vlaxisY)
#
#         # self.setChart(self.chart)
#         # 把曲线关联到坐标轴
#         self.series.attachAxis(self.dtaxisX)
#         self.series.attachAxis(self.vlaxisY)
#
#
#
#     def drawLine(self, length=None):
#         # 获取当前时间
#         bjtime = QDateTime.currentDateTime()
#         # 更新X轴坐标
#         self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(0))
#         self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
#         # 当曲线上的点超出X轴的范围时，移除最早的点
#         # if (self.series.count() > 149):
#         #     self.series.removePoints(0, self.series.count() - 149)
#         # 产生随即数
#         # yint = random.randint(0,50)
#         # yint = serial.Serial('com6', 9600, timeout=1)
#         # int.to_bytes(length, byteorder='big', signed=False)
#
#         # 添加数据到曲线末端
#         # self.series.append(bjtime.toMSecsSinceEpoch(), yint)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     view = ChartView()
#     view.show()
#     sys.exit(app.exec_())
