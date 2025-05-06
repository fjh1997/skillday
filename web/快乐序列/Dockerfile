# 使用官方的 PHP 镜像
FROM php:8.2-cli

# 设置工作目录
WORKDIR /var/www/html

# 复制当前目录下的 HTML 文件到容器中
COPY html/ /var/www/html/

# 暴露端口 8000
EXPOSE 8000

# 启动 PHP 内置 Web 服务器
CMD ["su","-m","www-data","-s","/bin/bash","-c","php -S 0.0.0.0:8000"]
