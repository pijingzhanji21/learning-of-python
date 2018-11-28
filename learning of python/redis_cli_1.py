'''redisÏûÏ¢¶©ÔÄ·½'''
import redis
pool=redis.ConnectionPool(host='localhost',port=6379)
r=redis.Redis(connection_pool=pool)
while True:
    task=r.brpop('task',0)
    print(r.llen('task'))
    print('current task %s'%task[1])