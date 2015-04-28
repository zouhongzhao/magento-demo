##打包工具


==== 使用方法： ====


1,下载packages.py文件,并且把该文件放在项目根目录下。比如:x2322.就放在/var/www/x2322/下面


2,执行命令


python packages.py 生成的文件名 包名 插件名 插件路径(1或2.1代表community，2代表local。默认是local下)


例如：打包Faarao_Colorpick插件 并保存到colorpick目录。



如果Faarao_Colorpick插件是放在app/code/local下面的,就这样:

```
python packages.py colorpick faarao colorpick 2
```

如果Faarao_Colorpick插件是放在app/code/community下面的,就这样:

```
python packages.py colorpick faarao colorpick 1
```

##注意：


有可能模板和layout路径存放的名字不是按照插件名来的，所有会有漏掉。到时候自己再加进去。


现在window和linux平台都能直接用了(有bug的话记得找我)



参考:http://www.cnblogs.com/hongten/archive/2013/07/28/hongten_python_upper_lower.html|http://www.cnblogs.com/hongten/archive/2013/07/28/hongten_python_upper_lower.html

