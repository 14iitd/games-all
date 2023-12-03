from users.user_dao import UserDao
class UserService():
    def __init__(self):
        self.user_dao=UserDao()
    def get_user_by_device_id(self,device_id):
        return self.user_dao.get_user_by_device(device_id)
    def create_user(self,user_request_data):
        new_user =  self.user_dao.create_user(user_request_data)
        return new_user

