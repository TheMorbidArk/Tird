import json
import os
import git
from prettytable import PrettyTable

# Data Buffer
"""
存储Tiderip解释器源码信息
- $src Path
- Exten Packages Path
"""
TideripPath = '../Tiderip/'
ExternPackagesPath = TideripPath + 'Extension/'


class Progress(git.remote.RemoteProgress):
    def __init__(self):
        super().__init__()

    def update(self, op_code, cur_count, max_count=None, message=''):
        if len(message) != 0:
            print(op_code, cur_count, max_count, message)
        print(self._cur_line)


def InstallPackages(packageName):
    # Install Packages

    # 获取Packages Message

    # TODO 测试期间注释
    # fileNames = os.listdir(ExternPackagesPath)
    # fileNames.remove('exten.Bind.inc')
    # fileNames.remove('exten.script.inc')
    # fileNames.remove('extenHeader.h')
    # for i in fileNames:
    #     if i == packageName:
    #         print('\033[1;31m-[ERROR] The Package is already installed\033[0m')
    #         return 0

    # # 获取 Package Message
    path = 'remotePackages.json'
    Packages = {}
    with open(path) as PackageData:
        Packages = json.load(PackageData)
    # # Package Names
    PackageMsg = []
    for Name in Packages['Packages']:
        if Name == packageName:
            PackageMsg = Packages['Packages'][Name]
    del PackageData, Packages, Name, path
    packageHost = PackageMsg.pop()
    del PackageMsg

    '''
    Clone 扩展库
    '''
    # Get packageHost
    print(packageHost)
    # TODO to_path='new/' 需要更正为 ExternPackagesPath
    repo = git.Repo.clone_from(
        url=packageHost, to_path='new/', progress=Progress())

    '''
    修改CMakeList.txt
    '''
    
    '''
    重新编译Tiderip
    '''


InstallPackages('Regex')


def printPackageMsg(mode):
    """
    输出本地/远程扩展包列表
    mode: 输出选项 local/remote
    """
    # 生成 Packages 相关 Messages
    path = ''
    if mode == 'local':
        path = 'localPackages.json'
        print('-[Local] Packages Message')
    elif mode == 'remote':
        path = 'remotePackages.json'
        print('-[Remote] Packages Message')

    # # Json Buffer
    Packages = {}
    with open(path) as PackageData:
        Packages = json.load(PackageData)

    # # Package Names
    PackageNames = []
    for Name in Packages['Packages']:
        PackageNames.append(Name)

    # # Package Messages
    PackageMsg = Packages['Packages']

    # # Package Table 输出
    table = PrettyTable(['No', 'ID', 'Name', 'Version', 'Host'])
    for key in PackageMsg:
        table.add_row(PackageMsg[key])
    print(table)


# 生成 Remote Packages 相关 Messages
# TODO 从远端获取 <Packages Json> 数据
Remotepackages = {}  # Json数据
RemotepackageNames = []  # Package Name
RemotepackageIDs = []  # Package Name
RemotepackageVersions = []  # Package Version
RemotepackageHosts = []  # Package Host


# 阻塞式调用
# os.system("htop")
# print(123)
