# Sample Python App with MongoDB ReplicaSet

This bundle of playbooks and tasks configure a MongoDB replicaset cluster and install a simple python app that writes data to cluster.

There are three files to edit before running the playbook: vars/weblayer/dev.yml, vars/mongodbrs/dev.yml and group_vars/all.yml

The files are commented out to facilitate the changes needed.

It will create a Route53 internal zone to host the mongodb instances addresses. It's mandatory that your VPC has the DNS Hostnames enabled. To enable it, open the AWS Console, go to VPC service menu, select your VPC, click on Actions -> Edit DNS Hostnames -> Yes

Before you can run the playbook to see the magic happens you will need to install ansible. Follow this steps to install on MacOS:

- sudo easy_install ansible

To create the infrastructure run the command below:
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -vv sampleapp.yml --extra-vars "{ 'app_env': 'dev', 'deploy': 'false' }"

It will create a dev.mycompany.com internal domain on route53.

After the playbook finishes look at your AWS Console and find the public IP of the weblayer instance. To test with everything is working run the command:

curl -XPOST WEBLAYER_PUBLIC_IP_ADDRESS/app

It should return a [OK] message. If not, something went wrong with the setup. 
