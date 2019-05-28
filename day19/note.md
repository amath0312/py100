# 迭代器与生成器

* 生成器仅在迭代至某个元素时才会将该元素放入内存，而在这之前或之后，元素可以不存在或者被销毁
* 列表解析[expr for iter_var in iterable if cond_expr]
* 生成器表达式(expr for iter_var in iterable if cond_expr)
* __iter__
* __next__
* yield