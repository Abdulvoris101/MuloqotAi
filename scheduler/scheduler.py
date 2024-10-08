import schedule
import time
from rq import Queue
from redis import Redis
from tasks import cancelExpiredSubscriptions, unsetExpiredKeys
from apps.common.settings import settings

# Connect to Redis and create an RQ queue
redis_conn = Redis.from_url(settings.REDIS_URL)
rq_queue = Queue(connection=redis_conn)


schedule.every().day.at("00:00").do(rq_queue.enqueue, cancelExpiredSubscriptions)
schedule.every().day.at("20:00").do(rq_queue.enqueue, cancelExpiredSubscriptions)
schedule.every().day.at("19:00").do(rq_queue.enqueue, unsetExpiredKeys)

while True:
    schedule.run_pending()
    time.sleep(1)
