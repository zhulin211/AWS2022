### 进入本地目录
```shell
cd /Users/qinke/PycharmProjects/AWS2021/CloudFormation/Scripts/ECR/dockerfile/ 
```

### 构建镜像(注意M1 MAC要添加--platform linux/amd64)
```shell
docker build --platform linux/amd64 -t 609047981853.dkr.ecr.us-east-1.amazonaws.com/qyt_lb:mac_x86_p80 .
```

### 需要在ECR上创建repository qyt_lb

### 推送镜像
```shell
docker push 609047981853.dkr.ecr.us-east-1.amazonaws.com/qyt_lb:mac_x86_p80
```


