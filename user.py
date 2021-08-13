from mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod 
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def create_user(cls, data):
        
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):

        query = "DELETE FROM users WHERE id = (%(id)s);"

        connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def get_single_user(cls, data):

        query = "SELECT * FROM users WHERE id = (%(id)s);"

        connectToMySQL('users_schema').query_db(query, data)
        
        # user_data = {
        #     'id': results[0]['id'],
        #     'first_name': results[0]['first_name'],
        #     'last_name': results[0]['last_name'],
        #     'email': results[0]['email'],
        #     'created_at': results[0]['created_at'],
        #     'updated_at': results[0]['updated_at'],
        # }

        # return user_data

    @classmethod
    def edit_user(cls, data):

        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, user_id = %(id)s;'

        connectToMySQL('users_schema').query_db(query, data)