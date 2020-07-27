from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from config.config import app,mysql
from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

user_api = Api(app)


class User(Resource):
    def post(self):
        """
        POST : To create user object.
        """
        try:
            args_data = request.get_json(force=True)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('CreateUser',unicode_to_str(args_data))
            cursor.callproc("LastRowEntry")
            data = cursor.fetchall()[0]
            cursor.close()
            conn.commit()
            if len(data)>0:
                usr = user_data_to_dict(data)
                return {'User':usr,'message':'User get created..'},201
            else:
                return {"message":str(data[0])},200          
        except Exception as e:
            return {'error': str(e)}
    def get(self,id = None):
        """
        GET  : It can be used.
            to get user object by id to get specific user.
            to get all users.
        """
        if (id == None):
            try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('GetAllUser')
                data = cursor.fetchall()
                users = []
                for user in data:
                    usr = user_data_to_dict(user)
                    users.append(usr)
                return {'Users':users},200
            except Exception as e:
                return {'error': str(e)}
        else:
            try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc("GetUserById",[id])
                data = cursor.fetchall()
                cursor.close()
                if len(data)>0:
                    user = user_data_to_dict(data[0])
                    return {'User':user},200
                else:
                    return {'StatusCode':'200','message':'User not found .. :< '}
            except Exception as e:
                return {'error': str(e)}
    def put(self,id=None):
        """
        PUT : It can be used to update user by id.
        """
        if id == None:
            return {'message':'Id not specified...'},400
        try:
            args_data = request.get_json(force=True) 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc("GetUserById",[id])
            data = cursor.fetchall()
            if len(data) > 0 :
                args_data = fill_all_field_in_arg(args_data,data)
                fname,lname,email,cno = args_data['first_name'],args_data['last_name'],args_data['email_id'],args_data['contact_no']
                args_data['id'] = id
                cursor.callproc("UpdateUserById",[id,fname,lname,email,cno])
                conn.commit()
                cursor.close()
                conn.close() 
                return {"message":"User get updated","User":args_data},200
            else:
                return {'StatusCode':'200', 'message':'User not found created..'}
        except Exception as e:
            return {'error': str(e)}
    def patch(self,id=None):
        """
        PATCH : It can be used to update user contact number.
        """
        if id == None:
            return {'message':'Id not specified...'},400
        try:
            args_data = request.get_json(force=True) 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc("GetUserById",[id])
            data = cursor.fetchall()
            if len(data) > 0 :
                cno = args_data['contact_no']
                args_data['id'] = id
                cursor.callproc("UpdateUserContactById",[id,cno])
                conn.commit()
                cursor.close()
                conn.close() 
                return {"message":"User get updated","User":{"contact_no":cno}},200
            else:
                return {'message':'User not found ...'},200
        except Exception as e:
            return {'error': str(e)}
    def delete(self,id=None):
        """
        DELETE : It can be used to delete user by id.
        """
        if id == None:
            return {'message':'Id not specified...'},400
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc("DeleteUserById",[id])
            conn.commit()
            cursor.close()
            return {'message':'User get Deleted...'},200
        except Exception as e:
            return {'error': str(e)}

user_api.add_resource(User, '/user','/user/<int:id>')