### 部署资源配置文件(本地路径)
```shell
kubectl apply -f /Users/qinke/PycharmProjects/AWS2021/CloudFormation/Scripts/EKS/yaml/qyt_lb.yaml
```

### 查看POD
```shell
qinke@qinkedeMBP dockerfile % kubectl get pod -n qyt-lb
NAME                                READY   STATUS    RESTARTS   AGE
deployment-qyt-lb-74876ff7b-mh446   1/1     Running   0          3m8s
deployment-qyt-lb-74876ff7b-xkmj5   1/1     Running   0          2m54s
```

### 查看Service
```shell
qinke@qinkedeMBP dockerfile % kubectl get svc -n qyt-lb
NAME     TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
qyt-lb   NodePort   172.20.112.87   <none>        80:32333/TCP   111m
```

### 查看Ingress
```shell
qinke@qinkedeMBP dockerfile % kubectl get ingress -n qyt-lb
NAME     CLASS    HOSTS   ADDRESS                                                             PORTS   AGE
qyt-lb   <none>   *       k8s-qytlb-qytlb-8c74c336ac-2045878957.us-east-1.elb.amazonaws.com   80      111m
```

### 游览器测试
http://k8s-qytlb-qytlb-8c74c336ac-2045878957.us-east-1.elb.amazonaws.com