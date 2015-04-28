
#Filename : packages.py
# -*- coding: UTF-8 -*- 
import os
import time
import sys
import shutil
import platform
copyFileCounts = 0
class magentoZip:
    def __init__(self, target_dir, plusDir, plusName, modelName , newZipName ,type):
        global opsystem
        self.source     = None
        self.target_dir             = target_dir
        self.plusDir = plusDir
        self.plusName = plusName[0].upper() + plusName[1:]
        self.modelName = modelName[0].upper() + modelName[1:]
        self.newZipName = newZipName
        self.type = type
        target = target_dir + newZipName
        if os.path.isfile(target):
            os.remove(target)
    def exeZipFile(self):
        #source = [r'D:\Users\array.h', r'D:\Users\arrayrc.h', r'D:\Users\test_for_poly.cpp', r'D:\Users\test.cpp']
#        source = self.source
        target_dir = self.target_dir
        sourceDir = target_dir + self.newZipName
        print sourceDir
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        #filename = time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.zip'
        filename = self.newZipName + '.zip'
#        for i in source:
#            print 'dir = ', i
        target = target_dir + filename
        if os.path.isfile(target):
            os.remove(target)
        #ep1           从名称中排除基本目录
        zip_command = "rar a -r -ep1 %s %s " % (target, sourceDir + '\*')
 
        print zip_command
 
        if os.system(zip_command) == 0:
            print 'Successful backup to', target
        else :
            print os.system(zip_command)
            print 'backup FAILED'
    def tarZipFile(self):
        target_dir = self.target_dir
        sourceDir = self.newZipName
        print sourceDir
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        #filename = time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.zip'
        filename = self.newZipName + '.tar'
