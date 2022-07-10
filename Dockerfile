FROM python:3.10-slim
LABEL maintainer="2892211452@qq.com"

# Why need these step?
# - fast mirror source
# - procps contains useful proccess control commands like: free, kill, pkill, ps, top
# - wget is quite basic tool
# - vim for online debugging
# - sync timezone
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
	&& sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
	&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime



WORKDIR /var/app
COPY . /var/app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

CMD ["python","main.py"]
