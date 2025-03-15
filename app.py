# https://github.com/scrapinghub/splash/issues/735
# https://pypi.org/project/klein/

# sudo docker build -t klein-python-app .
# sudo docker run --restart=always --expose 9000 --net=host -p 9000:9000 klein-python-app

# Сохранение образа с перенаправлением стандартного вывода (stdout) в tar-архив. 
# Пример кода: docker save image:tag > path/to/file.tar

# sudo docker save klein-python-app:latest > ./klein-py-app.tar

# Загрузить образ Docker. Для этого используется команда docker load с указанием имени архива. 
# Пример: docker load -i my-image.tar

# sudo docker load -i ./klein-py-app.tar

# Удалить образ
# sudo docker image rm klein-python-app

###############################################################################################
# https://hub.docker.com/

# sudo docker login
# sudo docker tag klein-python-app:latest tonycythony/klein-python-app-in-docker:klein
# sudo docker push tonycythony/klein-python-app-in-docker:tagname

###############################################################################################

import json
from klein import Klein

app = Klein()

@app.route('/')
def root(request):
    return 'Welcome'

@app.route('/hello')
def hello(request):
    return 'Hello World'

@app.route('/hello/<name>')
def helloName(request, name):
    return 'Hello %s!' % name

@app.route('/hello/<name>/<int:age>')
def helloNameAge(request, name, age):
    if age <= 1:
        return '%s is just starting life.' % name
    elif age >= 2 and age <= 29:
        return '%s is %d years old. You are so young!' % (name, age)
    return '%s is %d years old! You are so old!' % (name, age)

@app.route('/methods', methods=['POST', 'delete', 'Google'])
def specificMethods(request):
    return json.dumps({
                      'boolean': True,
                      'int': 1,
                      'list': [1,2,3]
                    })

app.run(host='0.0.0.0', port=9000)

# $ curl localhost:9000/hello
# Hello World

# $ curl -X GET localhost:9000/methods
# <!doctype html>
# <html lang=en>
# <title>405 Method Not Allowed</title>
# <h1>Method Not Allowed</h1>
# <p>The method is not allowed for the requested URL.</p>

# $ curl -X DELETE localhost:9000/methods
# {"boolean": true, "int": 1, "list": [1, 2, 3]}

# $ curl localhost:9000/
# Welcome

# $ curl localhost:9000/hello/Thony/31
# Thony is 31 years old! You are so old!

# $ curl -X google localhost:9000/methods
# {"boolean": true, "int": 1, "list": [1, 2, 3]}

# 2025-03-12 10:40:22+0000 [-] Timing out client: IPv4Address(type='TCP', host='192.168.1.121', port=49428)
# 2025-03-12 10:40:27+0000 [-] "192.168.1.121" - - [12/Mar/2025:10:40:26 +0000] "GET / HTTP/1.1" 200 7 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
