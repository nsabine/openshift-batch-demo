oc new-app https://github.com/nsabine/openshift-batch-demo --context=frontend --name=frontend --labels='app=flask,tier=frontend' -o yaml > frontend.yaml
