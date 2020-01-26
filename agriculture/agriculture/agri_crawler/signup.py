# 석빈이 소스 회원가입 부분
from .models import Signup
from django.shortcuts import render
class signUp():
    def __init__(self):
        self.result= 0
    def get(self):
        return render(request, 'vegetable/signup.html', {})

    def post(self, ID, password, email):
        person_info = Signup()
        person_info.ID = ID
        person_info.Email = email
        person_info.password = password
        person_info.save()
        '''if user_id is None or user_pw is None or user_email is None:
            return render(request, 'vegetable/signup.html', {})
        else:
            connection= models.Mongo()
            val = connection.Find_id_Mongo(user_id)
            if val ==1:
                return render(request, 'vegetable/signup.html',{})
            else:
                connection.Insert_info_Mongo(user_id, user_pw, user_name, user_email)
                return render(request, 'vegetable/login.html')
'''
'''
class logIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dblab/login_html',{})

    def post(self,request, *args, **kwargs):
        user_id =request.POST['login_id']
        user_pw = request.POST['login_pw']

        if(user_id is None or user_pw is None):
            return render(request, 'dblab/login.html',{})

        else:
            connection = models.Mongo()
            val1 = connection.Verify_id_Mongo(user_id)
            val2 = connection.Verify_id_pw_Mongo(user_id,user_pw)

            if val1 == 1:
                # 아이디와 비밀번호 모두 일치한다면
                if val2 == 1:
                    # 성공 출력 후 로그인
                    return HttpResponse("로그인성공")

                else:

                    return render(request, 'dblab/login.html', {})
                # 입력한 아이디가 존재하지 않는다면
            else:
                # 실패 출력 후 되돌아가기
'''
