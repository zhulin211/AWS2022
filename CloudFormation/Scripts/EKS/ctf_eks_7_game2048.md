### 部署资源配置文件(本地路径)
```shell
kubectl apply -f /Users/qinke/PycharmProjects/AWS2021/CloudFormation/Scripts/EKS/yaml/game2048.yaml
```

### 查看NS, 有新的NS game-2048
```shell
qinke@qinkedeMBP ~ % kubectl get ns
NAME              STATUS   AGE
default           Active   96m
game-2048         Active   17m
kube-node-lease   Active   96m
kube-public       Active   96m
kube-system       Active   96m
```

### 查看pod
```shell
qinke@qinkedeMBP ~ % kubectl get pod -n game-2048
NAME                               READY   STATUS    RESTARTS   AGE
deployment-2048-79785cfdff-9t2st   1/1     Running   0          17m
deployment-2048-79785cfdff-x2hr6   1/1     Running   0          17m
```

### 查看deploy
```shell
qinke@qinkedeMBP ~ % kubectl get deploy -n game-2048
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
deployment-2048   2/2     2            2           17m
```

### 查看ingress
```shell
qinke@qinkedeMBP ~ % kubectl get ingress/ingress-2048 -n game-2048
NAME           CLASS    HOSTS   ADDRESS                                                                   PORTS   AGE
ingress-2048   <none>   *       k8s-game2048-ingress2-d5350941b7-1084965636.us-east-1.elb.amazonaws.com   80      17m

```

### 查看负载均衡控制器日志,当初没有找到subnet的问题就是这样发现的,需要给subnet打标签
```shell
qinke@qinkedeMBP ~ % kubectl logs -n kube-system   deployment.apps/aws-load-balancer-controller
Found 2 pods, using pod/aws-load-balancer-controller-6885ddb5f7-zwrdj
{"level":"info","ts":1639272483.087642,"msg":"version","GitVersion":"v2.3.1","GitCommit":"1d492cb8648b2053086761140d9db9236f867237","BuildDate":"2021-12-08T18:13:11+0000"}
{"level":"info","ts":1639272483.1603692,"logger":"controller-runtime.metrics","msg":"metrics server is starting to listen","addr":":8080"}
{"level":"info","ts":1639272483.1641517,"logger":"setup","msg":"adding health check for controller"}
{"level":"info","ts":1639272483.164374,"logger":"controller-runtime.webhook","msg":"registering webhook","path":"/mutate-v1-pod"}
```
