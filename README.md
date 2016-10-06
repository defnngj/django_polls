=======
# django_polls

介绍：
  参考Django官方文档的demo,并将添加投票系统相关接口, 并为接口编写测试用例。
  https://docs.djangoproject.com/en/1.10/intro/tutorial01/

Python版本与依赖库：
  * Python3.5 :https://www.python.org/
  * Django1.9.7 :https://www.djangoproject.com/
  * Requests  : http://www.python-requests.org/en/master/

运行方式与接口文档：
  查看doc/目录。

  1.运行项目
  ...\django_polls_>python3 manage.py runserver

  2.登录后台添加数据
  http://127.0.0.1:8000/admin/  账号/密码：admin/admin123456

  3.运行接口用例：
  ...\django_polls\polls\interface_tests
  > python3 tests.py
  ............
  ----------------------------------------------------------------------
  Ran 12 tests in 0.153s

  OK
