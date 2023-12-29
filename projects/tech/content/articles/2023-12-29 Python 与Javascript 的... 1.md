---
title: 
slug: 
category: 
keywords: 
tags: 
date: 
created: 2023-12-29 21:46:56
modified: 2023-12-29 21:55:26
status: 
summary: 
---

## 1 一个小问题

今天遇到了这么一个场景，

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

这里面 remove 与 add 使用了同样的类，测试颜色不断修改时要改两个地方，所以我想把它们提出来放到变量里。比如，

```javascript
let activeClasses = 'text-sky-500 font-bold';

...
        a.classList.remove(activeClasses); // 移除多个类
        if (a.getAttribute('href') === '#' + id) {
            a.classList.add(activeClasses); // 添加多个类
            foundActive = true;
        }
    });
}
```

但是却发现不起作用。

原来这有些想当然， 此时传给 `classList.add` 和 `classList.remove` 方法的实际是一个**包含多个类名和空格的字符串**，而这两个方法预期接收的是**单个字符串（类名）或者多个单独的字符串（类名）参数**。当我尝试传递一个包含空格的字符串（如 `'text-sky-500 font-bold'`）时，它们不能正确地解析和应用这些类。

所以我现在有两个方法，要么传入一个列表，使用...解包，

```javascript
let activeClasses = ['text-sky-500', 'font-bold'];

...
        a.classList.remove(...activeClasses); // 移除多个类
        if (a.getAttribute('href') === '#' + id) {
            a.classList.add(...activeClasses); // 添加多个类
            foundActive = true;
        }
    });
}
```

要么还是传入这个带有多个类名和空格字符串，先 split，再解包，

```javascript
let activeClass = 'text-sky-500 font-bold';

if (bounding.top <= window.innerHeight * 0.2 && bounding.bottom >= 0) {
...
        // 使用 split 方法将字符串转换为数组，并使用展开运算符应用类名
        a.classList.remove(...activeClass.split(' '));
        if (a.getAttribute('href') === '#' + id) {
            a.classList.add(...activeClass.split(' '));
            foundActive = true;
        }
    });
}
```

这种情况下实际就是将带空格的字符串先根据空格分成了含有两个字符串的列表，再用...解包。分成两步看就是，

```javascript
let activeClass = 'text-sky-500 font-bold';
let classes = activeClass.split(' '); // ['text-sky-500', 'font-bold']

// 使用展开运算符将数组中的每个元素作为单独的参数传递
element.classList.add(...classes); // 等同于 element.classList.add('text-sky-500', 'font-bold');
```

[字符串的引号]() 有时对我们这些初学者会造成很大的困扰，不知道什么时候有，什么时候没了。我觉得可能得理解两个内容，一个是字面量，一个是 js 里的引号与 html 里的引号的区别。

## 2 展开运算符 `...`

在 JavaScript 中，`...` 是一个展开运算符（Spread Operator）。它用于将一个数组或类数组对象的所有元素“展开”成单独的项。在上面的情况下，当使用在 `activeClass.split(' ')` 返回的数组上时，它将数组中的每个元素（这里是类名）展开为单独的参数。

### 2.1 在 `classList.add` 和 `classList.remove` 中使用展开运算符

当 `activeClass` 字符串被 `split` 方法分割成数组后，数组中的每个元素是一个单独的类名。在调用 `classList.add` 或 `classList.remove` 方法时，您需要将这些类名作为单独的参数传递。这是展开运算符发挥作用的地方：

```javascript
let activeClass = 'text-sky-500 font-bold';
let classes = activeClass.split(' '); // ['text-sky-500', 'font-bold']

// 使用展开运算符将数组中的每个元素作为单独的参数传递
element.classList.add(...classes); // 等同于 element.classList.add('text-sky-500', 'font-bold');
```

### 2.2 展开运算符的其他用途

展开运算符在其他场景中也很有用，例如：

1.**在函数调用中**：将数组元素作为单独的参数传递给函数。

```javascript
function sum(x, y, z) {
 return x + y + z;
}

const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 输出 6
```

2.**在数组字面量中**：创建新数组时，将已有数组的元素包含进来。

```javascript
let parts = ['shoulders', 'knees'];
let body = ['head', ...parts, 'toes']; // ['head', 'shoulders', 'knees', 'toes']
```

3.**与对象字面量一起使用**：用于复制或合并对象。

```javascript
let obj1 = { foo: 'bar', x: 42 };
let obj2 = { foo: 'baz', y: 13 };
let clonedObj = { ...obj1 }; // { foo: 'bar', x: 42 }
let mergedObj = { ...obj1, ...obj2 }; // { foo: 'baz', x: 42, y: 13 }
```

展开运算符用于确保 `classList.add` 和 `classList.remove` 方法能够接收多个类名作为单独的参数，这对于动态地添加或移除元素上的多个类至关重要。

## 3 Javascript 里的 `...` 与 Python 里的 `*`

使用 `...` 解包让我想到 python 里的 `*`，作用都是解包，很多不同。`*` 的作用好像比较受限，只能用在函数里解包，而 `...` 的范围则广的多，几乎不受限制。

### 3.1 Python 中的展开运算符

- **函数调用**：在 Python 中，展开运算符 `*` 主要用于函数调用时，将列表或元组中的元素展开为单独的参数。

```python
def sum(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
print(sum(*numbers))  # 展开列表作为单独参数
```

- **限制**：Python 的 `*` 展开运算符**仅限于**这种情况，不能在像数组字面量或对象字面量中使用。

### 3.2 JavaScript 中的展开运算符

- **函数调用**：JavaScript 中的展开运算符 `...` 可以用于函数调用，与 Python 类似。

```javascript
function sum(a, b, c) {
  return a + b + c;
}

let numbers = [1, 2, 3];
console.log(sum(...numbers));  // 展开数组作为单独参数
```

- **数组和对象字面量**：在 JavaScript 中，`...` 还可以用于数组和对象字面量，用于合并数组或对象。

```javascript
let arr1 = [1, 2];
let arr2 = [3, 4];
let mergedArr = [...arr1, ...arr2];  // 合并数组

let obj1 = { a: 1 };
let obj2 = { b: 2 };
let mergedObj = { ...obj1, ...obj2 };  // 合并对象
```

### 3.3 总结

- 在 Python 中，`*` 仅用于函数调用中将列表或元组展开为参数。
- 在 JavaScript 中，`...` 不仅可以在函数调用中展开数组，还可以在创建新的数组或对象时用于合并。
