![](https://raw.githubusercontent.com/unton3ton/klein-python-web-app-in-docker/refs/heads/main/photo_2025-03-11_20-16-09.jpg)

```bash
curl localhost:9000/hello
Hello World
```

```bash
curl -X GET localhost:9000/methods
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```

```bash
curl -X DELETE localhost:9000/methods
{"boolean": true, "int": 1, "list": [1, 2, 3]}
```

```bash
curl localhost:9000/
Welcome
```

![](https://raw.githubusercontent.com/unton3ton/klein-python-web-app-in-docker/refs/heads/main/hoi-klein.PNG)

```bash
curl localhost:9000/hello/Thony/31
Thony is 31 years old! You are so old!
```

![](https://raw.githubusercontent.com/unton3ton/klein-python-web-app-in-docker/refs/heads/main/Capture.PNG)

```bash
curl -X google localhost:9000/methods
{"boolean": true, "int": 1, "list": [1, 2, 3]}
```

# Sources

* [tonycythony/klein-python-app-in-docker](https://hub.docker.com/repository/docker/tonycythony/klein-python-app-in-docker/general)
* [Remove Docker Images, Volumes, and Containers in Seconds](https://kinsta.com/blog/docker-remove-images/)
* [Что такое контейнеризация и как использовать Docker с Python](https://sky.pro/media/chto-takoe-kontejnerizacziya-i-kak-ispolzovat-docker-s-python/)
* [Упаковка простого Flask приложения в Docker контейнер](https://k2.cloud/blog/about-technologies/flask-prilozheniya-v-docker/)
* [Twisted Klein: Basics](https://notoriousno.blogspot.com/2016/08/basics-routes-methods-variables-this.html?m=1)
* [pip install Klein](https://pypi.org/project/klein/)

![](https://raw.githubusercontent.com/unton3ton/klein-python-web-app-in-docker/refs/heads/main/photo_2025-03-15_10-23-35.jpg)
