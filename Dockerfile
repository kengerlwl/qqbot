FROM python:3.10-slim
LABEL maintainer="2892211452@qq.com"


RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
	&& sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
	&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime



WORKDIR /var/app
COPY . /var/app

# 设置env
ENV TZ Asia/Shanghai


# 安装python需要的库
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# test

CMD ["bash","run_server.sh"]
