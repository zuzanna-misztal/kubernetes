#! /bin/bash

docker build -t bff-im ./bff/ 
docker build -t api1-im ./api1/ 
docker build -t api2-im ./api2/ 

cd k8s

kubectl delete -f ./api1-service.yml -f ./api2-service.yml -f ./bff-service.yml -f ./ingress.yml
kubectl apply -f ./api1-service.yml -f ./api2-service.yml -f ./bff-service.yml -f ./ingress.yml