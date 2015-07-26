# encoding: UTF-8
import re, os, zipfile
'''
svn更新文件查找
从java文件找出class文件
'''

# 读取文件名列表
def getFilesList():
    # 读取file.txt中文件名称列表
    files = []
    with open(fpath,"r") as f:
        for line in f.readlines():
            if line.strip() != "":
                files.append(line.strip())
    s = set(files)
    return list(s)

# java文件后辍转换成class
def javaToClass(filesList):
    return list(map(lambda fileName : re.sub(".java$", ".class", fileName), filesList))

# 搜索文件目录列表
def findFilePaths(fl):
    _path = {}
    for root, dirs, files in os.walk(webappPath):
        for file in files:
            if file in fl:
                path = os.path.join(root, file).strip()
                l = []
                if file in _path:
                    l = _path.get(file)
                l.append(path)
                _path[file] = l
    return _path

# 去除文件名重复文件
def clearSameNameFile(paths):
    pathList = []
    for k,v in paths.items():
        if len(v) > 1:
            print("以下文件文件名重复，请选择相应序号文件\n不选择默认复制所有文件，多个文件可用逗号分隔")
            for i,p in enumerate(v):
                print("【" + str(i) + "】 : " + p)
            index = input("请输入需要复制的文件编号：")
            # 如果未输入，则copy所有文件，否则按输入序号选择文件，多个文件可用,分隔选择
            if len(index) == 0:
                for m in v:
                    pathList.append(m)
            else:
                _indexs = re.split(",|，", index)
                for j in _indexs:
                    pathList.append(v[int(j)])
        else:
            pathList.append(v[0])
    return pathList

# 打包
def zipFiles(pathList):
    filePath = os.path.split(zipPath)[0]
    if not os.path.exists(filePath):
            os.makedirs(filePath)
    zf = zipfile.ZipFile(zipPath, "w", zipfile.zlib.DEFLATED)
    print("正在打包....")
    for tar in pathList:
        print(tar)
        arcname = "webapp\\" + tar[len(webappPath):]
        zf.write(tar, arcname)
    zf.close()

webappPath = input("输入项目webapp路径: ")
issusNo = input("请输入打包文件名（问题编号）：")

# webappPath = "E:\\jbdevstudio\\runtimes\\jboss-eap\\standalone\\deployments\\xzsp.war"
fpath = "file.txt"
zipPath = "updateFile\\" + issusNo + ".zip"

javaList = javaToClass(getFilesList())
allFilePaths = findFilePaths(javaList)
filePaths = clearSameNameFile(allFilePaths)
zipFiles(filePaths)
print("打包完成！共 " + str(len(filePaths)) + " 个文件")
input("Press <enter>")
