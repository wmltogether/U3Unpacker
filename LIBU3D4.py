# -*- coding: utf-8 -*-
'''
ver 1128
>增加了非法文件名判断
ver 1103
>增加了版本号地址判断
ver 0827
>修改了textassets的扩展名
ver 0815
>目前仅支持unity 4.x assets格式
>依然兼容旧版unity打包脚本
>添加了文件格式的简单判断，目前支持最基础的图片音频纯文本类型支持，判断规则详见
http://docs.unity3d.com/Documentation/Manual/ClassIDReference.html
>添加文件名unicode判断，使用异常判断来忽略非ascii文件名
>封包会自动过滤文件夹中的png格式
>split文件数量计算函数
>提供了OBB文件md5校验计算:getObbMD5

'''
import os,codecs
from struct import unpack,pack
import md5
def dir_fn(folder):
    dirlst=[]
    for root,dirs,files in os.walk(folder):
        for name in files:
            adrlist=os.path.join(root, name)
            dirlst.append(adrlist)
    return dirlst
def getsize(fn):
    fsize=os.path.getsize(fn)
    return fsize
def getSplitNUMS(fn):
    if not os.path.exists('assets/'):
        os.makedirs('assets/') 
    f=open('assets//%s'%fn,'rb')
    f.seek(4)
    fsize=unpack('>I',f.read(4))[0]
    if fsize%(0x00100000)==0:
        nums=fsize/(0x00100000)
    else:
        nums=fsize/(0x00100000)+1
    f.close()
    return nums
def getObbMD5(obbname):
    fp=open(obbname,'rb')
    fp.seek(-0x10016,2)
    string=fp.read(0x10016)
    m = md5.new()
    m.update(string)
    fp.close()
    return m.hexdigest()
def del_png(fl):
    new_fl=[]
    for a in fl:
        if a[-4:].lower() not in ['.png' , '.exe']:
            new_fl.append(a)
            
    return new_fl
def getClassDict():
    # Based on http://docs.unity3d.com/Documentation/Manual/ClassIDReference.html
    ClassDict={}
