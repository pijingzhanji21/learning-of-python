'''redis消息订阅发布端'''
import  redis,json
pool=redis.ConnectionPool(host='localhost',port=6379)
r=redis.Redis(connection_pool=pool)
q=r.pubsub()
q.subscribe('task')
for i in q.listen():
    if i['type']=='message':
        print('recv task:%s'%i['data'].decode())
        if i['data'].decode()=='over':
            print('task is stop')
            break
q.unsubscribe('task')
print('qu xiao dingyu')
