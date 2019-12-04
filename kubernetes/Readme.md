
## Primero Mircroservicio: Obras Catalog Service

1. Obtener los namespaces
```
kubectl get namespace
```

2. Crear un namespace: 
```
kubectl create namespace obras
```


3. Crear un deployment

```
kubectl create -f ./kubernetes/deployment-obras.yaml --namespace=obras

kubectl apply -f ./kubernetes/deployment-obras.yaml --namespace=obras
```

4. Obtener los deployments 

```
kubectl get deployment --namespace=obras
```

5. Obtener los pods

```
kubectl get pods --namespace=obras
````

6. Obtener info del deployment:

```
kubectl describe deployment/obras --namespace=obras
```

7. Obtener los servicios:
```
kubectl get service --namespace=obras
```

8. Obtener la url del servicio

```
minikube service obras --url --namespace=obras
```

## Segundo Mircroservicio: Ratings Service

1. Obtener los namespaces
```
kubectl get namespace
```

2. Crear un namespace: 
```
kubectl create namespace obras
```


3. Crear un deployment

```
kubectl create -f ./kubernetes/deployment-ratings.yaml --namespace=obras

kubectl apply -f ./kubernetes/deployment-ratings.yaml --namespace=obras
```

4. Obtener los deployments 

```
kubectl get deployment --namespace=obras
```

5. Obtener los pods

```
kubectl get pods --namespace=obras
````

6. Obtener info del deployment:

```
kubectl describe deployment/ratings --namespace=obras
```

7. Obtener los servicios:
```
kubectl get service --namespace=obras
```

8. Obtener la url del servicio

```
minikube service ratings --url --namespace=obras


## Aplicación web

1. Obtener los namespaces
```
kubectl get namespace
```

2. Crear un namespace: 
```
kubectl create namespace obras
```


3. Crear un deployment

```
kubectl create -f ./kubernetes/deployment-webapp.yaml --namespace=obras

kubectl apply -f ./kubernetes/deployment-webapp.yaml --namespace=obras
```

4. Obtener los deployments 

```
kubectl get deployment --namespace=obras
```

5. Obtener los pods

```
kubectl get pods --namespace=obras
````

6. Obtener info del deployment:

```
kubectl describe deployment/webapp --namespace=obras
```

7. Obtener los servicios:
```
kubectl get service --namespace=obras
```

8. Obtener la url del servicio

```
minikube service webapp --url --namespace=obras
```
