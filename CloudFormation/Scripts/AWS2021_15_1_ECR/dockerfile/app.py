from flask import Flask
import requests
import socket

node = Flask(__name__)


# 静态路由,最简单页面
@node.route('/', methods=['GET'])
def index():
    instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id").text
    availability_zone = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone").text
    return f"My ID {instance_id}, MY AZ is {availability_zone}, My IP is {socket.gethostbyname(socket.gethostname())}"


if __name__ == "__main__":
    node.run(host='0.0.0.0', port=80)