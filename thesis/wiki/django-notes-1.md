#Django

##url  herf标签的使用
	http://www.yihaomen.com/article/python/355.htm

##Django的orm中get和filter的不同
	 get

	Returns the object matching the given lookup parameters, which should be in the format described in Field lookups.

	get() raises MultipleObjectsReturned if more than one object was found. The MultipleObjectsReturned exception is an attribute of the model class.

	get() raises a DoesNotExist exception if an object wasn’t found for the given parameters. This exception is also an attribute of the model class

	filter

	Returns a new QuerySet containing objects that do not match the given lookup parameters.

	The lookup parameters (**kwargs) should be in the format described in Field lookups below. Multiple parameters are joined via AND in the underlying SQL statement, and the whole thing is enclosed in a NOT().

	参考网址：http://www.tuicool.com/articles/bYruEvu
##用户登陆与注销
	Login

	在视图函数中可以使用login()方法去登陆一个用户，这个方法需要一个HttpRequest对象和一个User对象，login()函数把用户ID存在session里面（是用django的session框架，所以请确保启用了会话中间件），如果是手工登陆用户，请先条用authenticate()方法

	from django.contrib.auth import authenticate, login
	def my_view(request):
	  username = request.POST['username']
	  password = request.POST['password']
	  user = authenticate(username=username, password=password)
	  if user is not None:
	    if user.is_active:
	      login(request, user)
	      # Redirect to a success page.
	    else:
	      # Return a 'disabled account' error message
	  else:
	    # Return an 'invalid login' error message.	

	logout()

	去注销一个使用django.contrib.auth.login()方法登陆的用户，请使用在视图函数中使用django.contrib.auth.logout()方法注销，该方法需要一个HttpRequest对象并且没有返回值

	from django.contrib.auth import logout

	def logout_view(request):
	    logout(request)
	    # Redirect to a success page.

## django 多对多 多对一 一对一

	http://my.oschina.net/ankh2008/blog/159517?fromerr=sOxar6JE
	http://www.tuicool.com/articles/mmUrmu