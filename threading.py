'''
python3中的多线程编程主要依靠threading模块。
threading.Thread方法可以接收两个参数, 第一个是target，一般指向函数名，第二个是args，需要向函数传递的参数。
对于创建的新线程，调用start()方法即可让其开始。我们还可以使用current_thread().name打印出当前线程的名字。

在python中，默认情况下主线程和子线程独立运行互不干涉。
如果希望让主线程等待子线程实现线程的同步，我们需要使用t.join()方法。
如果我们希望一个主线程结束时不再执行子线程，可以使用t.setDaemon(True)

一个进程所含的不同线程间共享内存，这就意味着任何一个变量都可以被任何一个线程修改，
因此线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
如果不同线程间有共享的变量，其中一个方法就是在修改前给其上一把锁lock，确保一次只有一个线程能修改它。
threading.lock()方法可以轻易实现对一个共享变量的锁定，修改完后release供其它线程使用。

另一种实现不同线程间数据共享的方法就是使用消息队列queue。
'''
'''
下例中创建了两个线程，一个负责生成，一个负责消费，所生成的产品存放在queue里，实现了不同线程间沟通。
'''
from queue import Queue
import random, threading, time

# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print("{} is producing {} to the queue!".format(self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())

# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print("{} is consuming {} in the queue.".format(self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())

def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')

if __name__ == '__main__':
    main()

'''
队列queue的put方法可以将一个对象obj放入队列中。如果队列已满，此方法将阻塞至队列有空间可用为止。
queue的get方法一次返回队列中的一个成员。如果队列为空，此方法将阻塞至队列中有成员可用为止。

queue同时还自带emtpy(), full()等方法来判断一个队列是否为空或已满，但是这些方法并不可靠，
因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。
'''
'''
Python多进程和多线程哪个快?

由于GIL的存在，很多人认为Python多进程编程更快，针对多核CPU，理论上来说也是采用多进程更能有效利用资源。

    对CPU密集型代码(比如循环计算) - 多进程效率更高
    对IO密集型代码(比如文件操作，网络爬虫) - 多线程效率更高。

为什么是这样呢？其实也不难理解。对于IO密集型操作，大部分消耗时间其实是等待时间，
在等待时间中CPU是不需要工作的，那你在此期间提供双CPU资源也是利用不上的，
相反对于CPU密集型代码，2个CPU干活肯定比一个CPU快很多。

为什么多线程会对IO密集型代码有用呢？因为python碰到等待会释放GIL供新的线程使用，实现了线程间的切换。
'''