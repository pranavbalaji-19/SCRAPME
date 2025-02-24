from dbsetup import get_connection, database_initialization
from logsetup import logger
from network_failures import *
from customer_complaints import *
import time

db, cur = get_connection()
database_initialization()

def add_user(username, password, role):
    try:
        cur.execute(
            f"INSERT INTO users(username, password, level) VALUES ('{username}', '{password}', '{role}')"
        )
        db.commit()
        time.sleep(1)
        logger.info(f"User {username} added with role '{role}'")
        print(f"User {username} added with role '{role}'")
    except Exception as e:
        logger.error(f"Error while adding user: {e}")

def check_and_validate_user(username, password):
    try:
        cur.execute(
            f"SELECT * FROM users WHERE username = '{username}'"
        )
        result = cur.fetchall()
        if result==[]: return "User not found"
        if result[0][1] == password:
            logger.info(f"User {username} ({result[0][-1]}) logged in")
            return result[0][-1]
        return "Invalid password"
    except Exception as e:
        logger.error(f"Error while validating user: {e}")
        return f"Error while validating user: {e}"

def check_network_failures(latency, packet_loss,signal_strength):
    try:
        severity = predict_severity(latency, packet_loss, signal_strength, FEATURES)
        cur.execute(
            f"INSERT INTO network_failures(latency, packet_loss, signal_strength, severity) VALUES ({latency}, {packet_loss}, {signal_strength}, '{severity}')"
        )
        db.commit()
        time.sleep(1)
        logger.info(f"Network Failure predicted with severity: {severity}")
        print(f"Network Failure predicted with severity: {severity}")
    except Exception as e: 
        logger.error(f"Error while checking network failures: {e}")

def add_customer_complaints(username, complaint):
    try:
        category = classify_complaint(complaint)
        cur.execute(
            f'INSERT INTO customer_complaints(username, complaint, category) VALUES ("{username}", "{complaint}", "{category}")'
        )
        db.commit()
        time.sleep(1)
        logger.info(f"Customer Complaint classified in category: {category}")
        cur.execute("SELECT MAX(cid) FROM customer_complaints")
        cid = cur.fetchone()[0]
        print(f"Complaint registered successfully! Your complaint id: {cid}")
    except Exception as e:
        logger.error(f"Error while adding complaint: {e}")

def check_complaint_status(cid):
    try:
        cur.execute(
            f"SELECT cid FROM resolved_customer_issues WHERE cid = {cid}"
        )
        result = cur.fetchall()
        if result == []:
            print(f"Complaint {cid} is still pending.")
        else:
            print(f"Complaint {cid} has been resolved.")
        logger.info(f"Complaint {cid} status checked")
    except Exception as e:
        logger.error(f"Error while checking complaint status: {e}")

def resolve_network_issues(fid, details):
    try:
        cur.execute(
            f"INSERT INTO resolved_network_issues(details) VALUES ('{details}')"
        )
        db.commit()
        time.sleep(1)
        cur.execute("SELECT MAX(rid) FROM resolved_network_issues")
        rid = cur.fetchone()[0]
        logger.info(f"A network issue has been resolved. Check rid {rid} for more details.")
        print(f"A network issue has been resolved. Check rid {rid} for more details.")
    except Exception as e:
        logger.error(f"Error while resolving network issues: {e}")

def resolve_customer_issues(details):
    try:
        cur.execute(
            f"INSERT INTO resolved_customer_issues(details) VALUES ('{details}')"
        )
        db.commit()
        time.sleep(1)
        cur.execute("SELECT MAX(rid) FROM resolved_customer_issues")
        rid = cur.fetchone()[0]
        logger.info(f"A customer issue has been resolved. Check rid {rid} for more details.")
        print(f"A customer issue has been resolved. Check rid {rid} for more details.")
    except Exception as e:
        logger.error(f"Error while resolving issues: {e}")

def check_logs():
    try:
        with open(r"logs/logfile.log", "r") as f:
            lines = f.readlines()[-20:]
            print("\nRecent logs:\n")
            for line in lines:
                print(line)
        logger.info("Logs checked.")
    except Exception as e:
        logger.error(f"Error while checking logs: {e}")