#        for i in source:
#            print 'dir = ', i
        #target = target_dir + filename
        if os.path.isfile(filename):
            os.remove(filename)
 
        os.system ("tar -cvf %s %s" % (filename, sourceDir))
 
        if os.path.isfile (filename):
            print 'Successful backup to', filename
        else :
            print 'backup FAILED'
 
    def makeDirLinux(self):
        print self.modelName 
 
        # os._exit()
        if(self.type == '1'):
            communityLocal = 'community/'
        elif(self.type == '2'):
            communityLocal = 'local/'
        else:
            raise Exception("no select type !")
            os._exit('no select type')
        sourceDir = self.plusDir + "/app/code/" + communityLocal + self.plusName + '/' + self.modelName
        target_dir = self.target_dir + self.newZipName
        print sourceDir
        print opsystem
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
        if os.path.isdir(sourceDir):
            #creatDirs(target_dir, 'app', 2, self.plusName, self.modelName)
            targetDir = target_dir + "/app/code/" + communityLocal + self.plusName + '/' + self.modelName
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFiles(sourceDir, targetDir)
            #Modules
            etcSourceFile = self.plusDir + "/app/etc/modules/" + self.plusName + '_' +self.modelName +'.xml'
            etcTargetDir = target_dir + "/app/etc/modules/"
            copyFile(etcSourceFile,etcTargetDir)
 
            #adminhtml layout
            adminLayoutSourceFile = self.plusDir + "/app/design/adminhtml/default/default/layout/" + self.plusName.lower() + '_' + self.modelName[0].lower() + self.modelName[1:] +'.xml'
            adminLayoutTargetDir = target_dir + '/app/design/adminhtml/default/default/layout/'
 
            copyFile(adminLayoutSourceFile,adminLayoutTargetDir)
 
            #adminhtml local en_US
            adminLocalSourceFile = self.plusDir + '/app/design/adminhtml/default/default/locale/en_US/' + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            adminLocalTargetDir = target_dir + '/app/design/adminhtml/default/default/locale/en_US/'
            copyFile(adminLocalSourceFile,adminLocalTargetDir)
 
            #adminhtml template
            adminTplSourceDir = self.plusDir + '/app/design/adminhtml/default/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            adminTplTargetDir = target_dir + '/app/design/adminhtml/default/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(adminTplSourceDir, adminTplTargetDir)
 
            #frontend base default layout
            frontBaseLayoutSourceFile = self.plusDir + "/app/design/frontend/base/default/layout/" + self.plusName.lower() + '_' + self.modelName[0].lower() + self.modelName[1:] +'.xml'
            frontBaseLayoutTargetFile = target_dir + "/app/design/frontend/base/default/layout/"
            copyFile(frontBaseLayoutSourceFile,frontBaseLayoutTargetFile)
 
            #frontend base default template
            frontendBaseTplSourceDir = self.plusDir + '/app/design/frontend/base/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            frontendBaseTplTargetDir = target_dir + '/app/design/frontend/base/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(frontendBaseTplSourceDir, frontendBaseTplTargetDir)
 
            #frontend base default locale
            frontBaseLocaleSourceFile = self.plusDir + "/app/design/frontend/base/default/locale/en_US/" + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            frontBaseLocaleTargetFile = target_dir + "/app/design/frontend/base/default/locale/en_US/"
            copyFile(frontBaseLocaleSourceFile,frontBaseLocaleTargetFile)
 
            #
            #frontend default default layout
            frontDefaultLayoutSourceFile = self.plusDir + "/app/design/frontend/default/default/layout/" + self.modelName[0].lower() + self.modelName[1:] +'.xml'
            frontDefaultLayoutTargetFile = target_dir + "/app/design/frontend/default/default/layout/"
            copyFile(frontDefaultLayoutSourceFile,frontDefaultLayoutTargetFile)
 
            #frontend default default template
            frontDefaultTplSourceDir = self.plusDir + '/app/design/frontend/default/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            frontDefaultTplTargetDir = target_dir + '/app/design/frontend/default/default/template/' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(frontDefaultTplSourceDir, frontDefaultTplTargetDir)
 
            #frontend default default locale
            frontDefaultLocaleSourceFile = self.plusDir + "/app/design/frontend/default/default/locale/en_US/" + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            frontDefaultLocaleTargetFile = target_dir + "/app/design/frontend/default/default/locale/en_US/"
            copyFile(frontDefaultLocaleSourceFile,frontDefaultLocaleTargetFile)
 
        else:
            raise Exception("app is None")
        #js
        JsourceDir = self.plusDir + "/js/" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(JsourceDir):
            #creatDirs(target_dir, 'js', 2, self.plusName, self.modelName)
            Jtarget_dir = target_dir + '/js/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(JsourceDir, Jtarget_dir)
 
        else:
            JsourceOtherDir = self.plusDir + "/js/" + self.plusName
            if os.path.isdir(JsourceOtherDir):
                Jtarget_dir = target_dir + '/js/' + self.plusName
                copyFiles(JsourceDir, Jtarget_dir)
            print "js is None"
        #media
        #MsourceDir = self.plusDir + "/media/" + self.modelName[0].lower() + self.modelName[1:]


        #if os.path.isdir(MsourceDir):
            #Mtarget_dir = target_dir + '/media/' + self.modelName[0].lower() + self.modelName[1:]
            #copyFiles(MsourceDir, Mtarget_dir)
        #else:
            #print "media is None"
        #lib
        LsourceDir = self.plusDir + "/lib/" + self.modelName[0].lower() + self.modelName[1:]
 
        if os.path.isdir(LsourceDir):
            Ltarget_dir = target_dir + '/lib/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(LsourceDir, Ltarget_dir)
        else:
            print "lib is None"
        #skin
        #admin base
        AbaseSourceDir = self.plusDir + "/skin/adminhtml/base/default/" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(AbaseSourceDir):
            Abasetarget_dir = target_dir + '/skin/adminhtml/base/default/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(AbaseSourceDir, Abasetarget_dir)
 
        #admin default
        AdefaultSourceDir = self.plusDir + "/skin/adminhtml/default/default/" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(AdefaultSourceDir):
            Adefaulttarget_dir = target_dir + '/skin/adminhtml/default/default/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(AdefaultSourceDir, Adefaulttarget_dir)
        #frontend base
        FbaseSourceDir = self.plusDir + "/skin/frontend/base/default/" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(FbaseSourceDir):
            Fbasetarget_dir = target_dir + '/skin/frontend/base/default/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(FbaseSourceDir, Fbasetarget_dir)
        #frontend default
        FdefaultSourceDir = self.plusDir + "/skin/default/default/default/" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(FdefaultSourceDir):
            Fdefaulttarget_dir = target_dir + '/skin/default/default/default/' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(FdefaultSourceDir, Fdefaulttarget_dir)
 
    def makeDirWindows(self):
        print self.type
 
