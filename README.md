# 🩺 医疗数据伪造工具

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License: Apache](https://img.shields.io/badge/license-Apache%202.0-green)
![Status: Experimental](https://img.shields.io/badge/status-experimental-yellow)

---

> **⚠️ 免责声明：本项目仅供学习和研究，严禁用于任何非法用途！请遵守当地法律法规，作者不承担任何违法责任。**

---

## 📑 目录

- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [项目结构](#项目结构)
- [配置说明](#配置说明)
- [API参数获取指南](#api参数获取指南)
- [常见问题](#常见问题)
- [贡献与许可](#贡献与许可)

---

## 📝 项目简介

本项目旨在协助某些无良志愿服务提供方（如部分养老院）快速伪造医疗数据。主要功能包括体征数据生成与自定义参数配置，支持第三方 API 对接。**请勿用于任何违法或不道德场景！**

---

## 🚀 快速开始

1. **克隆项目**
   ```bash
   git clone https://github.com/Bolin42/Python.git
   cd Python
   ```

2. **配置参数**
   - 编辑 `settings.ini`，设置体征数据范围限制。
   - 在 `main.py` 主入口，填写你的 API 地址和密钥。

3. **运行主程序**
   ```bash
   python main.py
   ```

---

## 🗂️ 项目结构

```text
├── main.py          # 项目主入口，修改API相关参数
├── settings.ini     # 体征限制参数配置
├── README.md        # 项目说明文档
└── ...              # 其他辅助文件
```

---

## ⚙️ 配置说明

- **settings.ini**  
  体征参数限制配置文件，按需调整生成数据的范围。

  ```ini
  [Vitals]
  heart_rate_min = 60
  heart_rate_max = 100
  # 更多参数...
  ```

- **main.py**  
  主程序入口，请自行在`main`函数内修改API密钥及地址。  
  **获取API参数方法：**  
  使用浏览器开发者工具抓取目标平台的请求/响应包，提取密钥和地址。
  **相关填写位置**
在 `main.py` 中，API地址和密钥需要在以下位置填写：

---

### 1. 主要填写函数

#### （1）put_request函数
- **行数：第33行附近**
- **函数名：put_request**
- **API地址：**
  ```python
  url = "https://xn--l6qy95a.fun/baseData/signs/general/add?time="+timestamp
  ```
- **API密钥：**
  ```python
  headers = {
      ...
      'Authorization': 'Bearer '   # 此处需填写真实密钥字符串
      ...
  }
  ```
- **说明：**  
  请将 `'Authorization': 'Bearer '` 替换为 `'Authorization': 'Bearer <你的密钥>'`。

#### （2）get_start_date函数
- **行数：第64行附近**
- **函数名：get_start_date**
- **API地址：**
  ```python
  url = "https://xn--l6qy95a.fun/baseData/signs/general/page?objectCode="+objectCode+"&branchId=23&current=1&size=1&time=" + timestamp
  ```
- **API密钥：**
  ```python
  headers = {
      ...
      'Authorization': 'Bearer'  # 此处需填写真实密钥字符串
      ...
  }
  ```
- **说明：**  
  请将 `'Authorization': 'Bearer'` 替换为 `'Authorization': 'Bearer <你的密钥>'`。

#### （3）get_stuff_ID函数
- **行数：第96行附近**
- **函数名：get_stuff_ID**
- **API地址：**
  ```python
  url = "https://xn--l6qy95a.fun/baseData/data/elderList?elderNameAndNo="+elderNameAndNo+"&size=1&type=all&time="+timestamp
  ```
- **API密钥：**
  ```python
  headers = {
      ...
      'Authorization': 'Bearer '  # 此处需填写真实密钥字符串
      ...
  }
  ```
- **说明：**  
  请将 `'Authorization': 'Bearer '` 替换为 `'Authorization': 'Bearer <你的密钥>'`。

---

**所有 API 地址均为以 `https://xn--l6qy95a.fun/` 开头的相关路径，密钥填写方式均为 headers 字典内的 `'Authorization': 'Bearer <你的密钥>'`。**
---

## 🧭 API参数获取指南

1. 打开目标平台网页，按`F12`启动开发者工具。
2. 切换到`Network`面板，执行相关操作，筛选出请求包。
3. 查看请求详情，复制API地址及密钥等参数。
4. 填写至`main.py`对应位置。

---

## ❓ 常见问题

- **Q:** 运行报错怎么办？  
  **A:** 检查Python版本、API参数填写是否正确、settings.ini格式是否规范。

- **Q:** 如何扩展体征类型？  
  **A:** 在`settings.ini`添加新参数，并在`main.py`补充相关处理逻辑。

---

## 🙏 贡献与许可

- 欢迎提出建议或贡献代码，但请严格遵守合法合规原则。
- **本项目不鼓励任何违法用途！**

---

> **⚠️ 免责声明：本工具仅限技术交流，禁止用于非法用途。任何滥用行为，后果自负，作者不承担任何责任。**