from kazoo.client import *
            
class Fans:
    def __init__(self, host='localhost'):
        server_list = host + ':' + str(2181)
        for i in range(1,3):
            server_list += (',' + host + ':' + str(2181+i))
        self.zk = KazooClient(server_list)
        self.zk.start()
        self.Node=list()
        self.mark=False
    def close(self):
        self.zk.close()
    def subscribe(self,path):
        old = self.zk.get_children(path)
        @self.zk.ChildrenWatch(path)
        def watch_children(children):
            newNode = list(set(children) - set(old))
            global Node,test
            if len(newNode) == 0: # Prevent the first time call
                return True
            self.Node=newNode[0]
            print(self.Node)
            self.mark=True
            return False # Stop watch
    def subscribe_result(self,path):
        result=self.zk.get(path+"/"+str(self.Node))[0].decode("utf-8")
        print(result)
        return (str(self.Node)+"\t"+result)
    def search(self,path):
        result=self.zk.get(path)[0].decode("utf-8")
        return result
    def Mark(self):
        return self.mark
    def Lock(self):
        self.mark=False
        
