# Time Tracker Backend

基于 Python Flask 和 MySQL 构建的个人时间管理系统后端 API 服务。用于接收、存储和分析个人的日常时间分配数据（睡眠、学习、娱乐、运动）。

## 🛠️ 技术栈

**语言**：Python 3

**Web 框架**：Flask

**数据库**：MySQL (通过 PyMySQL 驱动)

**开发工具**：VS Code / PyCharm / Git

**辅助工具**：DeepSeek (用于代码生成与 Bug 排错)

## ✨ 已实现功能

- [✔] 基础 Web 服务搭建与路由分发

- [✔] 接收前端 POST 请求，解析 JSON 数据

- [✔] 连接 MySQL 数据库，实现数据的持久化存储（Insert 操作）

- [✔] 增加 GET /api/time 接口

## 📂 项目结构

```text
time-tracker-backend/
├── .venv/               # 虚拟环境（已在 .gitignore 中忽略）
├── .gitignore           # Git 忽略文件配置
├── app_time.py          # Flask 核心应用与路由控制
├── test_api.py          # 本地测试 API 的 Python 脚本（可选）
└── README.md            # 项目说明文档
```

## 🚀 本地运行指南

### 1. 环境准备

确保你本地已安装 Python 3 和 MySQL。

### 2. 克隆项目并配置环境

```bash
# 克隆项目
git clone https://github.com/gennki-mxh/time-tracker-backend.git
cd time-tracker-backend

# 创建并激活虚拟环境
python -m venv .venv
# Windows 激活命令：
.venv\Scripts\activate
# Mac/Linux 激活命令：
source .venv/bin/activate

# 安装依赖
pip install flask pymysql
```

### 3. 数据库准备

在本地 MySQL 中执行以下 SQL 语句，创建数据库和数据表：

```sql
CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;

CREATE TABLE time_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sleep_hours FLOAT,
    study_hours FLOAT,
    fun_hours FLOAT,
    sport_hours FLOAT
);
```

### 4. 修改配置

打开 `app_time.py`，找到 `pymysql.connect` 部分，将 `password` 修改为你本地 MySQL 的真实密码。

### 5. 运行服务

```bash
python app_time.py
```

如果终端出现 `* Running on http://127.0.0.1:5000`，说明服务启动成功。

## 📡 API 接口文档

### 新增时间记录

- 接口地址：`/api/time`
- 请求方法：`POST`
- 请求头：`Content-Type: application/json`
- 请求参数：

| 参数名 | 类型  | 必填 | 描述             |
|--------|-------|------|------------------|
| sleep  | float | 是   | 睡眠时长（小时） |
| study  | float | 是   | 学习时长（小时） |
| fun    | float | 是   | 娱乐时长（小时） |
| sport  | float | 是   | 运动时长（小时） |

- 请求示例 (JSON)：

```json
{
    "sleep": 8,
    "study": 3,
    "fun": 2,
    "sport": 1
}
```

- 成功响应示例：

```json
{
    "status": "success",
    "msg": "时间数据已成功存入数据库！"
}
```

## 🗺️ 后续开发计划 (Roadmap)

- 增加 `GET /api/time` 接口，实现历史数据查询与分页
- 引入数据校验机制，防止非法字符或负数入库
- 增加 `flask-cors` 跨域配置
- 接入前端页面（HTML/CSS/JS），实现可视化数据看板
- 使用 Gunicorn + Nginx 部署到 Linux 服务器

---

*Created with ❤️ by [GennKi-梦心湖](https://github.com/gennki-mxh)*

```txt

---

### 💡 提交建议

1. 在 VS Code 里新建这个文件，保存。
2. 终端里跑一遍：
   ```bash
   git add README.md
   git commit -m "docs: 添加项目 README 说明文档"
   git push
    ```