#        os._exit()
        if(self.type == '1'):
            communityLocal = 'community\\'
        elif(self.type == '2'):
            communityLocal = 'local\\'
        else:
            raise Exception("no select type !")
            os._exit('no select type')
        sourceDir = self.plusDir + r"\app\code\\" + communityLocal + self.plusName + r'\\' + self.modelName
        target_dir = self.target_dir + self.newZipName
        print target_dir
        print opsystem
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
        if os.path.isdir(sourceDir):
            #creatDirs(target_dir, 'app', 2, self.plusName, self.modelName)
            targetDir = target_dir + r"\app\code\\" + communityLocal + self.plusName + r'\\' + self.modelName
            copyFiles(sourceDir, targetDir)
            #Modules
            etcSourceFile = self.plusDir + "\\app\\etc\\modules\\" + self.plusName + '_' +self.modelName +'.xml'
            etcTargetDir = target_dir + "\\app\\etc\\modules\\"
            copyFile(etcSourceFile,etcTargetDir)
 
            #adminhtml layout
            adminLayoutSourceFile = self.plusDir + r"\app\design\adminhtml\default\default\layout\\" + self.plusName + '_' +self.modelName +'.xml'
            adminLayoutTargetDir = target_dir + r'\app\design\adminhtml\default\default\layout\\'
            copyFile(adminLayoutSourceFile,adminLayoutTargetDir)
 
            #adminhtml local en_US
            adminLocalSourceFile = self.plusDir + r'\app\design\adminhtml\default\default\locale\en_US\\' + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            adminLocalTargetDir = target_dir + r'\app\design\adminhtml\default\default\locale\en_US\\'
            copyFile(adminLocalSourceFile,adminLocalTargetDir)
 
            #adminhtml template
            adminTplSourceDir = self.plusDir + r'\app\design\adminhtml\default\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            adminTplTargetDir = target_dir + r'\app\design\adminhtml\default\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(adminTplSourceDir, adminTplTargetDir)
 
            #frontend base default layout
            frontBaseLayoutSourceFile = self.plusDir + r"\app\design\frontend\base\default\layout\\" + self.plusName + '_' +self.modelName +'.xml'
            frontBaseLayoutTargetFile = target_dir + r"\app\design\frontend\base\default\layout\\"
            copyFile(frontBaseLayoutSourceFile,frontBaseLayoutTargetFile)
 
            #frontend base default template
            frontendBaseTplSourceDir = self.plusDir + r'\app\design\frontend\base\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            frontendBaseTplTargetDir = target_dir + r'\app\design\frontend\base\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(frontendBaseTplSourceDir, frontendBaseTplTargetDir)
 
            #frontend base default locale
            frontBaseLocaleSourceFile = self.plusDir + r"\app\design\frontend\base\default\locale\en_US\\" + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            frontBaseLocaleTargetFile = target_dir + r"\app\design\frontend\base\default\locale\en_US\\"
            copyFile(frontBaseLocaleSourceFile,frontBaseLocaleTargetFile)
 
            #
            #frontend default default layout
            frontDefaultLayoutSourceFile = self.plusDir + r"\app\design\frontend\default\default\layout\\" + self.plusName + '_' +self.modelName +'.xml'
            frontDefaultLayoutTargetFile = target_dir + r"\app\design\frontend\default\default\layout\\"
            copyFile(frontDefaultLayoutSourceFile,frontDefaultLayoutTargetFile)
 
            #frontend default default template
            frontDefaultTplSourceDir = self.plusDir + r'\app\design\frontend\default\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            frontDefaultTplTargetDir = target_dir + r'\app\design\frontend\default\default\template\\' + self.modelName[0].lower() + self.modelName[1:]
            #os._exit(0)
            copyFiles(frontDefaultTplSourceDir, frontDefaultTplTargetDir)
 
            #frontend default default locale
            frontDefaultLocaleSourceFile = self.plusDir + r"\app\design\frontend\default\default\locale\en_US\\" + self.modelName[0].lower() + self.modelName[1:] +'.csv'
            frontDefaultLocaleTargetFile = target_dir + r"\app\design\frontend\default\default\locale\en_US\\"
            copyFile(frontDefaultLocaleSourceFile,frontDefaultLocaleTargetFile)
 
        else:
            raise Exception("app is None")
        #js
        JsourceDir = self.plusDir + r"\js\\" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(JsourceDir):
            #creatDirs(target_dir, 'js', 2, self.plusName, self.modelName)
            Jtarget_dir = target_dir + r'\js\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(JsourceDir, Jtarget_dir)
        else:
            print "js is None"
        #media
        MsourceDir = self.plusDir + r"\media\\" + self.modelName[0].lower() + self.modelName[1:]
 
        if os.path.isdir(MsourceDir):
            Mtarget_dir = target_dir + r'\media\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(MsourceDir, Mtarget_dir)
        else:
            print "media is None"
 
        #lib
        LsourceDir = self.plusDir + r"\lib\\" + self.modelName[0].lower() + self.modelName[1:]
 
        if os.path.isdir(LsourceDir):
            Ltarget_dir = target_dir + r'\lib\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(LsourceDir, Ltarget_dir)
        else:
            print "lib is None"
        #skin
        #admin base
        AbaseSourceDir = self.plusDir + r"\skin\adminhtml\base\default\\" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(AbaseSourceDir):
            Abasetarget_dir = target_dir + r'\skin\adminhtml\base\default\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(AbaseSourceDir, Abasetarget_dir)
        #admin default
        AdefaultSourceDir = self.plusDir + r"\skin\adminhtml\default\default\\" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(AdefaultSourceDir):
            Adefaulttarget_dir = target_dir + r'\skin\adminhtml\default\default\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(AdefaultSourceDir, Adefaulttarget_dir)
        #frontend base
        FbaseSourceDir = self.plusDir + r"\skin\frontend\base\default\\" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(FbaseSourceDir):
            Fbasetarget_dir = target_dir + r'\skin\frontend\base\default\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(FbaseSourceDir, Fbasetarget_dir)
        #frontend default
        FdefaultSourceDir = self.plusDir + r"\skin\default\default\default\\" + self.modelName[0].lower() + self.modelName[1:]
        if os.path.isdir(FdefaultSourceDir):
            Fdefaulttarget_dir = target_dir + r'\skin\default\default\default\\' + self.modelName[0].lower() + self.modelName[1:]
            copyFiles(FdefaultSourceDir, Fdefaulttarget_dir)
