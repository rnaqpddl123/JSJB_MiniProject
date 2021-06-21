from flask import *
from flask_jwt_extended import *

application = Flask(import_name = __name__)
application.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "I'M IML"
		)
jwt = JWTManager(application)

@application.route("/")
def test_test():
	return "<h1>Hello, I'm IML!</h1>"

#################################################
# 로그인 API 영역

admin_id = "1234"
admin_pw = "qwer"

@application.route("/login", methods=['POST'])
def login_proc():
	
	# 클라이언트로부터 요청된 값
	input_data = request.get_json()
	user_id = input_data['id']
	user_pw = input_data['pw']

	# 아이디, 비밀번호가 일치하는 경우
	if (user_id == admin_id and
		user_pw == admin_pw):
		return jsonify(
			result = "success",
			# 검증된 경우, access 토큰 반환
			access_token = create_access_token(identity = user_id,
											expires_delta = False)
		)
	
	# 아이디, 비밀번호가 일치하지 않는 경우
	else:
		return jsonify(
			result = "Invalid Params!"
		)

#################################################
# 회원 전용 API 영역
@application.route('/user_only', methods=["GET"])
@jwt_required
def user_only():
	cur_user = get_jwt_identity()
	if cur_user is None:
		return "User Only!"
	else:
		return "Hi!," + cur_user

if __name__ == '__main__':
	application.run(host = '0.0.0.0',
					port = 5000, 
					debug = True)