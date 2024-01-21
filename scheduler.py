import schedule
import time
from rq import Queue
from redis import Redis
from utils import constants
import tasks

# Connect to Redis and create an RQ queue
redis_conn = Redis.from_url(constants.REDIS_URL)
rq_queue = Queue(connection=redis_conn)


schedule.every().day.at("00:00").do(rq_queue.enqueue, tasks.cancelExpiredSubscriptions)
schedule.every().day.at("00:00").do(rq_queue.enqueue, tasks.clearAllTodaysMessages)
schedule.every().day.at("19:00").do(rq_queue.enqueue, tasks.unsetExpiredKeys)

while True:
    schedule.run_pending()
    time.sleep(1)