#        print floder_path
#        file_list = []
#        if floder_path is None:
#            raise Exception("floder_path is None")
#        for dirpath, dirnames, filenames in os.walk(floder_path):
#            #print dirnames
#            for name in filenames:
#                file_list.append(dirpath + '\\' + name)
#        self.source = file_list
#        target_dir = 'D:\\zhz\\aa'
#        if not os.path.exists(target_dir):
#            os.mkdir(target_dir)
#            print target_dir


 
def copyFiles(sourceDir, targetDir):
    if os.path.isdir(sourceDir):
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
 
        global copyFileCounts
        print sourceDir
        print copyFileCounts
        print u"%s 当前处理文件夹%s已处理%s 个文件" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), sourceDir, copyFileCounts)
        for f in os.listdir(sourceDir):
            sourceF = os.path.join(sourceDir, f)
            targetF = os.path.join(targetDir, f)
            if os.path.isfile(sourceF):
                #创建目录
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                copyFileCounts += 1
                #文件不存在，或者存在但是大小不同，覆盖
                if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                    #2进制文件
                    if(opsystem == 'w'):
                        os.system ("copy %s %s" % (sourceF, targetF))
                    elif(opsystem == 'l'):
                        os.system ("cp %s %s" % (sourceF, targetF))
                    if os.path.isfile (targetF): print "Success"
                    #open(targetF, "wb").write(open(sourceF, "rb").read());
                    print u"%s %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF)
                else:
                    print u"%s %s 已存在，不重复复制" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF)
            if os.path.isdir(sourceF):
                copyFiles(sourceF, targetF)
 
def copyFile(sourceFile, targetDir):
    if os.path.isfile(sourceFile):
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        if(opsystem == 'w'):
            os.system ("copy %s %s" % (sourceFile, targetDir))
        elif(opsystem == 'l'):
            os.system ("cp %s %s" % (sourceFile, targetDir))
 
def isset(v):
     try:
         type (eval(v))
     except:
         return 0
     else:
         return 1
if __name__ == '__main__':
    #example: python zip.py faarao_colorpick faarao colorpick 2
    if len(sys.argv) <4:
        print ("Error ! Missing parameter !\r\n#example: python packages.py faarao_colorpick faarao colorpick 2(1为community，2为local)")
        os._exit(0)
    plusDir = os.getcwd()
    sysstr = platform.system()
    #plusDir = r'D:\wamp\www\17test.mage'
    #插件名  如"faarao"
    plusName = sys.argv[2]
    #模块名 如'colorpick'
    modelName = sys.argv[3]
    #保存的文件名
    newZipName = sys.argv[1]
    if(sysstr == "Windows"):
        target_dir = plusDir + r'\\'
        opsystem = 'w'
    elif(sysstr == "Linux"):
        target_dir = plusDir + '/'
        opsystem = 'l'
    else:
        raise Exception("this system not support!\n")
    #类型,是读取community下的还是local。默认是local
    #type = sys.argv[4]
    if len(sys.argv)> 4:
        type = sys.argv[4]
    else:
        type = '2'
    print 'newZipName ' + newZipName
    print 'plusName ' + plusName
    print 'modelName ' + modelName
    print 'type ' + type
    magento = magentoZip(target_dir, plusDir, plusName, modelName , newZipName , type)
    if(opsystem == 'w'):
        magento.makeDirWindows()
        magento.exeZipFile()
    elif(opsystem == 'l'):
        magento.makeDirLinux()
        magento.tarZipFile()
 
 
    #magento.test()
