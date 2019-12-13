# ABCBank webapp



## Development

### build image

1. git clone

    ```
    git clone git@github.ibm.com:NOGAYAMA/abcbank-webapp.git
    cd abcbank-webapp
    ```

1. build image from Dockerfile

    ```
    docker image build --tag abcbank-webapp:latest .
    ```

1. (optional) smoketest on local

    ```
    docker run -d -p 5000:5000 abcbank-webapp:latest
    docker ps 
    curl localhost:5000
    
    docker stop $(docker ps -lq)
    docker rm   $(docker ps -lq)
    ```

### upload the image to DockerHub

1. make sure user account on [DockerHub](https://hub.docker.com)

1. create a new tag of the image

    ```
    $ docker image list 
    REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
    abcbank-webapp                             latest              b48c890a6c82        9 minutes ago       
    ```

    ```
    docker image tag b48c890a6c82 nogayama/abcbank-webapp:latest
    ```

1. push the image to dockerhub

    ```
    docker image push nogayama/abcbank-webapp:latest
    ```

    After pushing, you can see image on DockerHub e.g., [nogayama](https://cloud.docker.com/u/nogayama/repository/docker/nogayama/abcbank-webapp)

### pull the image

1. pull the image

    ```
    docker image pull nogayama/abcbank-webapp:latest
    ```

### Upload the image to IBM Cloud

1. login to IBM Cloud

    ```
    $ ibmcloud login --sso
    ```

2. (optional) change region`ibmcloud cr region-set`

3. Login to Container registry

    ```
    $ ibmcloud cr login
    ```


3. add namespace

    ```
    $ ibmcloud cr namespace-add nogayama
    ```

4. add tag

    ```
    docker tag abcbank-web "de.icr.io/nogayama/abcbank-web:latest"
    ```

5. push

    ```bash
    #docker push <region>.icr.io/<my_namespace>/<image_repo>:<tag>
    $ docker push "jp.icr.io/nogayamaapp/mav:0.0.1"
    ```

    ```
    $ ibmcloud cr image-list
    イメージをリストしています...
    リポジトリー                タグ    ダイジェスト   名前空間      作成          サイズ   セキュリティー状況
    jp.icr.io/nogayamaapp/mav   0.0.1   8da58d49aea9   nogayamaapp   2 hours ago   381 MB   3 件の問題   
    OK
    ```

## Quick demo

```
./build.sh
kubectl create namespace abcbank
kubectl apply -f abcbank.yaml -n abcbank
kubectl get pods,deployments,service -n abcbank
curl localhost:30880/api/v1
```


