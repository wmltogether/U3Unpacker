# /usr/bin/python2
# -*- coding:utf-8 -*-
'''
2016-12-16 Unity Assets Reader完全重构
@author: wmltogether
'''
import os
import struct
import md5
import BinaryHelper


class ClassID:

    def __init__(self, major_ver, minor_ver):
        self.classDict = {}
        self.version = major_ver * 100 + minor_ver
        self._set()

    def _set(self):
        if (505 <= self.version):
            self.classDict[2] = ("Texture", ".tex")

        elif (305 <= self.version < 505):
            self.classDict[1] = ('GameObject', '.GameObject')
            self.classDict[2] = ('Component', '.Component')
            self.classDict[3] = ('LevelGameManager', '.LevelGameManager')
            self.classDict[4] = ('Transform', '.Transform')
            self.classDict[5] = ('TimeManager', '.TimeManager')
            self.classDict[6] = ('GlobalGameManager', '.GlobalGameManager')
            self.classDict[8] = ('Behaviour', '.Behaviour')
            self.classDict[9] = ('GameManager', '.GameManager')
            self.classDict[11] = ('AudioManager', '.AudioManager')
            self.classDict[12] = ('ParticleAnimator', '.ParticleAnimator')
            self.classDict[13] = ('InputManager', '.InputManager')
            self.classDict[15] = ('EllipsoidParticleEmitter',
                                  '.EllipsoidParticleEmitter')
            self.classDict[17] = ('Pipeline', '.Pipeline')
            self.classDict[18] = ('EditorExtension', '.EditorExtension')
            self.classDict[19] = ('Physics2DSettings', '.Physics2DSettings')
            self.classDict[20] = ('Camera', '.Camera')
            self.classDict[21] = ('Material', '.Material')
            self.classDict[27] = ('Texture', '.tex')  # texture
            self.classDict[28] = ('Texture2D', '.tex')  # texture2d
            self.classDict[29] = ('SceneSettings', '.SceneSettings')
            self.classDict[30] = ('GraphicsSettings', '.GraphicsSettings')
            self.classDict[33] = ('MeshFilter', '.MeshFilter')
            self.classDict[41] = ('OcclusionPortal', '.OcclusionPortal')
            self.classDict[43] = ('Mesh', '.mesh')
            self.classDict[45] = ('Skybox', '.Skybox')
            self.classDict[47] = ('QualitySettings', '.QualitySettings')
            self.classDict[48] = ('Shader', '.shader')
            # All text assets have classe id 49
            self.classDict[49] = ('TextAsset', '.TextAsset')
            self.classDict[50] = ('Rigidbody2D', '.Rigidbody2D')
            self.classDict[51] = ('Physics2DManager', '.Physics2DManager')
            self.classDict[53] = ('Collider2D', '.Collider2D')
            self.classDict[54] = ('Rigidbody', '.Rigidbody')
            self.classDict[55] = ('PhysicsManager', '.PhysicsManager')
            self.classDict[56] = ('Collider', '.Collider')
            self.classDict[57] = ('Joint', '.Joint')
            self.classDict[58] = ('CircleCollider2D', '.CircleCollider2D')
            self.classDict[59] = ('HingeJoint', '.HingeJoint')
            self.classDict[60] = ('PolygonCollider2D', '.PolygonCollider2D')
            self.classDict[61] = ('BoxCollider2D', '.BoxCollider2D')
            self.classDict[62] = ('PhysicsMaterial2D', '.PhysicsMaterial2D')
            self.classDict[64] = ('MeshCollider', '.MeshCollider')
            self.classDict[65] = ('BoxCollider', '.BoxCollider')
            self.classDict[66] = ('SpriteCollider2D', '.SpriteCollider2D')
            self.classDict[68] = ('EdgeCollider2D', '.EdgeCollider2D')
            self.classDict[72] = ('ComputeShader', '.ComputeShader')
            self.classDict[74] = ('AnimationClip', '.AnimationClip')
            self.classDict[75] = ('ConstantForce', '.ConstantForce')
            self.classDict[76] = ('WorldParticleCollider',
                                  '.WorldParticleCollider')
            self.classDict[78] = ('TagManager', '.TagManager')
            self.classDict[81] = ('AudioListener', '.AudioListener')
            self.classDict[82] = ('AudioSource', '.AudioSource')
            self.classDict[83] = ('AudioClip', '.AudioClip')
            self.classDict[84] = ('RenderTexture', '.tex')
            self.classDict[87] = ('MeshParticleEmitter',
                                  '.MeshParticleEmitter')
            self.classDict[88] = ('ParticleEmitter', '.ParticleEmitter')
            self.classDict[89] = ('Cubemap', '.Cubemap')
            self.classDict[90] = ('Avatar', '.Avatar')
            self.classDict[91] = ('AnimatorController', '.AnimatorController')
            self.classDict[92] = ('GUILayer', '.GUILayer')
            self.classDict[93] = (
                'RuntimeAnimatorController', '.RuntimeAnimatorController')
            self.classDict[94] = ('ScriptMapper', '.ScriptMapper')
            self.classDict[95] = ('Animator', '.Animator')
            self.classDict[96] = ('TrailRenderer', '.TrailRenderer')
            self.classDict[98] = ('DelayedCallManager', '.DelayedCallManager')
            self.classDict[102] = ('TextMesh', '.TextMesh')  # textmesh
            self.classDict[104] = ('RenderSettings', '.RenderSettings')
            self.classDict[108] = ('Light', '.Light')
            self.classDict[109] = ('CGProgram', '.CGProgram')
            self.classDict[110] = ('BaseAnimationTrack', '.BaseAnimationTrack')
            self.classDict[111] = ('Animation', '.Animation')
            pass
        else:
            pass

    def GetClassDict(self):
        return self.classDict


