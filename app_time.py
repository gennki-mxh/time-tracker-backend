from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app) # 相当于给所有网页发一张通行证

# 1. 写一个 POST 接口，用来接收数据并存入数据库
@app.route('/api/time', methods=['POST'])
def add_time_record():
    # 获取前端发来的 JSON 数据
    data = request.json
    sleep_h = data.get('sleep', 0)
    study_h = data.get('study', 0)
    fun_h = data.get('fun', 0)
    sport_h = data.get('sport', 0)

    # 数据校验逻辑
    if sleep_h < 0 or study_h < 0 or fun_h < 0 or sport_h < 0:
        return jsonify({"status": "error", "msg": "时间不能为负数！"}), 400

    try:
        # 连接 MySQL 数据库（记得把这里的密码换成你自己的）
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='admin',  # <--- 修改这里！！！
            database='test_db'
        )
        cursor = connection.cursor()

        # 执行插入语句
        sql = "INSERT INTO time_records (sleep_hours, study_hours, fun_hours, sport_hours) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (sleep_h, study_h, fun_h, sport_h))
        
        # 提交事务（没有这一句，数据存不进数据库）
        connection.commit()
        connection.close()

        return jsonify({"status": "success", "msg": "时间数据已成功存入数据库！"})

    except Exception as e:
        return jsonify({"status": "error", "msg": f"数据库报错了: {str(e)}"})

# 2. 新增 GET 接口：获取所有时间记录
@app.route('/api/time', methods=['GET'])
def get_all_time_records():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='admin',  # <--- 修改这里！！！
            database='test_db'
        )
        
        # 这里要用 DictCursor，这样查询出来的每行数据都是一个字典（带字段名），方便转 JSON
        cursor = connection.cursor(pymysql.cursors.DictCursor) 
        
        sql = "SELECT * FROM time_records ORDER BY id DESC" # 按 id 倒序，最新存的排前面
        cursor.execute(sql)
        
        # 获取所有结果
        results = cursor.fetchall()
        connection.close()

        # 将字典列表直接返回，jsonify 会自动把它变成标准的 JSON 格式
        return jsonify({
            "status": "success",
            "total": len(results),
            "data": results
        })

    except Exception as e:
        return jsonify({"status": "error", "msg": f"查询报错: {str(e)}"})

# 3. 新增 DELETE 接口：根据 id 删除某条记录
@app.route('/api/time/<int:record_id>', methods=['DELETE'])
def delete_time_record(record_id):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='admin', # <--- 记得保留你的密码
            database='test_db'
        )
        cursor = connection.cursor()
        
        # 执行删除语句（这里的 %s 是安全传参，防止 SQL 注入）
        sql = "DELETE FROM time_records WHERE id = %s"
        cursor.execute(sql, (record_id,))
        connection.commit()
        
        # 判断是否真的删除了数据
        if cursor.rowcount == 0:
            return jsonify({"status": "error", "msg": f"找不到 id 为 {record_id} 的记录"}), 404

        connection.close()
        return jsonify({"status": "success", "msg": f"成功删除 id 为 {record_id} 的记录！"})

    except Exception as e:
        return jsonify({"status": "error", "msg": f"删除报错: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)