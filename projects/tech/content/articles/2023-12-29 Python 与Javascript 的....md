---
title: Python 的 `*` 与Javascript 的`...` ： 展开运算符的比较
slug: 
category: Code Learning
keywords: JavaScript 展开运算符, Python 星号运算符, JavaScript 和 Python 比较, 函数参数传递, 数组和对象操作, 编程技巧, DOM操作, 代码优化, Web开发技术
tags: javascript ,python,编程,展开运算符,编程语言比较,python 与 javascript 比较
date: 2023-12-29
created: 2023-12-29 19:36:11
modified: 2023-12-29 22:34:30
status: 
summary: 本文对比了JavaScript的展开运算符`...`与Python中的`*`和`**`运算符，重点介绍了它们在处理数组、对象和函数参数方面的不同用法。通过具体的代码示例，文章展示了如何在JavaScript和Python中使用这些运算符进行数据结构的展开和合并。
allDay: false
startTime: 19:30
endTime: 20:00
completed: null
---

## 1 解决一个实际问题

今天，在处理 DOM 操作时，我遇到了一个有趣的场景。问题出在我想要优化下面这段 JavaScript 代码时：

```javascript
if (bounding.top <= window.innerHeight * 0.2 && bounding.bottom >= 0) {
    document.querySelectorAll('#toc-list a').forEach(function(a) {
        a.classList.remove('font-bold', 'text-red-500');
        if (a.getAttribute('href') === '#' + id) {
            a.classList.add('font-bold', 'text-red-500');
            foundActive = true;
        }
    });
}
```

在这个代码块中，我发现 `classList.add` 和 `classList.remove` 方法都使用了相同的类，这意味着我需要在两个不同的地方维护同样的信息。为了提高代码的可维护性，我决定将这些类名提取到一个变量中。但是，我遇到了一个问题：当我尝试将包含空格的字符串 `'font-bold text-red-500'` 作为类名参数传递给 `classList.add` 和 `classList.remove` 方法时，它们无法按预期工作。

为了解决这个问题，我想到了两种方法：

### 方法一：使用数组和展开运算符

```javascript
let activeClasses = ['text-sky-500', 'font-bold'];

// 在函数中使用展开运算符
a.classList.remove(...activeClasses); // 移除多个类
if (a.getAttribute('href') === '#' + id) {
    a.classList.add(...activeClasses); // 添加多个类
}
```

### 方法二：使用字符串、split 和展开运算符

```javascript
let activeClass = 'text-sky-500 font-bold';

// 将字符串转换为数组，并使用展开运算符
a.classList.remove(...activeClass.split(' '));
if (a.getAttribute('href') === '#' + id) {
    a.classList.add(...activeClass.split(' '));
}
```

这个过程让我想到了 Python 中的 `*`，两者在功能上好像有些相似。

## 2 JavaScript 中的展开运算符 `...`

JavaScript 的展开运算符（`...`）是一个多功能且强大的工具。它不仅可以在函数调用中展开数组元素为单独的参数，还可以在数组和对象字面量中用于合并。

### 2.1 函数调用

在函数调用中，`...` 可以将数组元素展开为单独的参数。

```javascript
function sum(x, y, z) {
    return x + y + z;
}

const numbers = [1, 2, 3];
console.log(sum(...numbers));  // 输出: 6
```

### 2.2 数组和对象合并

`...` 运算符还可以用于数组和对象的合并操作。

```javascript
let arr1 = [1, 2];
let arr2 = [3, 4];
let mergedArr = [...arr1, ...arr2];  // 合并数组

let obj1 = { a: 1 };
let obj2 = { b: 2 };
let mergedObj = { ...obj1, ...obj2 };  // 合并对象
```

## 3 JavaScript 与 Python: 展开运算符的对比

实际上，将 Python 中的 `*` 和 `**` 两个运算符共同与 JavaScript 中的 `...` 运算符对比更为合理，因为 Python 的这两个运算符结合起来覆盖了 JavaScript 中 `...` 运算符的大部分功能。

### 3.1 Python 中的 `*` 和 `**` 运算符

1.**`*` 用于列表和元组**：在 Python 中，`*` 用于将列表或元组展开为单独的值，这在函数参数传递和列表解构中非常有用。

```python
# 合并列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]  # 结果: [1, 2, 3, 4, 5, 6]
```

```python
# 合并元组
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = (*tuple1, *tuple2)  # 结果: (1, 2, 3, 4, 5, 6)

```

2.**`**` 用于字典**：`**` 用于展开字典，将键值对作为单独的项展开，这在合并多个字典或将字典转换为函数的关键字参数时非常有用。

```python
# 合并字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### 3.2 JavaScript 中的 `...` 运算符

1. **数组和对象展开**：`...` 用于展开数组和对象中的元素或属性。
2. **函数参数**：同样可以将数组展开为函数的多个参数。
3. **解构赋值**：`...` 还被用于数组和对象的解构赋值。

```javascript
// 合并对象
let obj1 = { a: 1, b: 2 };
let obj2 = { c: 3, d: 4 };
let mergedObj = { ...obj1, ...obj2 };  // { a: 1, b: 2, c: 3, d: 4 }
```

### 3.3 对比总结

- 在处理数组和元组（或类似结构）方面，Python 的 `*` 与 JavaScript 的 `...` 类似。
- 在处理对象（字典）方面，Python 的 `**` 与 JavaScript 的 `...` 类似。
- JavaScript 的 `...` 提供了一种统一的方式来处理数组、对象和其它类型的数据，而 Python 则通过 `*` 和 `**` 分别处理不同类型的数据。

因此，Python 的 `*` 和 `**` 结合起来，确实在功能上与 JavaScript 的 `...` 有些相似。这两种语言虽然在语法和具体实现上有所不同，但在数据展开和合并的功能上有着类似的应用。
