### 参考文章
https://github.com/kubernetes-sigs/aws-load-balancer-controller/tree/main/helm/aws-load-balancer-controller

### 创建EKS OIDC Provider (这个操作每个集群只需要做一次）
```shell
eksctl utils associate-iam-oidc-provider --cluster=QytangCluster --approve --region us-east-1
```

### 下载为AWS负载均衡控制器的IAM策略
```shell
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
```

### 创建名为"AWSLoadBalancerControllerIAMPolicy"的IAM策略
```shell
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam-policy.json
```

### 为负载均衡控制器,创建IAM Role和ServiceAccount
```shell
eksctl create iamserviceaccount \
--cluster=QytangCluster \
--namespace=kube-system \
--name=aws-load-balancer-controller \
--region us-east-1 \
--attach-policy-arn=arn:aws:iam::609047981853:policy/AWSLoadBalancerControllerIAMPolicy \
--approve
```

### 设置helm repo
```shell
helm repo add eks https://aws.github.io/eks-charts
```

### 使用IAM Role作为ServiceAccount安装
```shell
helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=QytangCluster -n kube-system --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller
```

### 查看pod
```shell
qinke@qinkedeMBP ~ % kubectl get pods -n kube-system
NAME                                            READY   STATUS    RESTARTS   AGE
aws-load-balancer-controller-6885ddb5f7-2tk4w   1/1     Running   0          29s
aws-load-balancer-controller-6885ddb5f7-zwrdj   1/1     Running   0          29s
aws-node-brjlt                                  1/1     Running   0          68m
aws-node-g9xdk                                  1/1     Running   0          67m
aws-node-m4ffv                                  1/1     Running   0          68m
aws-node-tr586                                  1/1     Running   0          67m
aws-node-vqsgr                                  1/1     Running   0          68m
coredns-66cb55d4f4-crfww                        1/1     Running   0          77m
coredns-66cb55d4f4-lbjkf                        1/1     Running   0          77m
kube-proxy-48gp9                                1/1     Running   0          68m
kube-proxy-8vpfv                                1/1     Running   0          68m
kube-proxy-nrmbw                                1/1     Running   0          68m
kube-proxy-xqz54                                1/1     Running   0          67m
kube-proxy-zkhw6                                1/1     Running   0          67m
```

### 查看Deploy
```shell
qinke@qinkedeMBP ~ % kubectl get deploy -n kube-system
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-controller   2/2     2            2           74s
coredns                        2/2     2            2           77m
```
