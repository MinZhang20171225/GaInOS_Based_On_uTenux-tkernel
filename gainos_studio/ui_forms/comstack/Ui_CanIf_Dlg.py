# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\parai@foxmail.com\nt\gainos-tkernel\gainos_studio\ui_forms\comstack\CanIf_Dlg.ui'
#
# Created: Sun Apr 21 21:43:46 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CanIf_Dlg(object):
    def setupUi(self, CanIf_Dlg):
        CanIf_Dlg.setObjectName(_fromUtf8("CanIf_Dlg"))
        CanIf_Dlg.resize(965, 588)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        CanIf_Dlg.setFont(font)
        self.groupBox = QtGui.QGroupBox(CanIf_Dlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 32, 250, 112))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbxDevErr = QtGui.QCheckBox(self.layoutWidget)
        self.cbxDevErr.setObjectName(_fromUtf8("cbxDevErr"))
        self.verticalLayout.addWidget(self.cbxDevErr)
        self.cbxVersionInfo = QtGui.QCheckBox(self.layoutWidget)
        self.cbxVersionInfo.setObjectName(_fromUtf8("cbxVersionInfo"))
        self.verticalLayout.addWidget(self.cbxVersionInfo)
        self.cbxDlcCheck = QtGui.QCheckBox(self.layoutWidget)
        self.cbxDlcCheck.setObjectName(_fromUtf8("cbxDlcCheck"))
        self.verticalLayout.addWidget(self.cbxDlcCheck)
        self.cbxRuntimePduCfg = QtGui.QCheckBox(self.layoutWidget)
        self.cbxRuntimePduCfg.setObjectName(_fromUtf8("cbxRuntimePduCfg"))
        self.verticalLayout.addWidget(self.cbxRuntimePduCfg)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 40, 551, 95))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_34 = QtGui.QLabel(self.layoutWidget1)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout.addWidget(self.label_34)
        self.leBusoffNf = QtGui.QLineEdit(self.layoutWidget1)
        self.leBusoffNf.setMinimumSize(QtCore.QSize(250, 0))
        self.leBusoffNf.setText(_fromUtf8(""))
        self.leBusoffNf.setObjectName(_fromUtf8("leBusoffNf"))
        self.horizontalLayout.addWidget(self.leBusoffNf)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_35 = QtGui.QLabel(self.layoutWidget1)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_24.addWidget(self.label_35)
        self.leErrorNf = QtGui.QLineEdit(self.layoutWidget1)
        self.leErrorNf.setText(_fromUtf8(""))
        self.leErrorNf.setObjectName(_fromUtf8("leErrorNf"))
        self.horizontalLayout_24.addWidget(self.leErrorNf)
        self.verticalLayout_10.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.label_36 = QtGui.QLabel(self.layoutWidget1)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_37.addWidget(self.label_36)
        self.cmbxSoftwareFilterType = QtGui.QComboBox(self.layoutWidget1)
        self.cmbxSoftwareFilterType.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxSoftwareFilterType.setObjectName(_fromUtf8("cmbxSoftwareFilterType"))
        self.cmbxSoftwareFilterType.addItem(_fromUtf8(""))
        self.cmbxSoftwareFilterType.addItem(_fromUtf8(""))
        self.cmbxSoftwareFilterType.addItem(_fromUtf8(""))
        self.cmbxSoftwareFilterType.addItem(_fromUtf8(""))
        self.cmbxSoftwareFilterType.addItem(_fromUtf8(""))
        self.horizontalLayout_37.addWidget(self.cmbxSoftwareFilterType)
        self.verticalLayout_10.addLayout(self.horizontalLayout_37)
        self.groupBox_2 = QtGui.QGroupBox(CanIf_Dlg)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 941, 411))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.trCanIfCfg = QtGui.QTreeWidget(self.groupBox_2)
        self.trCanIfCfg.setGeometry(QtCore.QRect(20, 30, 256, 371))
        self.trCanIfCfg.setObjectName(_fromUtf8("trCanIfCfg"))
        item_0 = QtGui.QTreeWidgetItem(self.trCanIfCfg)
        self.tabCfg = QtGui.QTabWidget(self.groupBox_2)
        self.tabCfg.setGeometry(QtCore.QRect(440, 20, 481, 361))
        self.tabCfg.setObjectName(_fromUtf8("tabCfg"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget2 = QtGui.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(21, 21, 349, 62))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_33 = QtGui.QLabel(self.layoutWidget2)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_36.addWidget(self.label_33)
        self.leChannelName = QtGui.QLineEdit(self.layoutWidget2)
        self.leChannelName.setText(_fromUtf8(""))
        self.leChannelName.setObjectName(_fromUtf8("leChannelName"))
        self.horizontalLayout_36.addWidget(self.leChannelName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_44 = QtGui.QLabel(self.layoutWidget2)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.horizontalLayout_23.addWidget(self.label_44)
        self.cmbxCanHwCtrl = QtGui.QComboBox(self.layoutWidget2)
        self.cmbxCanHwCtrl.setMinimumSize(QtCore.QSize(231, 0))
        self.cmbxCanHwCtrl.setObjectName(_fromUtf8("cmbxCanHwCtrl"))
        self.horizontalLayout_23.addWidget(self.cmbxCanHwCtrl)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.tabCfg.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget3 = QtGui.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(21, 21, 433, 95))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_32 = QtGui.QLabel(self.layoutWidget3)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_35.addWidget(self.label_32)
        self.leHthName = QtGui.QLineEdit(self.layoutWidget3)
        self.leHthName.setText(_fromUtf8(""))
        self.leHthName.setObjectName(_fromUtf8("leHthName"))
        self.horizontalLayout_35.addWidget(self.leHthName)
        self.verticalLayout_5.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_25 = QtGui.QLabel(self.layoutWidget3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_28.addWidget(self.label_25)
        self.cmbxHthType = QtGui.QComboBox(self.layoutWidget3)
        self.cmbxHthType.setMinimumSize(QtCore.QSize(320, 0))
        self.cmbxHthType.setObjectName(_fromUtf8("cmbxHthType"))
        self.cmbxHthType.addItem(_fromUtf8(""))
        self.cmbxHthType.addItem(_fromUtf8(""))
        self.horizontalLayout_28.addWidget(self.cmbxHthType)
        self.verticalLayout_5.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_26 = QtGui.QLabel(self.layoutWidget3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_29.addWidget(self.label_26)
        self.cmbxHthIdSymRef = QtGui.QComboBox(self.layoutWidget3)
        self.cmbxHthIdSymRef.setMinimumSize(QtCore.QSize(270, 0))
        self.cmbxHthIdSymRef.setObjectName(_fromUtf8("cmbxHthIdSymRef"))
        self.horizontalLayout_29.addWidget(self.cmbxHthIdSymRef)
        self.verticalLayout_5.addLayout(self.horizontalLayout_29)
        self.tabCfg.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 20, 435, 126))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.label_37 = QtGui.QLabel(self.layoutWidget4)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.horizontalLayout_38.addWidget(self.label_37)
        self.leHrhName = QtGui.QLineEdit(self.layoutWidget4)
        self.leHrhName.setText(_fromUtf8(""))
        self.leHrhName.setObjectName(_fromUtf8("leHrhName"))
        self.horizontalLayout_38.addWidget(self.leHrhName)
        self.verticalLayout_6.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.label_27 = QtGui.QLabel(self.layoutWidget4)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_30.addWidget(self.label_27)
        self.cmbxHrhType = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxHrhType.setMinimumSize(QtCore.QSize(320, 0))
        self.cmbxHrhType.setObjectName(_fromUtf8("cmbxHrhType"))
        self.cmbxHrhType.addItem(_fromUtf8(""))
        self.cmbxHrhType.addItem(_fromUtf8(""))
        self.horizontalLayout_30.addWidget(self.cmbxHrhType)
        self.verticalLayout_6.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_28 = QtGui.QLabel(self.layoutWidget4)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_31.addWidget(self.label_28)
        self.cmbxHrhIdSymRef = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxHrhIdSymRef.setMinimumSize(QtCore.QSize(270, 0))
        self.cmbxHrhIdSymRef.setObjectName(_fromUtf8("cmbxHrhIdSymRef"))
        self.horizontalLayout_31.addWidget(self.cmbxHrhIdSymRef)
        self.verticalLayout_6.addLayout(self.horizontalLayout_31)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.cbxSoftwareFilterHrh = QtGui.QCheckBox(self.layoutWidget4)
        self.cbxSoftwareFilterHrh.setObjectName(_fromUtf8("cbxSoftwareFilterHrh"))
        self.verticalLayout_8.addWidget(self.cbxSoftwareFilterHrh)
        self.tabCfg.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget5 = QtGui.QWidget(self.tab_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 20, 418, 194))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_40 = QtGui.QLabel(self.layoutWidget5)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.horizontalLayout_4.addWidget(self.label_40)
        self.leTxPduName = QtGui.QLineEdit(self.layoutWidget5)
        self.leTxPduName.setText(_fromUtf8(""))
        self.leTxPduName.setObjectName(_fromUtf8("leTxPduName"))
        self.horizontalLayout_4.addWidget(self.leTxPduName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_29 = QtGui.QLabel(self.layoutWidget5)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_2.addWidget(self.label_29)
        self.cmbxTxPduCanType = QtGui.QComboBox(self.layoutWidget5)
        self.cmbxTxPduCanType.setMinimumSize(QtCore.QSize(300, 0))
        self.cmbxTxPduCanType.setObjectName(_fromUtf8("cmbxTxPduCanType"))
        self.cmbxTxPduCanType.addItem(_fromUtf8(""))
        self.cmbxTxPduCanType.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbxTxPduCanType)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.spbxTxPduCanId = QtGui.QSpinBox(self.layoutWidget5)
        self.spbxTxPduCanId.setMinimumSize(QtCore.QSize(300, 0))
        self.spbxTxPduCanId.setObjectName(_fromUtf8("spbxTxPduCanId"))
        self.horizontalLayout_3.addWidget(self.spbxTxPduCanId)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_30 = QtGui.QLabel(self.layoutWidget5)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_6.addWidget(self.label_30)
        self.cmbxTxPduCanIdType = QtGui.QComboBox(self.layoutWidget5)
        self.cmbxTxPduCanIdType.setMinimumSize(QtCore.QSize(300, 0))
        self.cmbxTxPduCanIdType.setObjectName(_fromUtf8("cmbxTxPduCanIdType"))
        self.cmbxTxPduCanIdType.addItem(_fromUtf8(""))
        self.cmbxTxPduCanIdType.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cmbxTxPduCanIdType)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.layoutWidget5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.spbxTxPduDlc = QtGui.QSpinBox(self.layoutWidget5)
        self.spbxTxPduDlc.setMinimumSize(QtCore.QSize(200, 0))
        self.spbxTxPduDlc.setObjectName(_fromUtf8("spbxTxPduDlc"))
        self.horizontalLayout_5.addWidget(self.spbxTxPduDlc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_31 = QtGui.QLabel(self.layoutWidget5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_7.addWidget(self.label_31)
        self.cmbxTxPduConfirmation = QtGui.QComboBox(self.layoutWidget5)
        self.cmbxTxPduConfirmation.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxTxPduConfirmation.setObjectName(_fromUtf8("cmbxTxPduConfirmation"))
        self.cmbxTxPduConfirmation.addItem(_fromUtf8(""))
        self.cmbxTxPduConfirmation.addItem(_fromUtf8(""))
        self.cmbxTxPduConfirmation.addItem(_fromUtf8(""))
        self.cmbxTxPduConfirmation.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cmbxTxPduConfirmation)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.tabCfg.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.widget = QtGui.QWidget(self.tab_5)
        self.widget.setGeometry(QtCore.QRect(20, 22, 418, 260))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_41 = QtGui.QLabel(self.widget)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.horizontalLayout_8.addWidget(self.label_41)
        self.leRxPduName = QtGui.QLineEdit(self.widget)
        self.leRxPduName.setText(_fromUtf8(""))
        self.leRxPduName.setObjectName(_fromUtf8("leRxPduName"))
        self.horizontalLayout_8.addWidget(self.leRxPduName)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_38 = QtGui.QLabel(self.widget)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.horizontalLayout_9.addWidget(self.label_38)
        self.cmbxRxPduCanType = QtGui.QComboBox(self.widget)
        self.cmbxRxPduCanType.setMinimumSize(QtCore.QSize(300, 0))
        self.cmbxRxPduCanType.setObjectName(_fromUtf8("cmbxRxPduCanType"))
        self.cmbxRxPduCanType.addItem(_fromUtf8(""))
        self.cmbxRxPduCanType.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.cmbxRxPduCanType)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_10.addWidget(self.label_3)
        self.spbxRxPduCanId = QtGui.QSpinBox(self.widget)
        self.spbxRxPduCanId.setMinimumSize(QtCore.QSize(300, 0))
        self.spbxRxPduCanId.setObjectName(_fromUtf8("spbxRxPduCanId"))
        self.horizontalLayout_10.addWidget(self.spbxRxPduCanId)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_39 = QtGui.QLabel(self.widget)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.horizontalLayout_11.addWidget(self.label_39)
        self.cmbxRxPduCanIdType = QtGui.QComboBox(self.widget)
        self.cmbxRxPduCanIdType.setMinimumSize(QtCore.QSize(300, 0))
        self.cmbxRxPduCanIdType.setObjectName(_fromUtf8("cmbxRxPduCanIdType"))
        self.cmbxRxPduCanIdType.addItem(_fromUtf8(""))
        self.cmbxRxPduCanIdType.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.cmbxRxPduCanIdType)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_45 = QtGui.QLabel(self.widget)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_15.addWidget(self.label_45)
        self.leRxPduIdMask = QtGui.QLineEdit(self.widget)
        self.leRxPduIdMask.setText(_fromUtf8(""))
        self.leRxPduIdMask.setObjectName(_fromUtf8("leRxPduIdMask"))
        self.horizontalLayout_15.addWidget(self.leRxPduIdMask)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_12.addWidget(self.label_4)
        self.spbxRxPduDlc = QtGui.QSpinBox(self.widget)
        self.spbxRxPduDlc.setMinimumSize(QtCore.QSize(200, 0))
        self.spbxRxPduDlc.setObjectName(_fromUtf8("spbxRxPduDlc"))
        self.horizontalLayout_12.addWidget(self.spbxRxPduDlc)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_42 = QtGui.QLabel(self.widget)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.horizontalLayout_13.addWidget(self.label_42)
        self.cmbxRxPduIndication = QtGui.QComboBox(self.widget)
        self.cmbxRxPduIndication.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxRxPduIndication.setObjectName(_fromUtf8("cmbxRxPduIndication"))
        self.cmbxRxPduIndication.addItem(_fromUtf8(""))
        self.cmbxRxPduIndication.addItem(_fromUtf8(""))
        self.cmbxRxPduIndication.addItem(_fromUtf8(""))
        self.cmbxRxPduIndication.addItem(_fromUtf8(""))
        self.cmbxRxPduIndication.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.cmbxRxPduIndication)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_43 = QtGui.QLabel(self.widget)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.horizontalLayout_14.addWidget(self.label_43)
        self.leRxPduUserIndication = QtGui.QLineEdit(self.widget)
        self.leRxPduUserIndication.setText(_fromUtf8(""))
        self.leRxPduUserIndication.setObjectName(_fromUtf8("leRxPduUserIndication"))
        self.horizontalLayout_14.addWidget(self.leRxPduUserIndication)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.tabCfg.addTab(self.tab_5, _fromUtf8(""))
        self.layoutWidget6 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget6.setGeometry(QtCore.QRect(290, 51, 131, 95))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAdd = QtGui.QPushButton(self.layoutWidget6)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnAdd2 = QtGui.QPushButton(self.layoutWidget6)
        self.btnAdd2.setObjectName(_fromUtf8("btnAdd2"))
        self.verticalLayout_2.addWidget(self.btnAdd2)
        self.btnDel = QtGui.QPushButton(self.layoutWidget6)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.verticalLayout_2.addWidget(self.btnDel)

        self.retranslateUi(CanIf_Dlg)
        self.tabCfg.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(CanIf_Dlg)

    def retranslateUi(self, CanIf_Dlg):
        CanIf_Dlg.setWindowTitle(QtGui.QApplication.translate("CanIf_Dlg", "Can Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CanIf_Dlg", "CanIf General", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxDevErr.setText(QtGui.QApplication.translate("CanIf_Dlg", "DevErrorDetection", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxVersionInfo.setText(QtGui.QApplication.translate("CanIf_Dlg", "VersionInfoApi", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxDlcCheck.setText(QtGui.QApplication.translate("CanIf_Dlg", "DLC Check Support", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxRuntimePduCfg.setText(QtGui.QApplication.translate("CanIf_Dlg", "Runtime Pdu Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("CanIf_Dlg", "Busoff Notification Function:", None, QtGui.QApplication.UnicodeUTF8))
        self.leBusoffNf.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If want to turn off notification,input &quot;NULL&quot;.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("CanIf_Dlg", "Error Notification Function:", None, QtGui.QApplication.UnicodeUTF8))
        self.leErrorNf.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If want to turn off notification,input &quot;NULL&quot;.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("CanIf_Dlg", "Software Filter Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSoftwareFilterType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_SOFTFILTER_TYPE_MASK", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSoftwareFilterType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_SOFTFILTER_TYPE_BINARY", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSoftwareFilterType.setItemText(2, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_SOFTFILTER_TYPE_INDEX", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSoftwareFilterType.setItemText(3, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_SOFTFILTER_TYPE_LINEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSoftwareFilterType.setItemText(4, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_SOFTFILTER_TYPE_TABLE", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CanIf_Dlg", "CanIf Entities", None, QtGui.QApplication.UnicodeUTF8))
        self.trCanIfCfg.headerItem().setText(0, QtGui.QApplication.translate("CanIf_Dlg", "Can", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.trCanIfCfg.isSortingEnabled()
        self.trCanIfCfg.setSortingEnabled(False)
        self.trCanIfCfg.topLevelItem(0).setText(0, QtGui.QApplication.translate("CanIf_Dlg", "Channels", None, QtGui.QApplication.UnicodeUTF8))
        self.trCanIfCfg.setSortingEnabled(__sortingEnabled)
        self.label_33.setText(QtGui.QApplication.translate("CanIf_Dlg", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Hw Ctrl:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab), QtGui.QApplication.translate("CanIf_Dlg", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("CanIf_Dlg", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("CanIf_Dlg", "Hth Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHthType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CAN_ARC_HANDLE_TYPE_BASIC", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHthType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CAN_ARC_HANDLE_TYPE_FULL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("CanIf_Dlg", "CanIfHthIdSymRef:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_2), QtGui.QApplication.translate("CanIf_Dlg", "Hth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("CanIf_Dlg", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("CanIf_Dlg", "Hrh Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHrhType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CAN_ARC_HANDLE_TYPE_BASIC", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHrhType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CAN_ARC_HANDLE_TYPE_FULL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("CanIf_Dlg", "CanIfHrhIdSymRef:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSoftwareFilterHrh.setText(QtGui.QApplication.translate("CanIf_Dlg", "CanIfSoftwareFilterHrh", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_4), QtGui.QApplication.translate("CanIf_Dlg", "Hrh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("CanIf_Dlg", "Global Pdu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduCanType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_PDU_TYPE_STATIC", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduCanType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_PDU_TYPE_DYNAMIC", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Id Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduCanIdType.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This type is really decided by Can Hth,Configue it has no affect.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduCanIdType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_CAN_ID_TYPE_11", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduCanIdType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_CAN_ID_TYPE_29", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Data Length Code:", None, QtGui.QApplication.UnicodeUTF8))
        self.spbxTxPduDlc.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this means nothing,so you have no need to configure it.Just make compatible with arccore.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("CanIf_Dlg", "Confirmation API:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduConfirmation.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "NULL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduConfirmation.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "PduR_CanIfTxConfirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduConfirmation.setItemText(2, QtGui.QApplication.translate("CanIf_Dlg", "CanTp_TxConfirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxTxPduConfirmation.setItemText(3, QtGui.QApplication.translate("CanIf_Dlg", "CanIf_UserTxConfirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_3), QtGui.QApplication.translate("CanIf_Dlg", "Tx Pdu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("CanIf_Dlg", "Global Pdu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduCanType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_PDU_TYPE_STATIC", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduCanType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_PDU_TYPE_DYNAMIC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.spbxRxPduCanId.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Special CanId,If software filter mask on,only Can Frames with this CanId can be received.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Id Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduCanIdType.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unsupport configure item defined by Arccore,you have no need to configure it.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduCanIdType.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_CAN_ID_TYPE_11", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduCanIdType.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CANIF_CAN_ID_TYPE_29", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Id Mask:", None, QtGui.QApplication.UnicodeUTF8))
        self.leRxPduIdMask.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if software filter on,then only if &lt;the reveived Can Id&gt; &amp; Mask == &lt;Configured Can Id here&gt; &amp; Mask,Then the Pdu can be reveived(pass the filter) and a notification to upper layer can be generated.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CanIf_Dlg", "Can Data Length Code:", None, QtGui.QApplication.UnicodeUTF8))
        self.spbxRxPduDlc.setToolTip(QtGui.QApplication.translate("CanIf_Dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note:Rx Data\'s DLC must be bigger than the configured value,or the Data will be droped if DLC check enabled.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("CanIf_Dlg", "Indication Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduIndication.setItemText(0, QtGui.QApplication.translate("CanIf_Dlg", "CAN_NM", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduIndication.setItemText(1, QtGui.QApplication.translate("CanIf_Dlg", "CAN_TP", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduIndication.setItemText(2, QtGui.QApplication.translate("CanIf_Dlg", "CAN_PDUR", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduIndication.setItemText(3, QtGui.QApplication.translate("CanIf_Dlg", "J1939TP", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxRxPduIndication.setItemText(4, QtGui.QApplication.translate("CanIf_Dlg", "CAN_SPECIAL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("CanIf_Dlg", "User Indication:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_5), QtGui.QApplication.translate("CanIf_Dlg", "Rx Pdu", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("CanIf_Dlg", "Add Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd2.setText(QtGui.QApplication.translate("CanIf_Dlg", "Add Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("CanIf_Dlg", "Del", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CanIf_Dlg = QtGui.QDialog()
    ui = Ui_CanIf_Dlg()
    ui.setupUi(CanIf_Dlg)
    CanIf_Dlg.show()
    sys.exit(app.exec_())

