from dbsetup import get_connection, database_initialization
from logsetup import logger
from network_failures import *
from customer_complaints import *

db, cur = get_connection()
database_initialization()

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
        return "Error while validating user"

def check_network_failures(latency, packet_loss,signal_strength):
    try:
        severity = predict_severity(latency, packet_loss, signal_strength, FEATURES)
        cur.execute(
            f"INSERT INTO network_failures(latency, packet_loss, signal_strength, severity) VALUES ({latency}, {packet_loss}, {signal_strength}, '{severity}')"
        )
        logger.info(f"Network Failure severity predicted with severity: {severity}")
    except Exception as e: 
        logger.error(f"Error while checking network failures: {e}")

def check_customer_complaints(complaint):
    try:
        category = classify_complaint(complaint)
        cur.execute(
            f"INSERT INTO customer_complaints(complaint, category) VALUES ('{complaint}', '{category}')"
        )
        logger.info(f"Customer Complaint classified in category: {category}")
    except Exception as e:
        logger.error(f"Error while checking customer complaints: {e}")

def resolve_issues(type, details):
    try:
        cur.execute(
            f"INSERT INTO resolved_issues(type, details) VALUES ('{type}', '{details}')"
        )
        rid = cur.execute("SELECT MAX(rid) FROM resolved_issues").fetchone()[0]
        logger.info(f"An issue has been resolved. Check rid {rid} for more details.")
    except Exception as e:
        logger.error(f"Error while resolving issues: {e}")