# -*- coding: utf-8 -*-

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/chirs241097/QMidiPlayer.git'
        for ver in ["0.8.7-1"]:
            self.targets[ver] = f"https://github.com/chirs241097/QMidiPlayer/archive/{ver}.tar.gz"
            self.archiveNames[ver] = f"qmidiplayer-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"QMidiPlayer-{ver}"
        self.defaultTarget = "0.8.7-1"

        self.description = "A free cross-platform midi file player based on libfluidsynth and Qt."
        self.displayName = "QMidiPlayer"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/fluidsynth"] = None
        self.runtimeDependencies["libs/libsdl2"] = None
        self.runtimeDependencies["media-libs/rtmidi"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DBUILD_VISUALIZATION=OFF"

    def createPackage(self):
        # self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["company"] = "Bear Kids Team"
        self.defines["executable"] = "qmidiplayer.exe"
        self.defines["license"] = os.path.join(self.sourceDir(), "COPYING")
        self.defines["icon"] = os.path.join(self.sourceDir(), "img", "qmidiplayer.ico")
        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")
        return TypePackager.createPackage(self)
