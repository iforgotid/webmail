# webmail
A python application for job interview
## 1.代码结构
 - web.py  通过webapp2 + jinja 构建的web服务，为webmail提供web界面功能。
 - worker.py 延时发送邮件的background服务
 - service目录 提供消息队列、邮件发送等服务
 - static目录 提供css,js等静态资源
 - Procfile heroku的启动配置文件
 - requirements.txt pip安装依赖

 		#Procfile配置:
 		web: gunicorn web:app
		worker: python worker.py

## 2.webmail在heroku平台的部署
### 2.1部署web服务(web.py)
- Step1.从github克隆代码

		git clone https://github.com/iforgotid/webmail.git
		cd webmail


- Step2.登录heroku

		172-13-0-143:~ philipp$ heroku login
		Enter your Heroku credentials.
		Email: philipp.xue@gmail.com
		Password (typing will be hidden):
		Authentication successful.

- Step3.创建app

		172-13-0-143:~ philipp$ heroku create
		Creating desolate-springs-4277... done, stack is cedar-14
		https://desolate-springs-4277.herokuapp.com/ | https://git.heroku.com/desolate-springs-4277.git

- Step4.将代码部署到heroku

		git push heroku master
		Counting objects: 272, done.
		Delta compression using up to 4 threads.
		Compressing objects: 100% (132/132), done.
		Writing objects: 100% (272/272), 1.44 MiB | 170 KiB/s, done.
		Total 272 (delta 108), reused 272 (delta 108)
		remote: Compressing source files... done.
		remote: Building source:
		remote:
		remote: -----> Python app detected
		remote: -----> Installing runtime (python-2.7.10)
		remote: -----> Installing dependencies with pip
		此处省略安装依赖
		remote: -----> Discovering process types
		remote:        Procfile declares types -> web, worker
		remote:
		remote: -----> Compressing... done, 41.3MB
		remote: -----> Launching... done, v3
		remote:        https://desolate-springs-4277.herokuapp.com/ deployed to Heroku
		remote:
		remote: Verifying deploy... done.
		To https://git.heroku.com/desolate-springs-4277.git
 		* [new branch]      master -> master


- Step5.查看web进程是否启动成功

  		172-13-0-143:webmail philipp$ heroku ps
		=== web (Free): `gunicorn web:app`
		web.1: up 2015/06/22 10:49:33 (~ 5m ago)

- Step6.打开web页面,若能成功打开页面则代表部署完成

		172-13-0-143:webmail philipp$ heroku open
		Opening desolate-springs-4277... done

### 2.2延时发送邮件进程的管理
- Step1.启动worker(heroku一个app最多启动两个免费dyno。one-off24小时内会被关闭，在此不适用)

		172-13-0-143:webmail philipp$ heroku ps:scale worker=1
		Scaling dynos... done, now running worker at 1:Free.

- Step2.查看进程状态

		172-13-0-143:webmail philipp$ heroku ps
		=== web (Free): `gunicorn web:app`
		web.1: up 2015/06/22 10:49:34 (~ 13m ago)

		=== worker (Free): `python worker.py`
		worker.1: up 2015/06/22 11:00:00 (~ 2m ago)

- Step3. 查看日志

		172-13-0-143:webmail philipp$ heroku logs --tail -p worker.1
		2015-06-22T03:00:00.913799+00:00 heroku[worker.1]: Starting process with command `python worker.py`
		2015-06-22T03:00:01.606177+00:00 heroku[worker.1]: State changed from starting to up
		2015-06-22T03:00:03.458293+00:00 app[worker.1]: Start producing: 1434942303
		2015-06-22T03:01:13.088988+00:00 app[worker.1]: Start consuming:



## DEMO地址
https://desolate-springs-4277.herokuapp.com/