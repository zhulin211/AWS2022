### 参考文章
https://github.com/kubernetes-sigs/aws-load-balancer-controller/tree/main/helm/aws-load-balancer-controller

### 如何安装eksctl
```shell
https://docs.aws.amazon.com/zh_cn/eks/latest/userguide/eksctl.html
```

### 创建EKS OIDC Provider (这个操作每个集群只需要做一次）
```shell
eksctl utils associate-iam-oidc-provider --cluster=QytangCluster --approve --region us-east-1
```

### 下载为AWS负载均衡控制器的IAM策略
```shell
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
```

### 创建名为"AWSLoadBalancerControllerIAMPolicy"的IAM策略(如果以前创建过,会报错)
```shell
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam-policy.json
```

### 为负载均衡控制器,创建IAM Role和ServiceAccount
### 让一个K8S集群内的ServiceAccount,拥有AWS的IAM Role的权限
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

### 使用Helm安装负载均衡控制器, 使用预先创建的ServiceAccount
### 使用手机+快连翻墙 测试没有问题
```shell
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
--set clusterName=QytangCluster \
-n kube-system \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller

```

### 如果出现Error: INSTALLATION FAILED: failed to download "eks/aws-load-balancer-controller"
```shell
qinke@qinkedeMBP ~ % helm repo update  # 尝试更新一下
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "eks" chart repository
Update Complete. ⎈Happy Helming!⎈

qinke@qinkedeMBP ~ % helm search repo  # 查看repo是否有"eks/aws-load-balancer-controller"
NAME                                            CHART VERSION   APP VERSION     DESCRIPTION                                       
eks/appmesh-controller                          1.4.4           1.4.2           App Mesh controller Helm chart for Kubernetes     
eks/appmesh-gateway                             0.1.5           1.0.0           App Mesh Gateway Helm chart for Kubernetes        
eks/appmesh-grafana                             1.0.4           6.4.3           App Mesh Grafana Helm chart for Kubernetes        
eks/appmesh-inject                              0.14.8          0.5.0           App Mesh Inject Helm chart for Kubernetes         
eks/appmesh-jaeger                              1.0.2           1.19.0          App Mesh Jaeger Helm chart for Kubernetes         
eks/appmesh-prometheus                          1.0.0           2.13.1          App Mesh Prometheus Helm chart for Kubernetes     
eks/appmesh-spire-agent                         1.0.2           1.0.0           SPIRE Agent Helm chart for AppMesh mTLS support...
eks/appmesh-spire-server                        1.0.1           1.0.0           SPIRE Server Helm chart for AppMesh mTLS suppor...
eks/aws-calico                                  0.3.10          3.19.1          A Helm chart for installing Calico on AWS         
eks/aws-cloudwatch-metrics                      0.0.6           1.247345        A Helm chart to deploy aws-cloudwatch-metrics p...
eks/aws-for-fluent-bit                          0.1.11          2.13.0          A Helm chart to deploy aws-for-fluent-bit project 
eks/aws-load-balancer-controller                1.3.3           v2.3.1          AWS Load Balancer Controller Helm chart for Kub...
eks/aws-node-termination-handler                0.16.0          1.14.0          A Helm chart for the AWS Node Termination Handler 
eks/aws-sigv4-proxy-admission-controller        0.1.2           1               AWS SIGv4 Admission Controller Helm Chart for K...
eks/aws-vpc-cni                                 1.1.12          v1.10.1         A Helm chart for the AWS VPC CNI                  
eks/csi-secrets-store-provider-aws              0.0.1           1.0.r2          A Helm chart to install the Secrets Store CSI D...
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
