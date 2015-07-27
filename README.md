### 功能
从项目目录中找出列表中的增量文件，按原目录结构打包成压缩文件<br>
java文件最终会查找对应的class文件，其他文件不变

### 使用说明
<br>1、将要打包的文件名写到file.txt中换行分隔（java文件直接写以.java结尾即可）
<br>2、双击findFile.py
<br>3、按提示输入要查找文件所在项目的webapp目录
<br>4、按提示输入打包后的压缩文件名
<br>5、开始打包，如果找到相同文件名会提示按数字进行选择，不选择则打包所有文件，选择多个使用逗号分割
<br>6、打包完成，在uploadFile文件夹下生成压缩文件
