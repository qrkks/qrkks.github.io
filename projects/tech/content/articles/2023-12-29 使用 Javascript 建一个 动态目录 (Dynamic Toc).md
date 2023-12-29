---
title: 使用 Javascript, tailwind css 建一个动态目录 
slug: building-dynamic-toc-with-javascript
category: Pelican
keywords: pelican, nav, toc, dynamic toc, javascript, tailwind
tags: pelican, javascript, toc, nav, tailwind 
date: 2023-12-29
created: 2023-12-29 10:43:32
modified: 2023-12-29 15:51:31
status: draft
summary: 
allDay: false
startTime: 10:30
endTime: 11:00
completed: null
---

## 1 实现思路

1. 使用 tailwind 建一个目录的框架和样式。
2. 设置要生成目录的内容区，可以通过添加类名进行选择和反选。
3. 由 javascript 监听内容区提取标题加入到目录中，并监听滚动高亮正在显示的标题。
4. 监听点击。

## 2 Javascript 代码

```javascript
document.addEventListener("DOMContentLoaded", function() {
    // 获取TOC列表的容器
    var tocList = document.getElementById('toc-list');

    // 定义要选择的标题
    const headingSelector = "h1, h2, h3, h4, h5";

    // 选择指定容器内的标题元素
    var headings = document.querySelectorAll(".toc-content-area " + headingSelector);

    // 函数：更新TOC高亮状态
    function updateTocHighlight() {
        var foundActive = false;
        headings.forEach(function(node) {
            // 排除带有特定类（toc-exclude）的元素
            if (node.closest('.toc-exclude')) {
                return;
            }

            // 获取标题的位置
            var id = node.id;
            var bounding = node.getBoundingClientRect();

            // 判断标题是否在视窗内
            if (bounding.top <= window.innerHeight * 0.2 && bounding.bottom >= 0) {
                document.querySelectorAll('#toc-list a').forEach(function(a) {
                    a.classList.remove('font-bold', 'text-red-500');
                    if (a.getAttribute('href') === '#' + id) {
                        a.classList.add('font-bold', 'text-red-500');
                        foundActive = true;
                    }
                });
            }
        });
    }

    // 遍历所有标题元素，为它们创建TOC项
    headings.forEach(function(node) {
        if (node.closest('.toc-exclude')) {
            return;
        }

        var id = node.id || node.innerText.trim().toLowerCase().replace(/\s+/g, '-');
        node.id = id;

        // 根据标题级别计算左边距
        var level = parseInt(node.nodeName.substring(1)) - 1;
        var marginLeftClass = `ml-${level * 4}`;

        // 创建TOC项
        var listItem = document.createElement('li');
        listItem.innerHTML = `<a href="#${id}" class="text-blue-500 hover:text-blue-700 ${marginLeftClass}">${node.innerText}</a>`;

        // 为TOC项添加点击事件监听器
        listItem.querySelector('a').addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
            setTimeout(updateTocHighlight, 200); // 延迟更新高亮
        });

        tocList.appendChild(listItem);
    });

    // 监听滚动事件以更新TOC高亮
    window.addEventListener('scroll', updateTocHighlight);
});

```

## 3 详细解释

### 3.1 `getBoundingClientRect()`

`getBoundingClientRect()` 是一个 JavaScript DOM 方法，它返回一个 DOM 元素的大小及其相对于视口的位置。当这个方法应用于一个 DOM 节点时（比如一个 HTML 元素），它会提供该元素的 `top`, `bottom`, `left`, `right`, `width`, 和 `height` 等属性。

在我们的动态目录（TOC）的上下文中，`getBoundingClientRect()` 被用来确定一个标题元素在当前视口中的位置。这是非常重要的，因为它允许脚本知道用户当前查看的是哪部分内容。

#### 3.1.1 代码示例解释

```javascript
var bounding = node.getBoundingClientRect();
```

在这行代码中：

- `node` 代表一个标题元素（如 `h1`, `h2`, `h3` 等）。
- `getBoundingClientRect()` 对该元素调用，返回一个包含该元素位置和尺寸的对象。
- `bounding` 变量现在包含了元素的位置信息。

#### 3.1.2 如何使用这些信息

- `bounding.top`: 元素顶部相对于视口顶部的距离。如果这个值小于或等于 0，意味着元素的顶部已经滚动到视口顶部或以上。
- `bounding.bottom`: 元素底部相对于视口顶部的距离。如果这个值大于视口的高度，意味着元素的底部还没有进入视口。

这些信息被用来判断一个标题是否在当前视口内，从而决定是否将对应的 TOC 项设置为“活动”状态，这通常通过改变样式（如高亮）来实现。

#### 3.1.3 `getBoundingClientRect` 方法的字面意思

`getBoundingClientRect` 方法的字面意思可以分为两部分：

1. **Bounding**: 在这个上下文中，"bounding" 通常指的是一个边界框（bounding box）或外围矩形（bounding rectangle）。这个边界框是围绕着元素最小的矩形，包含了元素的全部可视部分，包括边框、滚动条等。
2. **ClientRect**: "ClientRect" 指的是客户端区域（client area），在浏览器中通常指的是浏览器视口（viewport）的区域。这个区域不包括浏览器的界面元素（如地址栏、工具栏等），只包括网页内容显示的部分。
3.  "Rect" 在 `getBoundingClientRect` 方法中是 "rectangle"（矩形）的缩写。在计算机图形学和 Web 开发中，矩形通常用来描述一个元素或区域的形状和大小，它由两个坐标（通常是左上角和右下角）或者一个坐标加上宽度和高度来定义。

所以，`getBoundingClientRect` 方法的名字表示它返回一个元素在客户端区域（即视口）内的边界框信息。这个信息包括元素的位置（相对于视口的左上角）和尺寸（宽度和高度）。

#### 3.1.4 小结

实际上就是获取客户端方块的意思，返回的与 **两个“方块”（或矩形）** 相关的信息：

1. **元素本身的方块**：这指的是元素的外围边界框。这个矩形框定义了元素的尺寸，包括其宽度（`width`）和高度（`height`）。
2. **元素相对于视口的位置**：这些信息表示元素的边界框相对于浏览器视口（屏幕上可见区域）的位置。它包括元素顶部（`top`）、底部（`bottom`）、左侧（`left`）和右侧（`right`）距离视口顶部和左侧的距离。

总结来说，`getBoundingClientRect` 方法提供了**一个元素在页面上的几何信息，这包括它的大小和它相对于当前视口的位置**。这个方法在处理页面布局和交互时非常有用，特别是在需要确定元素是否在当前可视区域内，以及元素的确切位置时。