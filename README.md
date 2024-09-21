# Task-Creator

![License](https://img.shields.io/badge/license-MIT-yellow) ![Language](https://img.shields.io/badge/language-python-brightgreen)

**Create Repeat Task with Notion API**

## 项目概述

### 需求

使用**Python**和**NotionAPI**，实现自动化在NotionDatabase中添加重复任务，例如课程表，以弥补Notion缺乏相关功能的不足

### 项目架构

项目包含如下模块

- 数据输入：利用JSON,CSV等导入任务数据
- 数据格式化：将输入的数据统一为NotionAPI兼容的数据格式
- 数据上传：将数据上传至Notion
  - 获取数据库属性
  - 根据获取的属性上传相关数据

### 使用的库

Requests

## 更新日志

### Version 0

#### V 0.1

上传时间：2024年3月1日21点19分

- 撰写项目文档，编制开发计划
- 编写了数据库获取和数据上传部分的代码`QueryAndUpdateNotionDatabase.py`

#### V 0.2

上传时间：2024年3月3日15：32分

完成了针对树维教务的课表自动化添加

## 开发计划

### Version 0

从创建课程表出发，编写各个模块并分别进行测试

### Version 1 

合并各个模块，清除个人信息后将库公开

### Version 2 

改进数据输入方式，扩展使用范围，开发图形化界面

## 程序结构

程序输入：通过控制台获得的课表的JSON数据

程序输出：Notion数据库

定义如下名词：

- Course

