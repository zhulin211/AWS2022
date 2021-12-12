FROM centos

##修改时区为东八区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    echo 'Asia/Shanghai' >/etc/timezone

# 安装必要工具
RUN yum install -y python38 python38-devel gcc && yum install -y net-tools && yum install -y bind-utils && yum install -y lrzsz && yum install -y curl && yum install -y dos2unix

# 安装Python模块
RUN pip3 install -i https://pypi.douban.com/simple/ flask
RUN pip3 install -i https://pypi.douban.com/simple/ requests

# 工作目录
WORKDIR /qytang

# 拷贝APP
COPY app.py .

# 转码
RUN dos2unix app.py

# 添加执行权限
RUN chmod +x app.py

# 启动Flask
ENTRYPOINT ["python3", "/qytang/app.py"]