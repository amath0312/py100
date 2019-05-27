#Python Day 15: 图形和办公文档处理

## 图像操作

Pillow：PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作。<br/>
Pillow.Image:
    * show(): 显示
    * open(path)->Image: 打开
    * format->str: 格式,JPG
    * size->tuple: 像素尺寸
    * mode->str: 模式,RGB
    * crop(rect)->Image: 裁剪图像
    * thumbnail(size)->Image: 缩略图
    * resize(size)->Image: 缩放
    * paste(img, pos): 将img图像粘贴到Image对象的指定位置
    * rotate(angle)->Image: 旋转
    * transpose(type)->Image: type可设置为Image.FLIP_LEFT_RIGHT，左右翻转
    * putpixel((x,y), (r,g,b))->Image: 将指定像素的颜色替换为指定值
    * filter(filter)->Image: 滤镜效果，filter可设置为PIL.ImageFilter.CONTOUR

## Excel

openpyxl模块可以在Python程序中读取和修改Excel电子表格。<br/>
[官方文档](https://openpyxl.readthedocs.io/en/stable/#)

也可以使用xlrd模块 / xlwt模块

## Word

python-docx模块可以创建和修改Word文档

## PDF

可以利用pypdf2模块 / reportlab模块处理PDF文件

