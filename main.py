import sys
# from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication
# from PySide6.QtCore import *
from ui import fun_bind, main_ui

app = QApplication(sys.argv)
m_ui = main_ui.Ui_MainWindow()
widgets = [m_ui.port_ui_w, m_ui.b64_ui_w, m_ui.scan_for_ip]
buts = [m_ui.port_but, m_ui.b64_but, m_ui.pushButton]

for aa in range(len(buts)):
    buts[aa].clicked.connect(lambda y=False, aa=aa: fun_bind.ui_show(aa, widgets))

m_ui.pushButton_2.clicked.connect(
    lambda: fun_bind.port_scan2(m_ui.lineEdit.text(), m_ui.lineEdit_2.text(), m_ui.lineEdit_3.text()))
m_ui.b64_swap_but.clicked.connect(lambda: fun_bind.swap_text(m_ui.b64dec, m_ui.b64src))
m_ui.b64_enc_but.clicked.connect(lambda: fun_bind.b64_enc_text(m_ui.b64dec, m_ui.b64src))
m_ui.b64_dec_but.clicked.connect(lambda: fun_bind.b64_dec_text(m_ui.b64dec, m_ui.b64src))
fun_bind.a.finished.connect(lambda: m_ui.textBrowser.setText(fun_bind.res))
m_ui.sc_ip.clicked.connect(lambda: fun_bind.ip_scan(m_ui.min_ip.text(), m_ui.max_ip.text()))
# fun_bind.show_info()
fun_bind.a2.finished.connect(lambda: m_ui.ip_res.setText(fun_bind.res2))
m_ui.show()
sys.exit(app.exec())
