#!/bin/bash

yum update -y
yum install -y python3 git python3-pip

export BUCKET_NAME='BUCKET_NAME'

git clone https://github.com/devqos/aws-python.git /home/ec2-user/flask-app
cd /home/ec2-user/flask-app || exit

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

cat <<EOF > /etc/systemd/system/flask-app.service
[Unit]
Description=Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/flask-app
ExecStart=/home/ec2-user/flask-app/venv/bin/python3 -m flask --app app/main.py run --host=0.0.0.0 --port=5000 --debug
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable flask-app
systemctl start flask-app