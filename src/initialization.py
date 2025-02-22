from dbsetup import *
from logsetup import *
from network_failures import *
from customer_complaints import *

logger.info("--- INITIALIZATION ---")
db, cur = get_connection()
database_initialization()
logger.info("Database initialized")
train_nf_model(FEATURES, TARGET)
logger.info("Network Failures model trained")
train_cc_model()
logger.info("Customer Complaints model trained")
logger.info("----------------------")