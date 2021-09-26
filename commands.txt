>>> from main.models import Todo
>>> from todo in Todo.objects.all()
  File "<console>", line 1
    from todo in Todo.objects.all()
               ^
SyntaxError: invalid syntax
>>> for todo in Todo.objects.all():
...     print(todo)
... 
Buy grocery
>>> from datetime import datetime
>>> from datetime import timedelta
>>> today = datetime.now()
>>> today
datetime.datetime(2020, 5, 8, 15, 11, 34, 882759)
>>> tmrw = today + timedelta(days=1)
>>> tmrw
datetime.datetime(2020, 5, 9, 15, 11, 34, 882759)
>>> Todo.objects.create(title='Read the docs', description='Read the Django docs on models', due_date=tmrw)
<Todo: Read the docs>
>>> Todo.objects.count()
2
>>> last = Todo.objects.last()
>>> last
<Todo: Read the docs>
>>> last.title
'Read the docs'
>>> q = Todo.objects.all()
>>> q.query
<django.db.models.sql.query.Query object at 0x7f7d5a5e3ba8>
>>> print(q.query)
SELECT "main_todo"."id", "main_todo"."title", "main_todo"."due_date", "main_todo"."done", "main_todo"."description" FROM "main_todo"
>>> Todo.objects.filter(title = 'Read the docs')
<QuerySet [<Todo: Read the docs>]>
>>> Todo.objects.filter(title = 'Read the docs').count()
1
>>> Todo.objects.filter(title = 'Read the docs').delete()
(1, {'main.Todo': 1})
>>> Todo.objects.filter(title = 'Read the docs').count()
0
>>> first = Todo.objects.first()
>>> first.title = 'Buy laptop'
>>> first.save()
>>> Todo.objects.filter(title = 'Buy laptop').update(done=True)
1
