import socket,threading
UNCONNECT = "未连接"
CONNECT = "连接"
friends = {"a":"b","b":"a","c":"d","d":"c"}
class User(object):
    def __init__(self,ip_port,name,status,client_socket):
        self ip_port = ip_port
        self name = name
        self status = status
        self client_socket = client_socket
    def __eq__(self,other):
        return other.name = self.name

class UserManager(object):
    users_online = []
    def get_friends(self,current_user_name):
        for user in self.users_online:
            if(user_name ==friends[current_user_name]):
                return user
        return None
    def get_socket(self,qq):
        for socket_u in self.users_online:
            if(socket_u.client_socket == qq):
                return socket_u
        return None
    def login(self,adress,user_name,sockert):
        online_users=User(ip_port=adress[0]+":"+str(adress[1]),status=CONNECT,name=user_name,client_socket=socket)
        self.users_online.append(online_users)
        return online_users
    def is_online(self,current_name):
        for user in users_online:
            if(user == current_user):
                return True
        return False
user_manager_instance = UserManager()
sockets = []
class Server(object):
    def manage_user_connection(self):
        s=socket.socket()
        s.bind("0.0.0.0":8249)
        s.listen(11)
        while True:
            user_socket,address = s.accept()
            user_name = None
            user_name = user_socket.recv(1024)
            if(user_name):
                print(user_name)
            if(user_name):
                current_user = user_manager_instance.login(address,user_name.decode("utf-8"),user_socket)
            else:
                pass
            








