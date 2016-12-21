# Unity3D-Assets-Unpacker
Unity3D Assets Unpacker

''' Created on 2015-8-11 @author: wmltogether '''

说明：在Unity 5.5+中已经没有Class ID reference这个结构了，所以无法简单识别文件类型，对于纹理格式，纹理数据也被转移到了resS中进行保存。

'''

ver 20161216

>修复unity5.5索引对齐导致解包失败的问题

ver 20161216

>重构版本，增加unity5.5支持

ver 20150811

>修正U3D版本判断

ver 20150727

>增加Debug output

>增加Classid判断

ver 20150414

>增加Unity 版本判断机制

ver 20150323

>添加Unity 5支援

>移除Unity 4支援

ver 20150127

>增加了Texture Sprite扩展名(tmsk)

ver 20141128

>增加了非法文件名判断

ver 20141103

>增加了版本号地址判断

ver 20140827

>修改了textassets的扩展名

ver 20140815

>目前仅支持unity 4.x assets格式

>依然兼容旧版unity打包脚本

>添加了文件格式的简单判断，目前支持最基础的图片音频纯文本类型支持，判断规则详见

http://docs.unity3d.com/Documentation/Manual/ClassIDReference.html

>添加文件名unicode判断，使用异常判断来忽略非ascii文件名

>封包会自动过滤文件夹中的png格式

>split文件数量计算函数

>提供了OBB文件md5校验计算:getObbMD5



'''
