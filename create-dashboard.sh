echo "Deploy through OpenShift UI, python:latest"
echo "make sure to add the context dir for /dashboard"


#oc new-app https://github.com/nsabine/openshift-batch-demo --context=dashboard --name=dashboard --labels='app=rq-dashboard,tier=dashboard' 