def getClassDict():
    # Based on http://docs.unity3d.com/Documentation/Manual/ClassIDReference.html
    ClassDict={}
    ClassDict[1] = ('GameObject' , '.gobj')
    ClassDict[2] = ('Component' , '.cpt')
    ClassDict[3] = ('LevelGameManager' , '.lgm')
    ClassDict[4] = ('Transform' , '.tfm')
    ClassDict[5] = ('TimeManager' , '.tmg')
    ClassDict[8] = ('Behaviour' , '.bhv')
    ClassDict[9] = ('GameManager' , '.gmr')
    ClassDict[11] = ('AudioManager' , '.amr')
    ClassDict[12] = ('ParticleAnimator' , '.ParticleAnimator')
    ClassDict[13] = ('InputManager' , '.InputManager')
    ClassDict[15] = ('EllipsoidParticleEmitter' , '.EllipsoidParticleEmitter')
    ClassDict[17] = ('Pipeline' , '.Pipeline')
    ClassDict[18] = ('EditorExtension' , '.EditorExtension')
    ClassDict[19] = ('Physics2DSettings' , '.Physics2DSettings')
    ClassDict[20] = ('Camera' , '.Camera')
    ClassDict[21] = ('Material' , '.material')
    ClassDict[27]=('Texture','.tex')# texture
    ClassDict[28]=('Texture2D','.tex')# texture2d
    ClassDict[29] = ('SceneSettings' , '.SceneSettings')
    ClassDict[30] = ('GraphicsSettings' , '.GraphicsSettings')
    ClassDict[33] = ('MeshFilter' , '.MeshFilter')
    ClassDict[41] = ('OcclusionPortal' , '.OcclusionPortal')
    ClassDict[43]=('Mesh','.mesh')
    ClassDict[45] = ('Skybox' , '.Skybox')
    ClassDict[47] = ('QualitySettings' , '.QualitySettings')
    ClassDict[48]=('Shader', '.shader')
    ClassDict[49]=('TextAsset','.textassets')#All text assets have classe id 49
    ClassDict[50] = ('Rigidbody2D' , '.Rigidbody2D')
    ClassDict[51] = ('Physics2DManager' , '.Physics2DManager')
    ClassDict[53] = ('Collider2D' , '.Collider2D')
    ClassDict[54] = ('Rigidbody' , '.Rigidbody')
    ClassDict[55] = ('PhysicsManager' , '.PhysicsManager')
    ClassDict[56] = ('Collider' , '.Collider')
    ClassDict[57] = ('Joint' , '.Joint')
    ClassDict[58] = ('CircleCollider2D' , '.CircleCollider2D')
    ClassDict[59] = ('HingeJoint' , '.HingeJoint')
    ClassDict[60] = ('PolygonCollider2D' , '.PolygonCollider2D')
    ClassDict[61] = ('BoxCollider2D' , '.BoxCollider2D')
    ClassDict[62] = ('PhysicsMaterial2D' , '.PhysicsMaterial2D')
    ClassDict[64] = ('MeshCollider' , '.MeshCollider')
    ClassDict[65] = ('BoxCollider' , '.BoxCollider')
    ClassDict[66] = ('SpriteCollider2D' , '.SpriteCollider2D')
    ClassDict[68] = ('EdgeCollider2D' , '.EdgeCollider2D')
    ClassDict[72] = ('ComputeShader' , '.ComputeShader')
    ClassDict[74] = ('AnimationClip' , '.AnimationClip')
    ClassDict[75] = ('ConstantForce' , '.ConstantForce')
    ClassDict[76] = ('WorldParticleCollider' , '.WorldParticleCollider')
    ClassDict[78] = ('TagManager' , '.TagManager')
    ClassDict[81] = ('AudioListener' , '.AudioListener')
    ClassDict[82] = ('AudioSource' , '.AudioSource')
    ClassDict[83]=('AudioClip','.wav')
    ClassDict[84]=('RenderTexture','.tex')
    ClassDict[87] = ('MeshParticleEmitter' , '.MeshParticleEmitter')
    ClassDict[88] = ('ParticleEmitter' , '.ParticleEmitter')
    ClassDict[89] = ('Cubemap' , '.Cubemap')
    ClassDict[90] = ('Avatar' , '.Avatar')
    ClassDict[91] = ('AnimatorController' , '.AnimatorController')
    ClassDict[92] = ('GUILayer' , '.GUILayer')
    ClassDict[93] = ('RuntimeAnimatorController' , '.RuntimeAnimatorController')
    ClassDict[94] = ('ScriptMapper' , '.ScriptMapper')
    ClassDict[95] = ('Animator' , '.Animator')
    ClassDict[96] = ('TrailRenderer' , '.TrailRenderer')
    ClassDict[98] = ('DelayedCallManager' , '.DelayedCallManager')
    ClassDict[102]=('TextMesh','.TextMesh')# textmesh
    ClassDict[104] = ('RenderSettings' , '.RenderSettings')
    ClassDict[108] = ('Light' , '.Light')
    ClassDict[109] = ('CGProgram' , '.CGProgram')
    ClassDict[110] = ('BaseAnimationTrack' , '.BaseAnimationTrack')
    ClassDict[111] = ('Animation' , '.Animation')
    #Classes defined from scripts
    #will always have class ID 114,
    #such as NGUI font
    ClassDict[114]=('MonoBehaviour','.mb')
    ClassDict[115]=('MonoScript','.mscr')
    ClassDict[116] = ('MonoManager' , '.MonoManager')
    ClassDict[117] = ('Texture3D' , '.Texture3D')
    ClassDict[118] = ('NewAnimationTrack' , '.NewAnimationTrack')
    ClassDict[119] = ('Projector' , '.Projector')
    ClassDict[120] = ('LineRenderer' , '.LineRenderer')
    ClassDict[121] = ('Flare' , '.Flare')
    ClassDict[122] = ('Halo' , '.Halo')
    ClassDict[123] = ('LensFlare' , '.LensFlare')
    ClassDict[124] = ('FlareLayer' , '.FlareLayer')
    ClassDict[125] = ('HaloLayer' , '.HaloLayer')
    ClassDict[126] = ('NavMeshAreas' , '.NavMeshAreas')
    ClassDict[127] = ('HaloManager' , '.HaloManager')
    ClassDict[128]=('Font','.font')#GUIText Font /Dynamic font(True Type Font)
    ClassDict[129] = ('PlayerSettings' , '.PlayerSettings')
    ClassDict[130]=('NamedObject','.nobj')
    ClassDict[131]=('GUITexture','.tex')
    ClassDict[132]=('GUIText','.guitext')
    ClassDict[133] = ('GUIElement' , '.GUIElement')
    ClassDict[134] = ('PhysicMaterial' , '.PhysicMaterial')
    ClassDict[135] = ('SphereCollider' , '.SphereCollider')
    ClassDict[136] = ('CapsuleCollider' , '.CapsuleCollider')
    ClassDict[137] = ('SkinnedMeshRenderer' , '.SkinnedMeshRenderer')
    ClassDict[138] = ('FixedJoint' , '.FixedJoint')
    ClassDict[140] = ('RaycastCollider' , '.RaycastCollider')
    ClassDict[141] = ('BuildSettings' , '.BuildSettings')
    ClassDict[142] = ('AssetBundle' , '.AssetBundle')
    ClassDict[143] = ('CharacterController' , '.CharacterController')
    ClassDict[144] = ('CharacterJoint' , '.CharacterJoint')
    ClassDict[145] = ('SpringJoint' , '.SpringJoint')
    ClassDict[146] = ('WheelCollider' , '.WheelCollider')
    ClassDict[147] = ('ResourceManager' , '.ResourceManager')
    ClassDict[148] = ('NetworkView' , '.NetworkView')
    ClassDict[149] = ('NetworkManager' , '.NetworkManager')
    ClassDict[150] = ('PreloadData' , '.PreloadData')
    ClassDict[152] = ('MovieTexture' , '.MovieTexture')
    ClassDict[153] = ('ConfigurableJoint' , '.ConfigurableJoint')
    ClassDict[154] = ('TerrainCollider' , '.TerrainCollider')
    ClassDict[155] = ('MasterServerInterface' , '.MasterServerInterface')
    ClassDict[156] = ('TerrainData' , '.TerrainData')
    ClassDict[157] = ('LightmapSettings' , '.LightmapSettings')
    ClassDict[158] = ('WebCamTexture' , '.WebCamTexture')
    ClassDict[159] = ('EditorSettings' , '.EditorSettings')
    ClassDict[160] = ('InteractiveCloth' , '.InteractiveCloth')
    ClassDict[161] = ('ClothRenderer' , '.ClothRenderer')
    ClassDict[162] = ('EditorUserSettings' , '.EditorUserSettings')
    ClassDict[163] = ('SkinnedCloth' , '.SkinnedCloth')
    ClassDict[164] = ('AudioReverbFilter' , '.AudioReverbFilter')
    ClassDict[165] = ('AudioHighPassFilter' , '.AudioHighPassFilter')
    ClassDict[166] = ('AudioChorusFilter' , '.AudioChorusFilter')
    ClassDict[167] = ('AudioReverbZone' , '.AudioReverbZone')
    ClassDict[168] = ('AudioEchoFilter' , '.AudioEchoFilter')
    ClassDict[169] = ('AudioLowPassFilter' , '.AudioLowPassFilter')
    ClassDict[170] = ('AudioDistortionFilter' , '.AudioDistortionFilter')
    ClassDict[171] = ('SparseTexture' , '.SparseTexture')
    ClassDict[180] = ('AudioBehaviour' , '.AudioBehaviour')
    ClassDict[181] = ('AudioFilter' , '.AudioFilter')
    ClassDict[182] = ('WindZone' , '.WindZone')
    ClassDict[183] = ('Cloth' , '.Cloth')
    ClassDict[184] = ('SubstanceArchive' , '.SubstanceArchive')
    ClassDict[185] = ('ProceduralMaterial' , '.ProceduralMaterial')
    ClassDict[186] = ('ProceduralTexture' , '.ProceduralTexture')
    ClassDict[191] = ('OffMeshLink' , '.OffMeshLink')
    ClassDict[192] = ('OcclusionArea' , '.OcclusionArea')
    ClassDict[193] = ('Tree' , '.Tree')
    ClassDict[194] = ('NavMeshObsolete' , '.NavMeshObsolete')
    ClassDict[195] = ('NavMeshAgent' , '.NavMeshAgent')
    ClassDict[196] = ('NavMeshSettings' , '.NavMeshSettings')
    ClassDict[197] = ('LightProbesLegacy' , '.LightProbesLegacy')
    ClassDict[198] = ('ParticleSystem' , '.ParticleSystem')
    ClassDict[199] = ('ParticleSystemRenderer' , '.ParticleSystemRenderer')
    ClassDict[200] = ('ShaderVariantCollection' , '.ShaderVariantCollection')
    ClassDict[205] = ('LODGroup' , '.LODGroup')
    ClassDict[206] = ('BlendTree' , '.BlendTree')
    ClassDict[207] = ('Motion' , '.Motion')
    ClassDict[208] = ('NavMeshObstacle' , '.NavMeshObstacle')
    ClassDict[210] = ('TerrainInstance' , '.TerrainInstance')
    ClassDict[212] = ('SpriteRenderer' , '.SpriteRenderer')
    ClassDict[213]=('Sprite','.tmsk')
    ClassDict[214] = ('CachedSpriteAtlas' , '.CachedSpriteAtlas')
    ClassDict[215] = ('ReflectionProbe' , '.ReflectionProbe')
    ClassDict[216] = ('ReflectionProbes' , '.ReflectionProbes')
    ClassDict[220] = ('LightProbeGroup' , '.LightProbeGroup')
    ClassDict[221] = ('AnimatorOverrideController' , '.AnimatorOverrideController')
    ClassDict[222] = ('CanvasRenderer' , '.CanvasRenderer')
    ClassDict[223] = ('Canvas' , '.Canvas')
    ClassDict[224] = ('RectTransform' , '.RectTransform')
    ClassDict[225] = ('CanvasGroup' , '.CanvasGroup')
    ClassDict[226] = ('BillboardAsset' , '.BillboardAsset')
    ClassDict[227] = ('BillboardRenderer' , '.BillboardRenderer')
    ClassDict[228] = ('SpeedTreeWindAsset' , '.SpeedTreeWindAsset')
    ClassDict[229] = ('AnchoredJoint2D' , '.AnchoredJoint2D')
    ClassDict[230] = ('Joint2D' , '.Joint2D')
    ClassDict[231] = ('SpringJoint2D' , '.SpringJoint2D')
    ClassDict[232] = ('DistanceJoint2D' , '.DistanceJoint2D')
    ClassDict[233] = ('HingeJoint2D' , '.HingeJoint2D')
    ClassDict[234] = ('SliderJoint2D' , '.SliderJoint2D')
    ClassDict[235] = ('WheelJoint2D' , '.WheelJoint2D')
    ClassDict[238] = ('NavMeshData' , '.NavMeshData')
    ClassDict[240] = ('AudioMixer' , '.AudioMixer')
    ClassDict[241] = ('AudioMixerController' , '.AudioMixerController')
    ClassDict[243] = ('AudioMixerGroupController' , '.AudioMixerGroupController')
    ClassDict[244] = ('AudioMixerEffectController' , '.AudioMixerEffectController')
    ClassDict[245] = ('AudioMixerSnapshotController' , '.AudioMixerSnapshotController')
    ClassDict[246] = ('PhysicsUpdateBehaviour2D' , '.PhysicsUpdateBehaviour2D')
    ClassDict[247] = ('ConstantForce2D' , '.ConstantForce2D')
    ClassDict[248] = ('Effector2D' , '.Effector2D')
    ClassDict[249] = ('AreaEffector2D' , '.AreaEffector2D')
    ClassDict[250] = ('PointEffector2D' , '.PointEffector2D')
    ClassDict[251] = ('PlatformEffector2D' , '.PlatformEffector2D')
    ClassDict[252] = ('SurfaceEffector2D' , '.SurfaceEffector2D')
    ClassDict[258] = ('LightProbes' , '.LightProbes')
    ClassDict[271] = ('SampleClip' , '.SampleClip')
    ClassDict[272] = ('AudioMixerSnapshot' , '.AudioMixerSnapshot')
    ClassDict[273] = ('AudioMixerGroup' , '.AudioMixerGroup')
    ClassDict[290] = ('AssetBundleManifest' , '.AssetBundleManifest')
    ClassDict[1001]=('Prefab','.prefab')
    ClassDict[1002] = ('EditorExtensionImpl' , '.EditorExtensionImpl')
    ClassDict[1003] = ('AssetImporter' , '.AssetImporter')
    ClassDict[1004] = ('AssetDatabase' , '.AssetDatabase')
    ClassDict[1005] = ('Mesh3DSImporter' , '.Mesh3DSImporter')
    ClassDict[1006] = ('TextureImporter' , '.TextureImporter')
    ClassDict[1007] = ('ShaderImporter' , '.ShaderImporter')
    ClassDict[1008] = ('ComputeShaderImporter' , '.ComputeShaderImporter')
    ClassDict[1011] = ('AvatarMask' , '.AvatarMask')
    ClassDict[1020] = ('AudioImporter' , '.AudioImporter')
    ClassDict[1026] = ('HierarchyState' , '.HierarchyState')
    ClassDict[1027] = ('GUIDSerializer' , '.GUIDSerializer')
    ClassDict[1028] = ('AssetMetaData' , '.AssetMetaData')
    ClassDict[1029] = ('DefaultAsset' , '.DefaultAsset')
    ClassDict[1030] = ('DefaultImporter' , '.DefaultImporter')
    ClassDict[1031] = ('TextScriptImporter' , '.TextScriptImporter')
    ClassDict[1032] = ('SceneAsset' , '.SceneAsset')
    ClassDict[1034] = ('NativeFormatImporter' , '.NativeFormatImporter')
    ClassDict[1035] = ('MonoImporter' , '.MonoImporter')
    ClassDict[1037] = ('AssetServerCache' , '.AssetServerCache')
    ClassDict[1038] = ('LibraryAssetImporter' , '.LibraryAssetImporter')
    ClassDict[1040] = ('ModelImporter' , '.ModelImporter')
    ClassDict[1041] = ('FBXImporter' , '.FBXImporter')
    ClassDict[1042] = ('TrueTypeFontImporter' , '.TrueTypeFontImporter')
    ClassDict[1044] = ('MovieImporter' , '.MovieImporter')
    ClassDict[1045] = ('EditorBuildSettings' , '.EditorBuildSettings')
    ClassDict[1046] = ('DDSImporter' , '.DDSImporter')
    ClassDict[1048] = ('InspectorExpandedState' , '.InspectorExpandedState')
    ClassDict[1049] = ('AnnotationManager' , '.AnnotationManager')
    ClassDict[1050] = ('PluginImporter' , '.PluginImporter')
    ClassDict[1051] = ('EditorUserBuildSettings' , '.EditorUserBuildSettings')
    ClassDict[1052] = ('PVRImporter' , '.PVRImporter')
    ClassDict[1053] = ('ASTCImporter' , '.ASTCImporter')
    ClassDict[1054] = ('KTXImporter' , '.KTXImporter')
    ClassDict[1101] = ('AnimatorStateTransition' , '.AnimatorStateTransition')
    ClassDict[1102] = ('AnimatorState' , '.AnimatorState')
    ClassDict[1105] = ('HumanTemplate' , '.HumanTemplate')
    ClassDict[1107] = ('AnimatorStateMachine' , '.AnimatorStateMachine')
    ClassDict[1108] = ('PreviewAssetType' , '.PreviewAssetType')
    ClassDict[1109] = ('AnimatorTransition' , '.AnimatorTransition')
    ClassDict[1110] = ('SpeedTreeImporter' , '.SpeedTreeImporter')
    ClassDict[1111] = ('AnimatorTransitionBase' , '.AnimatorTransitionBase')
    ClassDict[1112] = ('SubstanceImporter' , '.SubstanceImporter')
    ClassDict[1113] = ('LightmapParameters' , '.LightmapParameters')
    ClassDict[1120] = ('LightmapSnapshot' , '.LightmapSnapshot')
    ClassDict[-14]=('NGUI Plugin Text Type','.ngt')
    return ClassDict
