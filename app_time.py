from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 1. 写一个 POST 接口，用来接收数据并存入数据库
@app.route('/api/time', methods=['POST'])
def add_time_record():
    # 获取前端发来的 JSON 数据
    data = request.json
    sleep_h = data.get('sleep', 0)
    study_h = data.get('study', 0)
    fun_h = data.get('fun', 0)
    sport_h = data.get('sport', 0)

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

if __name__ == '__main__':
    app.run(debug=True)