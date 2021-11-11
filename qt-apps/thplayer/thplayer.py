# -*- coding: utf-8 -*-

import info
from Package.QMakePackageBase import *


class subinfo(info.infoclass):

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/BearKidsTeam/thplayer.git'
        #for ver in ["0.23"]:
        #    self.targets[ver] = f"https://github.com/BearKidsTeam/thplayer/archive/v{ver}.tar.gz"
        #    self.archiveNames[ver] = f"thplayer-{ver}.tar.gz"
        #    self.targetInstSrc[ver] = f"thplayer-{ver}"
        self.defaultTarget = "master"

        self.description = "Touhou BGM Player for all platform."
        self.displayName = "TouHou Player"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = None


class Package(QMakePackageBase):
    def __init__(self, **args):
        QMakePackageBase.__init__(self)
        self.subinfo.options.fetch.checkoutSubmodules = True

    def createPackage(self):
        # self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["company"] = "Bear Kids Team"
        self.defines["executable"] = "bin\\thplayer.exe"
        self.defines["license"] = os.path.join(self.sourceDir(), "LICENSE")
        self.defines["icon"] = os.path.join(self.sourceDir(), "assets", "thplayer.ico")
        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")
        return TypePackager.createPackage(self)