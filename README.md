## 这是一个基于flask的课程，学生，老师信息管理系统
### 1.安装相关依赖性
```bash
pip3 install -r ./requirement.txt
```
### 2.初始化数据库
``` bash
python ./manage.py db init
```
### 3.数据库迁移
```bash
python ./manage.py db migrate
```
### 4.数据库升级
```bash
python ./manage.py db upgrade
```
### 5.导入虚拟数据
```bash
python ./manage.py generate_fake
```
### 6.启动web服务
```bash
python ./manage.py runserver
```
