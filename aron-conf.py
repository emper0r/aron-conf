#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2016 by Antonio Peña Diaz <emperor.cu@gmail.com>
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
# Aron Config :: License GPLv3+

from PyQt5.Qt import *
from modules import aron


def main():
    import sys
    import time
    QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
    app = QApplication(sys.argv)
    image_splash = QPixmap('./QtUI/ctime_logo.png')
    splash_pix = QPixmap(image_splash)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    qApp.processEvents()
    time.sleep(4)
    window = aron.Main()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

main()