def MatchClassID(classid,filename_mark):
    ClassDict=getClassDict()
    if classid in ClassDict:
        (FileType,extname) = ClassDict[classid]
        return (FileType,extname)
    elif filename_mark == True:
        (FileType,extname) = ('Unknown','')
    else:
        (FileType,extname) = ('Unknown','.bin')
    return (FileType,extname)
def fix_ascii_name(name):
    if ':' in name:
        return ''
    if "\\" in name:
        return ''
    if "//" in name:
        return ''
    if "|" in name:
        return ''
    if "?" in name:
        return '' 
    if "<" in name:
        return '' 
    if ">" in name:
        return '' 
    try:
        binname=name.encode('ascii')
        return name
    except:
        return ''
def unpack_assets(fn):
    if not os.path.exists('assets/'):
        os.makedirs('assets/')    
    dn = os.path.splitext(fn)[0]
    fn = 'assets/'+fn
    if os.path.isdir('assets/%s'%dn):
        print('%s id dir,pass'%dn)
        return None
    if not os.path.exists('assets/%s_unpacked/'%dn):
        os.makedirs('assets/%s_unpacked/'%dn)
    fp = open(fn,'rb')
    fp.seek(0xc)
    head_size = unpack('>I',fp.read(4))[0]
    fp.seek(0x14)
    pos = len(fp.read(10).split('\x00')[0]) - 7
    fp.seek(0x28+pos)
    num = unpack('I',fp.read(4))[0]
    print('Unpacking:%s File Nums:%d'%(fn,num))
    for i in range(num):
        fp.seek(0x30+i*0x14+pos)
        tmp_ofs=fp.tell()
        (offset,size)=unpack('2I',fp.read(8))
        (classid0,classid,index_id)=unpack('3I',fp.read(0xc))# get classid and index id
        offset+=head_size
        fp.seek(offset,0)
        dat=fp.read(size)
        if size>=4:
            filename_length = unpack('I',dat[:4])[0]
            
            if filename_length != 0:
                filename_mark=True
                try:
                    name = dat[4:filename_length+4].decode('utf8').replace(' ','_')
                    name=fix_ascii_name(name)
                    (FileType,extname)=MatchClassID(classid,filename_mark)
                    final_name='%08d_%s%s'%(i,name,extname)
                    if not '\x00' in final_name:
                        dest = open('assets/%s_unpacked/%s'%(dn,final_name),'wb')
                    else:
                        final_name='%08d%s'%(i, '.bin')
                        dest = open('assets/%s_unpacked/%s'%(dn,final_name),'wb')
                except:
                    filename_mark=False
                    (FileType,extname)=MatchClassID(classid,filename_mark)
                    final_name='%08d%s'%(i,extname)
                    dest = open('assets/%s_unpacked/%s'%(dn,final_name),'wb')
                
            else:
                filename_mark=False
                (FileType,extname)=MatchClassID(classid,filename_mark)
                final_name='%08d%s'%(i,extname)
                dest = open('assets/%s_unpacked/%s'%(dn,final_name),'wb')
        else:
            final_name='%08d.bin'%(i)
            dest = open('assets/%s_unpacked/%s'%(dn,final_name),'wb')
        #print('%08x|%s'%(tmp_ofs,final_name))
        dest.write(dat)
        dest.close()
    fp.close()
