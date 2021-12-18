### 获取登录密码
```shell
qinke@qinkedeMBP ~ % aws ECR get-login-password --region us-east-1
~~~忽略密码~~~
```

### Linux登录
```shell
docker login docker login 609047981853.dkr.ECR.us-east-1.amazonaws.com
用户名:AWS
密码: 粘贴上面的密码
```

### MAC登录问题(拷贝Linux产生的认证文件)
```shell
产生 .docker/config.json

内容如下:
{
        "auths": {
                "609047981853.dkr.ecr.us-east-1.amazonaws.com": {
                        "auth": ~~~忽略认证内容~~~ 
                },
                "https://index.docker.io/v1/": {
                        "auth": ~~~忽略认证内容~~~ 
                }
        }
}
```