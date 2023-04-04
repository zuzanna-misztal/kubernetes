#! /bin/bash
docker build -t api-image .
cd k8s
kubectl delete -f ./secrets.yml -f ./db.yml -f ./api.yml -f ./ingress.yml
kubectl apply -f ./secrets.yml -f ./db.yml -f ./api.yml -f ./ingress.yml