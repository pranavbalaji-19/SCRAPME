from dbsetup import *
from logsetup import logger
from network_failures import train_nf_model
from customer_complaints import train_cc_model

logger.info("--- INITIALIZATION ---")
db, cur = get_connection()
database_initialization()
logger.info("Database initialized")
train_nf_model()
logger.info("Network Failures model trained")
train_cc_model()
logger.info("Customer Complaints model trained")
logger.info("----------------------")