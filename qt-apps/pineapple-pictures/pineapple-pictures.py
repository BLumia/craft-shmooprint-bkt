# -*- coding: utf-8 -*-

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/BLumia/pineapple-pictures.git'
        for ver in ["0.5.2", "0.6.0", "0.6.1", "0.6.2", "0.6.5"]:
            self.targets[ver] = f"https://github.com/BLumia/pineapple-pictures/archive/{ver}.tar.gz"
            self.archiveNames[ver] = f"pineapple-pictures-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"Pineapple-Pictures-{ver}"
        self.defaultTarget = "0.6.5"

        self.description = "A homebrew image viewer."
        self.displayName = "Pineapple Pictures"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/qt5/qttools"] = None
        self.runtimeDependencies["libs/exiv2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kimageformats"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["company"] = "Bear Kids Team"
        self.defines["executable"] = "bin\\ppic.exe"
        self.defines["license"] = os.path.join(self.sourceDir(), "LICENSE")
        self.defines["icon"] = os.path.join(self.sourceDir(), "assets", "icons", "app-icon.ico")
        self.defines["file_types"] = [".jpg", ".jpeg", ".jfif", ".gif", ".png", ".webp", ".svg", ".tga", ".psd", ".xcf", ".kra"]
        # Icon used by AppxPackager
        self.defines["icon_png"] = os.path.join(self.packageDir(), "icons", "150-apps-pineapple-pictures.png")
        self.defines["icon_png_44"] = os.path.join(self.packageDir(), "icons", "44-apps-pineapple-pictures.png")
        self.addExecutableFilter(r"(bin|libexec)/(?!(ppic|update-mime-database)).*")
        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")
        return TypePackager.createPackage(self)