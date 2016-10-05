oc new-app --name=redis-master --docker-image=redis --labels='app=redis,role=master,tier=backend' -o yaml > queue.yaml