def pack_assets(fn):
    dn = os.path.splitext(fn)[0]
    if not os.path.isdir('assets/%s_unpacked'%dn):
        return None
    if '_unpacked' in dn:
        return None
    fn = 'assets/'+fn

    fp = open(fn,'rb+')
    print('Packing %s'%fn)
    fp.seek(0xc)
    head_size = unpack('>I',fp.read(4))[0]
    fp.seek(0x14)
    pos = len(fp.read(10).split('\x00')[0]) - 7
    fp.seek(0x28+pos)
    num = unpack('I',fp.read(4))[0]

    fp.seek(head_size)
    ol = []
    sl = []
    fl = dir_fn('assets/%s_unpacked'%dn)
    fl=del_png(fl)
    if len(fl) != num:
        print('An error occured while reading %s\n'%(dn)+\
              ' files in assets:%d|\n files in folder:%d'%(num,len(fl)))
        fp.close()
        return None
    for fn in fl:
        if fp.tell()%8 != 0:
            fp.seek((fp.tell()/8+1)*8)
        sl.append(getsize(fn))
        ol.append(fp.tell()-head_size)
        dat = open(fn,'rb').read()
        fp.write(dat)
    fp.seek(0,2)

    total_size = fp.tell()

    for i in range(num):
        fp.seek(0x30+i*0x14+pos)
        fp.write(pack('I',ol[i]))
        fp.write(pack('I',sl[i]))

    fp.seek(4)
    fp.write(pack('>I',total_size))
    fp.close()
    
     