class Uitlity(object):

    def __init__(self):

        pass

    @staticmethod
    def GetObbMD5(obbName):
        with open(obbName, "rb") as fs:
            fs.seek(-0x10016, 2)
            string = fs.read(0x10016)
            m = md5.new()

            m.update(string)
            return m.hexdigest()

    @staticmethod
    def GetFileSize(fName):
        return os.path.getsize(fName)


class AssetsLoader(object):
    UnityRuntimePlatform = {4: "Mac OS X",
                            5: "PC",
                            6: "Web Player",
                            7: "Web Stream",
                            9: "iOS",
                            10: "PS3",
                            11: "Xbox360",
                            13: "Android"
                            }

    def __init__(self, assetName):
        self.packageName = assetName
        self.packageSize = os.path.getsize(assetName)
        self.packageMajorVersion = 0
        self.packageMinorVersion = 0
        self.packagePatchVersion = ""
        self.packageItemNums = 0

        self.packageGen = 0  # 包版本号
        self.headerSize = 0
        self._tableSize = 0
        self.ObjectsEntryOffset = 0
        self.IndexEntryOffset = 0
        self.platformType = 0
        self.baseStream = None
        self.EntryList = []
        self.ClassIDDict = {}
        self.Load()

        print(
            "**********************\n" +
            " Unity Package: \t%s\n" % self.packageName +
            " PackageVersion: \t%d\n" % self.packageGen +
            " Unity Version: \t%d.%d.%s\n" % (self.packageMajorVersion,
                                              self.packageMinorVersion,
                                              self.packagePatchVersion) +
            " Platform: \t%d\n" % self.platformType +
            " Object nums: \t%d\n" % self.packageItemNums +
            "**********************\n")

    def Load(self):
        self.baseStream = open(self.packageName, "rb+")
        br = BinaryHelper.BinaryReader(self.baseStream)
        self._tableSize = br.ReadBEUInt32()
        self.packageSize = br.ReadBEUInt32()
        self.packageGen = br.ReadBEUInt32()
        self.ObjectsEntryOffset = br.ReadBEUInt32()

        self.headerSize = self.ObjectsEntryOffset
        if (self.packageGen == 9):  # unity 3.5 - 4.6
            br.Seek(4, 1)
            version = br.ReadCString()
            br.Seek(1, 1)
            self.platformType = br.ReadUInt32()
            self._checkVersion(version)
            br.Seek(8, 1)
            self.IndexEntryOffset = br.Tell()
            self.ClassIDDict = ClassID(
                self.packageMajorVersion,
                self.packageMinorVersion).GetClassDict()

            self._getPackageIndex35()

        elif (self.packageGen == 15):  # unity 5.0.1 - 5.4
            br.Seek(4, 1)
            version = br.ReadCString()
            br.Seek(1, 1)
            self.platformType = br.ReadUInt32()
            self._checkVersion(version)
            unkBool = ord(br.ReadByte())
            base_nums = br.ReadUInt32()
            for i in xrange(base_nums):
                m0 = br.ReadInt32()
                if (m0 < 0):
                    br.Seek(0x20, 1)
                else:
                    br.Seek(0x10, 1)
            self.IndexEntryOffset = br.Tell()
            self.ClassIDDict = ClassID(
                self.packageMajorVersion,
                self.packageMinorVersion).GetClassDict()

            self._getPackageIndex50()

        elif (self.packageGen == 17):  # unity 5.5.0
            br.Seek(4, 1)
            version = br.ReadCString()
            br.Seek(1, 1)
            self.platformType = br.ReadUInt32()
            self._checkVersion(version)
            unkBool = ord(br.ReadByte())
            base_nums = br.ReadUInt32()

            for i in xrange(base_nums):
                m0 = br.ReadInt32()
                m1 = ord(br.ReadByte())
                m2 = br.ReadInt16()
                if (m1 == 0 and m2 < 0):
                    br.Seek(0x10, 1)
                else:
                    br.Seek(0x20, 1)

            self.ClassIDDict = ClassID(
                self.packageMajorVersion,
                self.packageMinorVersion).GetClassDict()
            self.IndexEntryOffset = br.Tell()
            self._getPackageIndex55()

        pass

    def _getPackageIndex35(self):
        # 3.5.x - 4.6.x的打包格式
        br = BinaryHelper.BinaryReader(self.baseStream)
        br.Seek(self.IndexEntryOffset)
        self.packageItemNums = br.ReadInt32()
        position = br.Tell()
        for i in xrange(self.packageItemNums):
            br.Seek(position, 0)
            m_pathID = br.ReadInt32()
            t_pos = br.Tell()  # 记录offset位置
            (offset, size) = struct.unpack(
                "2I", self.baseStream.read(0x8))
            classid0 = br.ReadInt32()
            classid = br.ReadInt32()

            position = br.Tell()

            # 记录到entry class
            index_entry = self.IndexEntry()
            index_entry.IndexID = i
            index_entry.Offset = offset + self.headerSize
            index_entry.Size = size
            index_entry.ClassID = classid
            index_entry.Offset_ptr = t_pos

            br.Seek(offset + self.headerSize, 0)
            # 分析可能的文件名和文件类型
            fname = ""
            if (index_entry.Size > 4):
                fname_length = br.ReadInt32()
                if (0 < fname_length < 0x20):
                    fname = self._fixAsciiName(br.ReadBytes(fname_length))
            ext_name = ".bin"
            if (index_entry.ClassID in self.ClassIDDict):
                ext_name = self.ClassIDDict[index_entry.ClassID][1]
            index_entry.ObjectName = fname + ext_name

            # 存储到list
            self.EntryList.append(index_entry)
        pass

    def _getPackageIndex50(self):
        # 5.0.1 - 5.4.x 的打包格式
        br = BinaryHelper.BinaryReader(self.baseStream)
        br.Seek(self.IndexEntryOffset)
        self.packageItemNums = br.ReadInt32()
        position = br.Tell()
        for i in xrange(self.packageItemNums):
            # 每个entry都要对齐到4字节
            br.Seek(position, 0)
            if br.Tell() % 4 != 0:
                br.Seek(4 - br.Tell() % 4, 1)
            m_pathID = br.ReadInt64()
            t_pos = br.Tell()  # 记录offset位置
            (offset, size) = struct.unpack(
                "2I", self.baseStream.read(0x8))
            classid = br.ReadInt32()
            classid2 = br.ReadInt16()
            unk = br.ReadInt16()
            unkByte = br.ReadByte()

            position = br.Tell()
            # 记录到entry class
            index_entry = self.IndexEntry()
            index_entry.IndexID = i
            index_entry.Offset = offset + self.headerSize
            index_entry.Size = size
            index_entry.ClassID = classid
            index_entry.Offset_ptr = t_pos

            br.Seek(offset + self.headerSize, 0)
            # 分析可能的文件名和文件类型
            fname = ""
            if (index_entry.Size > 4):
                fname_length = br.ReadInt32()
                if (0 < fname_length < 0x20):
                    fname = self._fixAsciiName(br.ReadBytes(fname_length))
            ext_name = ".bin"
            if (index_entry.ClassID in self.ClassIDDict):
                ext_name = self.ClassIDDict[index_entry.ClassID][1]
            index_entry.ObjectName = fname + ext_name

            # 存储到list
            self.EntryList.append(index_entry)

        pass

    def _getPackageIndex55(self):
        # 5.5.x
        # print("Index Entry:%08x"%self.IndexEntryOffset)
        br = BinaryHelper.BinaryReader(self.baseStream)
        br.Seek(self.IndexEntryOffset)

        self.packageItemNums = br.ReadInt32() # 实际是读4字节，后面再按照4字节补齐
        position = br.Tell()
        for i in xrange(self.packageItemNums):
            br.Seek(position, 0)
            if br.Tell() % 4 != 0:
                br.Seek(4 - br.Tell() % 4, 1)
            (index_id, unk) = struct.unpack("2I", self.baseStream.read(0x8))
            t_pos = br.Tell()

            (offset, size, classid) = struct.unpack(
                "3I", self.baseStream.read(0xc))

            # print("%08x"%(offset + self.headerSize))
            position = br.Tell()
            index_entry = self.IndexEntry()
            index_entry.IndexID = i
            index_entry.Offset = offset + self.headerSize
            index_entry.Size = size
            index_entry.ClassID = classid
            index_entry.Offset_ptr = t_pos

            br.Seek(offset + self.headerSize, 0)
            
            fname = ""
            if (index_entry.Size > 4):
                fname_length = br.ReadInt32()
                if (0 < fname_length < 0x20):
                    fname = self._fixAsciiName(br.ReadBytes(fname_length))
            ext_name = ".bin"
            if (index_entry.ClassID in self.ClassIDDict):
                ext_name = self.ClassIDDict[index_entry.ClassID][1]
            index_entry.ObjectName = fname + ext_name
            # print("Entry %d %s :%08x,%08x,Class ID :%08x"%(index_entry.IndexID, index_entry.ObjectName,index_entry.Offset,index_entry.Size ,classid))
            self.EntryList.append(index_entry)

        pass

    def _checkVersion(self, version_string):
        (a, b, c) = version_string.split(".")[:3]
        self.packageMajorVersion = int(a)
        self.packageMinorVersion = int(b)
        self.packagePatchVersion = c
        pass

    def _fixAsciiName(self, name):
        result = ""
        for var in name:
            if 0x20 <= ord(var) <= 0x7e:
                result += var
                pass
            else:
                return ""
        return result

    # 解包到目录

    def Unpack(self, dst_folder):
        print("Unpacking Assets...")
        br = BinaryHelper.BinaryReader(self.baseStream)
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)

        for entry in self.EntryList:
            br.Seek(entry.Offset)
            data = br.ReadBytes(entry.Size)
            with open("%s/%08d_%s" % (dst_folder,
                                      entry.IndexID,
                                      entry.ObjectName), "wb") as dst:
                dst.write(data)
        self.baseStream.close()
        print("Assets Unpacked")
        pass

    # 从文件夹打包到assets

    def Pack(self, input_folder):
        print("Packing Assets...")
        br = BinaryHelper.BinaryReader(self.baseStream)
        br.Seek(self.ObjectsEntryOffset, 0)

        # 检查所有文件是否存在
        for entry in self.EntryList:
            name = "%s/%08d_%s" % (input_folder,
                                   entry.IndexID,
                                   entry.ObjectName)
            if not os.path.exists(name):
                print("Error: asset not found:%s" % name)
                return False

        self.baseStream.truncate()

        for i in xrange(len(self.EntryList)):
            entry = self.EntryList[i]
            name = "%s/%08d_%s" % (input_folder,
                                   entry.IndexID,
                                   entry.ObjectName)
            fs = open(name, "rb")
            data = fs.read()
            length = len(data)
            pos = self.baseStream.tell()
            if pos % 8 != 0:
                self.baseStream.write("\x00" * (8 - pos))
                pos = self.baseStream.tell()

            self.baseStream.write(data)
            # 更新entry
            entry.Offset = pos
            entry.Size = length
            self.EntryList[i] = entry

        self.baseStream.seek(0, 2)
        total_size = self.baseStream.tell()

        for i in xrange(len(self.EntryList)):
            entry = self.EntryList[i]
            self.baseStream.seek(entry.Offset_ptr)
            self.baseStream.write(struct.pack(
                "I", entry.Offset - self.headerSize))
            self.baseStream.write(struct.pack("I", entry.Size))
        self.baseStream.seek(4, 0)
        self.baseStream.write(struct.pack("I", total_size))
        self.baseStream.close()
        pass

    def Close(self):
        if self.baseStream is not None:
            self.baseStream.close()

    class IndexEntry:
        Offset_ptr = 0
        Offset = 0
        Size = 0
        IndexID = 0
        ClassID = 0
        ObjectName = ""


def test():
    loader = AssetsLoader("sharedassets0.assets")
    loader.Unpack("sharedassets0.assets_unpacked")
