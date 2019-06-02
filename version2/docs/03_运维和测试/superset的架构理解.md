superset详解
>https://me.csdn.net/python_tty

权限分类

superset的权限基本上可以分为3类，菜单类，基本权限，资源类。superset在为角色添加权限的时候，添加的不是基本的权限而是权限和视图的组合。比如我想访问报表功能，视图是slicemodelview,权限是menu_access,需要把它们的组合 menu access on slicemodelview添加到我的角色当中
菜单类
flask appbuilder自己定义的控制菜单权限
menu_access
基本权限
基本权限有很多，类中的所有的加了@has_access|@has_access_api装饰器的方法都会生成基本权限
```python
can_list can_add can_csv

PERMISSION_PREFIX = 'can'


def has_access(f):
	if hasattr(f,"_permission_name"):
		permission_st = f._permission_name
	else:
		permission_str = f.__name__
	def wraps(self, *args, **kwargs):
		permission_str = PERMISSION_PREFIX 







```