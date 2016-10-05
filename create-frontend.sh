oc new-app https://github.com/nsabine/openshift-hpc-demo.git --context=frontend --name=frontend --labels='app=flask,tier=frontend' -o yaml > frontend.yaml
