### 安装kubectl
https://kubernetes.io/zh/docs/tasks/tools/

### 连接eks
https://aws.amazon.com/cn/premiumsupport/knowledge-center/eks-cluster-connection/

### 获取kube配置文件脚本
```shell
aws eks --region us-east-1 update-kubeconfig --name QytangCluster
```

### 策略kubectl
```shell
qinke@qinkedeMBP ~ % kubectl get nodes
NAME                          STATUS   ROLES    AGE   VERSION
ip-10-6-11-140.ec2.internal   Ready    <none>   76m   v1.21.5-eks-bc4871b
ip-10-6-11-188.ec2.internal   Ready    <none>   75m   v1.21.5-eks-bc4871b
ip-10-6-11-75.ec2.internal    Ready    <none>   76m   v1.21.5-eks-bc4871b
ip-10-6-12-139.ec2.internal   Ready    <none>   75m   v1.21.5-eks-bc4871b
ip-10-6-12-53.ec2.internal    Ready    <none>   75m   v1.21.5-eks-bc4871b

qinke@qinkedeMBP ~ % kubectl cluster-info
Kubernetes control plane is running at https://541B69C9F9CF0F6BDD04733D807031BC.gr7.us-east-1.eks.amazonaws.com
CoreDNS is running at https://541B69C9F9CF0F6BDD04733D807031BC.gr7.us-east-1.eks.amazonaws.com/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```
