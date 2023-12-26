---
title: Tailwind CSS 中 Grid 的使用
slug: 
date: 2023-12-25 20:09:39
modified: 2023-12-26 10:40:55
category: 
tags: tailwind css
summary:  讨论Tailwind CSS 中的 Grid 的使用，三步走：先定义是个grid，然后定义有几行几列，然后再定义有没有跨行。
---

## 基本用法

Tailwind CSS 是一个功能类优先的 CSS 框架，它提供了一组预先定义的类，用于快速构建响应式布局。在 Tailwind 中，网格布局是通过一系列的工具类来实现的，这些类基于 CSS Grid Layout。以下是 Tailwind Grid 的基本用法：

1.**创建一个网格容器**：首先，你需要创建一个网格容器。这可以通过使用 `grid` 类来实现。

```html
<div class="grid">
 <!-- 网格项 -->
</div>
```

2.**定义列**：使用 `grid-cols-{n}` 类来定义列的数量。例如，`grid-cols-3` 将创建三列的网格。

```html
<div class="grid grid-cols-3">
 <div>1</div>
 <div>2</div>
 <div>3</div>
</div>
```

<div class="grid grid-cols-3">
	<div class="bg-blue-500">1</div>
	<div class="bg-gray-300">2</div>
	<div class="bg-yellow-400">3</div>
</div>

3.**间距**：可以使用 `gap-{size}` 类来定义行与列之间的间距。例如，`gap-4` 会在行与列之间添加一定的空间。

```html
<div class="grid grid-cols-3 gap-4">
 <div>1</div>
 <div>2</div>
 <div>3</div>
</div>
```

<div class="grid grid-cols-3 gap-4">
	<div class="bg-blue-500">1</div>
	<div class="bg-gray-300">2</div>
	<div class="bg-yellow-400">3</div>
</div>

4.**响应式设计**：Tailwind 提供了基于不同断点的响应式类。例如，`md:grid-cols-2` 会在中等尺寸的屏幕上将网格设置为两列。

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
 <div>1</div>
 <div>2</div>
 <div>3</div>
</div>
```

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
	<div class="bg-blue-500">1</div>
	<div class="bg-gray-300">2</div>
	<div class="bg-yellow-400">3</div>
</div>

5.**对齐和定位**：你可以使用 `justify-items-{alignment}`, `align-items-{alignment}`, `justify-content-{alignment}` 和 `align-content-{alignment}` 类来控制子项的对齐和定位。

```html
<div class="grid grid-cols-3 justify-items-center">
 <div>1</div>
 <div>2</div>
 <div>3</div>
</div>
```

<div class="grid grid-cols-3 justify-items-center">
	<div class="bg-blue-500">1</div>
	<div class="bg-gray-300">2</div>
	<div class="bg-yellow-400">3</div>
</div>

6.**网格行**：类似于列，你也可以使用 `grid-rows-{n}` 来定义行数。

Tailwind 的这种方法极大地简化了 CSS Grid 的使用，并使得创建响应式布局变得非常快捷和直观。记得要根据你的项目需求和设计选择合适的类。

## 添加跨度

在 Tailwind CSS 中，使用 `span` 类可以控制网格项(grid items)跨越多少列（column-span）或行（row-span）。这是实现更复杂网格布局的关键部分，允许你定义某个网格项应该占据的空间大小。

### 列跨度（Column Span）

- **使用 `col-span-{n}` 类**：这个类用于定义一个网格项应跨越多少列。例如，`col-span-2` 表示网格项将跨越两列。

```html
<div class="grid grid-cols-4">
	<div class="col-span-2">1</div> <!-- 此项跨两列 -->
	<div>2</div>
	<div>3</div>
</div>
```

<div class="grid grid-cols-4">
	<div class="col-span-2 bg-green-400">1</div> <!-- 此项跨两列 -->
	<div class="bg-blue-500">2</div>
	<div class="bg-gray-300">3</div>
</div>

### 行跨度（Row Span）

- **使用 `row-span-{n}` 类**：与列跨度类似，行跨度类定义一个网格项应跨越多少行。例如，`row-span-3` 表示网格项将跨越三行。

```html
<div class="grid grid-cols-3 grid-rows-3">
	<div class="row-span-2">1</div> <!-- 此项跨两行 -->
	<div>2</div>
	<div>3</div>
	<div>4</div>
</div>
```

<div class="grid grid-cols-3 grid-rows-3 ">
	<div class="row-span-2 bg-green-500">1</div> <!-- 此项跨两行 -->
	<div class="bg-blue-500">2</div>
	<div class="bg-gray-300">3</div>
	<div class="bg-yellow-400">4</div>
</div>

### 响应式设计

与其他 Tailwind 类一样，列跨度和行跨度也可以结合响应式前缀来使用，以适应不同屏幕尺寸。

- **响应式跨度**：例如，`md:col-span-2` 表示在中等尺寸屏幕上，元素将跨越两列。

```html
<div class="grid grid-cols-3">
	<div class="col-span-1 md:col-span-2">1</div> <!-- 小屏占一列，中屏占两列 -->
	<div>2</div>
	<div>3</div>
</div>
```

<div class="grid grid-cols-3 ">
	<div class="col-span-1 bg-green-400 md:col-span-2">1</div> <!-- 小屏占一列，中屏占两列 -->
	<div class="bg-blue-500">2</div>
	<div class="bg-gray-300">3</div>
</div>

使用这些类，你可以灵活地定义网格布局中各项的大小和位置，从而创建出既美观又响应式的布局设计。

## 总结

在使用 Tailwind CSS 创建网格布局时，通常遵循以下步骤：

1. **定义网格容器**：首先，通过使用 `grid` 类将一个元素定义为网格容器。
2. **设定行和列的数量**：接下来，使用 `grid-cols-{n}` 和 `grid-rows-{n}` 类来定义网格的列数和行数。例如，`grid-cols-3` 创建三列，而 `grid-rows-2` 创建两行。
3. **决定跨行或跨列**：然后，你可以为网格中的项（子元素）指定它们应该跨越的行数或列数。这是通过 `col-span-{n}` 和 `row-span-{n}` 类来实现的。例如，`col-span-2` 表示一个网格项将跨越两列。
4. **调整间隙和对齐**：此外，你还可以使用 `gap-{size}`、`justify-items-{alignment}`、`align-items-{alignment}` 等类来调整网格项之间的间距和对齐方式。
5. **添加响应式设计**：最后，可以结合使用响应式前缀（如 `md:`, `lg:`）来调整不同屏幕尺寸下的网格布局。

通过这些步骤，你可以灵活地创建各种网格布局，从简单的均匀网格到复杂的跨行或跨列布局，都可以用 Tailwind CSS 快速实现。
