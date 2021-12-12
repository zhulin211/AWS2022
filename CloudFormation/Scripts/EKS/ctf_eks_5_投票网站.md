### 投票网站
```shell
kubectl apply -f /Users/qinke/PycharmProjects/AWS2021/CloudFormation/Scripts/EKS/yaml/azure-vote.yaml
```

###查看pod
```shell
qinke@qinkedeMBP ~ % kubectl get pod   
NAME                                READY   STATUS    RESTARTS   AGE
azure-vote-back-5f46f8f4cc-ckd8m    1/1     Running   0          12m
azure-vote-front-5d68fcf586-cgm5l   1/1     Running   0          12m
```

### 查看deploy
```shell
qinke@qinkedeMBP ~ % kubectl get deploy
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
azure-vote-back    1/1     1            1           14m
azure-vote-front   1/1     1            1           14m
```

### 查看svc
```shell
qinke@qinkedeMBP ~ % kubectl get svc
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP                                                              PORT(S)        AGE
azure-vote-back    ClusterIP      172.20.193.129   <none>                                                                   6379/TCP       12m
azure-vote-front   LoadBalancer   172.20.90.8      ad567ea87a4434ab491c4e6e7e286b4d-904069269.us-east-1.elb.amazonaws.com   80:30026/TCP   12m
kubernetes         ClusterIP      172.20.0.1       <none>  
```

### 尝试用域名访问网页
