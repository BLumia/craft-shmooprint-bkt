import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['4.0.0']:
            self.targets[ver] = f"https://github.com/thestk/rtmidi/archive/{ver}.tar.gz"
            self.archiveNames[ver] = f"rtmidi-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"rtmidi-{ver}"

        self.targetDigests['4.0.0'] = (['d32de9ceebf6d969537e9a9720925a1ac7f6a8bc4ac4ce7c58c01434f4e54f44'], CraftHash.HashAlgorithm.SHA256)
        self.description = "A set of C++ classes that provide a common API for realtime MIDI input/output across Linux (ALSA & JACK), Macintosh OS X (CoreMIDI) and Windows (Multimedia)"
        self.webpage = "http://www.music.mcgill.ca/~gary/rtmidi/"
        self.defaultTarget = '4.0.0'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["dev-utils/pkg-config"] = None
        self.runtimeDependencies["libs/glib"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-D__WINDOWS_MM__='1'"
