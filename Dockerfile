# 从仓库拉取 带有 python 3.9 的 Linux 环境
FROM python:3.9-slim

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 添加 Debian 镜像源
RUN echo \
    deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib \
    deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib \
    deb https://mirrors.aliyun.com/debian-security/ bullseye-security main \
    deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main \
    deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib \
    deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib \
    deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib \
    deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib \
    > /etc/apt/sources.list

# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code
# 更新 pip
RUN pip install pip -U -i https://mirrors.aliyun.com/pypi/simple/

# 更新apt
RUN apt-get update

# 安装相关依赖
RUN apt-get install libgl1-mesa-glx -y
RUN apt-get install libglib2.0-0 -y
RUN apt-get install libgomp1 -y
# RUN apt-get install libsm6 libxext6 -y
# RUN apt-get install libxrender-dev -y 

# 将 requirements.txt 复制到容器的 code 目录
ADD requirements.txt /code/
RUN pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple
RUN pip install pip PyMuPDF==1.21.1 -i https://mirror.baidu.com/pypi/simple

# 将当前目录复制到容器的 code 目录
ADD . /code/

# 运行容器时执行的命令
CMD ["python3", "manage.py", "runserver", "0.0.0.0:10086"]