import mysql.connector as mycon

def get_connection():
    db = mycon.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="telecom_db"
    )

    cur = db.cursor()
    return db, cur

def database_initialization():
    db, cur = get_connection()
    cur.execute("CREATE DATABASE IF NOT EXISTS telecom_db;")

    cur.execute("USE telecom_db;")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users \
            (username VARCHAR(255) PRIMARY KEY, password VARCHAR(255), level ENUM('admin','customer'));"
    )

    cur.execute(
        "CREATE TABLE IF NOT EXISTS network_failures \
            (fid INT AUTO_INCREMENT PRIMARY KEY, latency INT, packet_loss DOUBLE, signal_strength INT, severity VARCHAR(8), failure_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    )

    cur.execute(
        "CREATE TABLE IF NOT EXISTS customer_complaints \
            (cid INT AUTO_INCREMENT PRIMARY KEY, complaint TEXT, category VARCHAR(30), complaint_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    )

    cur.execute(
        "CREATE TABLE IF NOT EXISTS resolved_issues \
            (rid INT AUTO_INCREMENT PRIMARY KEY, type ENUM('network','complaint'), details TEXT, resolved_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    )

    db.commit()
    cur.close()