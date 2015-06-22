## 1.代码结构
 - web.py  通过webapp2 + jinja 构建的web服务，为webmail提供web界面功能。
 - worker.py 延时发送邮件的background服务
 - service目录 提供消息队列、邮件发送等服务
 - static目录 提供css,js等静态资源
 - Procfile heroku的启动配置文件
 - requirements.txt pip安装依赖
 - docs目录 包含文档，自测报告
 
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

## 已知问题
- No.1 html editor对中文支持的问题，在mac chrome浏览器里面输入拼音，第一个字符无法输入。 状态：** 待解决 **
- No.2 Heroku 免费dyno会间歇性的idle,可能会导致服务不可用  状态: ** 待解决**
- No.3 未实现对附件的支持  状态:**待实现**  原因：稳定后有时间再实现。无技术瓶颈
- No.4 未实现定时重发  状态:**待实现**  原因：对heroku的dyno状态熟悉之后实现，实现此功能无技术瓶颈，预计需要2-3小时。现在因为dyno自身重启引起了一些问题导致暂停。