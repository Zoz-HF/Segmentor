# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1207, 789)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 0px;\n"
"  color: #E0E1E3;\n"
"  selection-background-color: #346792;\n"
"  selection-color: #E0E1E3;\n"
"    font-family : Ubuntu;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"  selection-background-color: #26486B;\n"
"  selection-color: #9DA9B5;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #176B87;\n"
"}\n"
"\n"
"QWidget::item:hover:!selected {\n"
"  background-color: rgba(23, 107, 135,50%);\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #60798B;\n"
"  border: 0px solid #1A72BB;\n"
"}\n"
"\n"
"/*-------------------------------------------------------------------------------------------*/\n"
"\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #E0E1E3;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #9DA9B5;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"/*-------------------------------------------------------------------------------------------*/\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid white;\n"
"  border-radius: 4px;\n"
"  background-color: rgb(25, 35, 45);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #176B87;\n"
"  border: 1px solid #C9CDD0;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: rgba(23, 107, 135,80%);\n"
"  border:#4169E1;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid red;\n"
"}\n"
"QScrollBar:vertical {\n"
"  background-color: rgb(25, 35, 45);\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid white;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #176B87;\n"
"  border: 1px solid #C9CDD0;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: rgba(23, 107, 135,80%);\n"
"  border: #9FCBFF;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #73C7FF;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\"qss_icons/light/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\"qss_icons/light/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\"qss_icons/light/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\"qss_icons/light/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\"qss_icons/light/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\"qss_icons/light/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\"qss_icons/light/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\"qss_icons/light/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/*----------------------------------------------------------------------------------------*/\n"
"QPushButton{\n"
" /*border:2px solid #05B8CC;*/\n"
" background-color: #176B87;\n"
" color:rgb(255, 255, 255);\n"
" border-radius: 10px;\n"
" font-weight:bold;\n"
" font-size:16px;\n"
"  transition: 500ms;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
" border: 1px solid #176B87;\n"
" background-color: rgba(23, 107, 135,80%)\n"
"}\n"
"QPushButton:pressed {\n"
" margin:1px 2px;\n"
" font-size: 15px;\n"
"}\n"
"/*----------------------------------------------------------------------------------------*/\n"
"QTabBar::tab {\n"
"    background-color: #455364;\n"
"    border: 3px solid #19232D;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    color: #E0E1E3;\n"
"    font-family: Ubuntu;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: #455364;\n"
"    border: 3px solid #19232D;\n"
"    border-radius: 10px;\n"
"    padding: 4px 8px;\n"
"    color: #E0E1E3;\n"
"    font-family: Ubuntu;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color:rgba(69,83,100,60%);\n"
"    color: white;\n"
"    margin-top: 3px;\n"
"    border-bottom: 3px solid white;\n"
"}\n"
"QPlotWidget{\n"
" background-color:(25, 35, 45, 0.8)\n"
"}\n"
"/*----------------------------------------------------------------------------------------*/\n"
"QComboBox{\n"
" border:1px solid #176B87;\n"
"border-radius:5px;\n"
"background-color: #176B87;\n"
"padding: 2px 10px;\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 22px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/caret-down copy.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"border:none;\n"
"    selection-background-color:#176B87;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_seg = QtWidgets.QWidget()
        self.tab_seg.setObjectName("tab_seg")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_seg)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(25)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_seg)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_seg = QtWidgets.QComboBox(self.tab_seg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_seg.sizePolicy().hasHeightForWidth())
        self.comboBox_seg.setSizePolicy(sizePolicy)
        self.comboBox_seg.setMaximumSize(QtCore.QSize(199, 16777215))
        self.comboBox_seg.setStyleSheet("")
        self.comboBox_seg.setIconSize(QtCore.QSize(30, 30))
        self.comboBox_seg.setObjectName("comboBox_seg")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_seg)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)
        self.stackedWidget_seg = QtWidgets.QStackedWidget(self.tab_seg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_seg.sizePolicy().hasHeightForWidth())
        self.stackedWidget_seg.setSizePolicy(sizePolicy)
        self.stackedWidget_seg.setObjectName("stackedWidget_seg")
        self.page_agglo = QtWidgets.QWidget()
        self.page_agglo.setObjectName("page_agglo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_agglo)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_agglo)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(22)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 14))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.spinBox_clusters_num = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_clusters_num.setFont(font)
        self.spinBox_clusters_num.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_clusters_num.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox_clusters_num.setProperty("value", 5)
        self.spinBox_clusters_num.setDisplayIntegerBase(10)
        self.spinBox_clusters_num.setObjectName("spinBox_clusters_num")
        self.horizontalLayout_6.addWidget(self.spinBox_clusters_num)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(22)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.spinBox_clusters_init = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_clusters_init.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox_clusters_init.setSuffix("")
        self.spinBox_clusters_init.setPrefix("")
        self.spinBox_clusters_init.setProperty("value", 15)
        self.spinBox_clusters_init.setDisplayIntegerBase(10)
        self.spinBox_clusters_init.setObjectName("spinBox_clusters_init")
        self.horizontalLayout_9.addWidget(self.spinBox_clusters_init)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.stackedWidget_seg.addWidget(self.page_agglo)
        self.page_mean_shift = QtWidgets.QWidget()
        self.page_mean_shift.setObjectName("page_mean_shift")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_mean_shift)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_mean_shift)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setContentsMargins(-1, 25, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.spinBox_cluster_size_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_cluster_size_2.setObjectName("spinBox_cluster_size_2")
        self.horizontalLayout_10.addWidget(self.spinBox_cluster_size_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.spinBox_cluster_init_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_cluster_init_2.setObjectName("spinBox_cluster_init_2")
        self.horizontalLayout_11.addWidget(self.spinBox_cluster_init_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.stackedWidget_seg.addWidget(self.page_mean_shift)
        self.page_kmeans = QtWidgets.QWidget()
        self.page_kmeans.setObjectName("page_kmeans")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_kmeans)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_kmeans)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_2.setContentsMargins(-1, 25, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setStyleSheet("font-size:15px;")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sld_seg_ksize = QtWidgets.QSlider(self.groupBox_4)
        self.sld_seg_ksize.setMinimum(3)
        self.sld_seg_ksize.setMaximum(12)
        self.sld_seg_ksize.setPageStep(2)
        self.sld_seg_ksize.setProperty("value", 3)
        self.sld_seg_ksize.setOrientation(QtCore.Qt.Horizontal)
        self.sld_seg_ksize.setObjectName("sld_seg_ksize")
        self.horizontalLayout_7.addWidget(self.sld_seg_ksize)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setMinimumSize(QtCore.QSize(50, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setStyleSheet("font-size:15px;")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sld_seg_max_iterations = QtWidgets.QSlider(self.groupBox_4)
        self.sld_seg_max_iterations.setMinimum(50)
        self.sld_seg_max_iterations.setMaximum(100)
        self.sld_seg_max_iterations.setProperty("value", 50)
        self.sld_seg_max_iterations.setOrientation(QtCore.Qt.Horizontal)
        self.sld_seg_max_iterations.setObjectName("sld_seg_max_iterations")
        self.horizontalLayout_8.addWidget(self.sld_seg_max_iterations)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setMinimumSize(QtCore.QSize(50, 0))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.stackedWidget_seg.addWidget(self.page_kmeans)
        self.page_region_grow = QtWidgets.QWidget()
        self.page_region_grow.setObjectName("page_region_grow")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_region_grow)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_region_grow)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(-1, 25, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setStyleSheet("font-size:15px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sld_region_threshold = QtWidgets.QSlider(self.groupBox_3)
        self.sld_region_threshold.setMinimum(1)
        self.sld_region_threshold.setMaximum(50)
        self.sld_region_threshold.setProperty("value", 6)
        self.sld_region_threshold.setOrientation(QtCore.Qt.Horizontal)
        self.sld_region_threshold.setObjectName("sld_region_threshold")
        self.horizontalLayout.addWidget(self.sld_region_threshold)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMinimumSize(QtCore.QSize(65, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.stackedWidget_seg.addWidget(self.page_region_grow)
        self.horizontalLayout_13.addWidget(self.stackedWidget_seg)
        self.btn_seg_apply = QtWidgets.QPushButton(self.tab_seg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_seg_apply.sizePolicy().hasHeightForWidth())
        self.btn_seg_apply.setSizePolicy(sizePolicy)
        self.btn_seg_apply.setMinimumSize(QtCore.QSize(100, 36))
        self.btn_seg_apply.setObjectName("btn_seg_apply")
        self.horizontalLayout_13.addWidget(self.btn_seg_apply)
        self.gridLayout_10.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.wgt_seg_input = PlotWidget(self.tab_seg)
        self.wgt_seg_input.setSizeIncrement(QtCore.QSize(1, 1))
        self.wgt_seg_input.setBaseSize(QtCore.QSize(200, 200))
        self.wgt_seg_input.setStyleSheet("background: crimson;")
        self.wgt_seg_input.setObjectName("wgt_seg_input")
        self.horizontalLayout_12.addWidget(self.wgt_seg_input)
        self.wgt_seg_output = PlotWidget(self.tab_seg)
        self.wgt_seg_output.setSizeIncrement(QtCore.QSize(1, 1))
        self.wgt_seg_output.setBaseSize(QtCore.QSize(200, 200))
        self.wgt_seg_output.setStyleSheet("background: deep blue;")
        self.wgt_seg_output.setObjectName("wgt_seg_output")
        self.horizontalLayout_12.addWidget(self.wgt_seg_output)
        self.gridLayout_10.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.gridLayout_10.setRowStretch(1, 1)
        self.tabWidget.addTab(self.tab_seg, "")
        self.tab_thresh = QtWidgets.QWidget()
        self.tab_thresh.setObjectName("tab_thresh")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_thresh)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.tab_thresh)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.comboBox_thresh = QtWidgets.QComboBox(self.tab_thresh)
        self.comboBox_thresh.setStyleSheet("background: #132f5c;")
        self.comboBox_thresh.setObjectName("comboBox_thresh")
        self.comboBox_thresh.addItem("")
        self.comboBox_thresh.addItem("")
        self.comboBox_thresh.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox_thresh)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.checkBox_thresh_global = QtWidgets.QCheckBox(self.tab_thresh)
        self.checkBox_thresh_global.setStyleSheet("font-size:15px;")
        self.checkBox_thresh_global.setChecked(True)
        self.checkBox_thresh_global.setObjectName("checkBox_thresh_global")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_thresh_global)
        self.horizontalLayout_15.addWidget(self.checkBox_thresh_global)
        self.checkBox_thresh_local = QtWidgets.QCheckBox(self.tab_thresh)
        self.checkBox_thresh_local.setStyleSheet("font-size:15px;")
        self.checkBox_thresh_local.setObjectName("checkBox_thresh_local")
        self.buttonGroup.addButton(self.checkBox_thresh_local)
        self.horizontalLayout_15.addWidget(self.checkBox_thresh_local)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_thresh)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_7.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_multi = QtWidgets.QWidget()
        self.page_multi.setObjectName("page_multi")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_multi)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_multi)
        self.label_3.setStyleSheet("font-size:15px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_thesh_multi_num_classes = QtWidgets.QSpinBox(self.page_multi)
        self.spinBox_thesh_multi_num_classes.setStyleSheet("font-size:15px;")
        self.spinBox_thesh_multi_num_classes.setMinimum(3)
        self.spinBox_thesh_multi_num_classes.setMaximum(20)
        self.spinBox_thesh_multi_num_classes.setProperty("value", 3)
        self.spinBox_thesh_multi_num_classes.setObjectName("spinBox_thesh_multi_num_classes")
        self.horizontalLayout_4.addWidget(self.spinBox_thesh_multi_num_classes)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.wgt_thresh_patch_size = QtWidgets.QWidget(self.page_multi)
        self.wgt_thresh_patch_size.setObjectName("wgt_thresh_patch_size")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.wgt_thresh_patch_size)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.wgt_thresh_patch_size)
        self.label_4.setStyleSheet("font-size:15px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spinBox_thesh_multi_patch_size = QtWidgets.QSpinBox(self.wgt_thresh_patch_size)
        self.spinBox_thesh_multi_patch_size.setStyleSheet("font-size:15px;")
        self.spinBox_thesh_multi_patch_size.setMinimum(0)
        self.spinBox_thesh_multi_patch_size.setMaximum(500)
        self.spinBox_thesh_multi_patch_size.setProperty("value", 25)
        self.spinBox_thesh_multi_patch_size.setObjectName("spinBox_thesh_multi_patch_size")
        self.horizontalLayout_5.addWidget(self.spinBox_thesh_multi_patch_size)
        self.verticalLayout.addWidget(self.wgt_thresh_patch_size)
        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_multi)
        self.horizontalLayout_17.addWidget(self.stackedWidget)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.btn_thresh_apply = QtWidgets.QPushButton(self.tab_thresh)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_thresh_apply.sizePolicy().hasHeightForWidth())
        self.btn_thresh_apply.setSizePolicy(sizePolicy)
        self.btn_thresh_apply.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_thresh_apply.setObjectName("btn_thresh_apply")
        self.horizontalLayout_17.addWidget(self.btn_thresh_apply)
        self.gridLayout_11.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.wgt_thresh_input = PlotWidget(self.tab_thresh)
        self.wgt_thresh_input.setSizeIncrement(QtCore.QSize(1, 1))
        self.wgt_thresh_input.setBaseSize(QtCore.QSize(200, 200))
        self.wgt_thresh_input.setStyleSheet("background: crimson;")
        self.wgt_thresh_input.setObjectName("wgt_thresh_input")
        self.horizontalLayout_14.addWidget(self.wgt_thresh_input)
        self.wgt_thresh_output = PlotWidget(self.tab_thresh)
        self.wgt_thresh_output.setSizeIncrement(QtCore.QSize(1, 1))
        self.wgt_thresh_output.setBaseSize(QtCore.QSize(200, 200))
        self.wgt_thresh_output.setStyleSheet("background: deep blue;")
        self.wgt_thresh_output.setObjectName("wgt_thresh_output")
        self.horizontalLayout_14.addWidget(self.wgt_thresh_output)
        self.gridLayout_11.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.gridLayout_11.setRowStretch(1, 1)
        self.tabWidget.addTab(self.tab_thresh, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.menuFile.addAction(self.actionOpen_Image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_seg.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.sld_seg_ksize.valueChanged['int'].connect(self.label_12.setNum) # type: ignore
        self.sld_seg_max_iterations.valueChanged['int'].connect(self.label_13.setNum) # type: ignore
        self.comboBox_seg.currentIndexChanged['int'].connect(self.stackedWidget_seg.setCurrentIndex) # type: ignore
        self.comboBox_thresh.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex) # type: ignore
        self.sld_region_threshold.valueChanged['int'].connect(self.label_5.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Segmentation Method"))
        self.comboBox_seg.setItemText(0, _translate("MainWindow", "Agglomerative"))
        self.comboBox_seg.setItemText(1, _translate("MainWindow", "Mean Shift"))
        self.comboBox_seg.setItemText(2, _translate("MainWindow", "K-Means"))
        self.comboBox_seg.setItemText(3, _translate("MainWindow", "Region Growing"))
        self.groupBox.setTitle(_translate("MainWindow", "                            Agglomerative Settings"))
        self.label_6.setText(_translate("MainWindow", "Clusters number = "))
        self.label_9.setText(_translate("MainWindow", "Initial Clusters ="))
        self.groupBox_2.setTitle(_translate("MainWindow", "Mean Shift Settings"))
        self.label_10.setText(_translate("MainWindow", "Cluster Size:"))
        self.label_11.setText(_translate("MainWindow", "Init Cluster:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "K-Means Settings"))
        self.label_7.setText(_translate("MainWindow", "K-Size"))
        self.label_12.setText(_translate("MainWindow", "3"))
        self.label_8.setText(_translate("MainWindow", "Max Iterations"))
        self.label_13.setText(_translate("MainWindow", "50"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Region Grow Settings"))
        self.label.setText(_translate("MainWindow", "Region Threshold"))
        self.label_5.setText(_translate("MainWindow", "6"))
        self.btn_seg_apply.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_seg), _translate("MainWindow", "Segmentation"))
        self.label_14.setText(_translate("MainWindow", "Thresholding Method"))
        self.comboBox_thresh.setItemText(0, _translate("MainWindow", "Optimal"))
        self.comboBox_thresh.setItemText(1, _translate("MainWindow", "Otsu"))
        self.comboBox_thresh.setItemText(2, _translate("MainWindow", "Multilevel"))
        self.checkBox_thresh_global.setText(_translate("MainWindow", "Global"))
        self.checkBox_thresh_local.setText(_translate("MainWindow", "Local"))
        self.label_3.setText(_translate("MainWindow", "#Classes"))
        self.label_4.setText(_translate("MainWindow", "Patch_Size"))
        self.btn_thresh_apply.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_thresh), _translate("MainWindow", "Thresholding"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
        self.actionOpen_Image.setShortcut(_translate("MainWindow", "Ctrl+O"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
