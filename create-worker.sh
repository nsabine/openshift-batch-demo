echo "Deploy through OpenShift UI, python:latest"
echo "make sure to add the context dir for /worker"


#oc new-app https://github.com/nsabine/openshift-hpc-demo.git --context=worker --name=worker --labels='app=rq,role=worker,tier=backend' -o yaml > worker.yaml
