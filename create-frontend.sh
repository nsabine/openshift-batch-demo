echo "Deploy through OpenShift UI, python:latest"
echo "make sure to add the context dir for /frontend"


#oc new-app https://github.com/nsabine/openshift-batch-demo --context=frontend --name=frontend --labels='app=flask,tier=frontend' -o yaml > frontend.yaml
