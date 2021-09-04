import string
from django.core.exceptions import ValidationError



def not_include_rank(value):
    ranks = ['병장','상병','일병','이병']
    if len(value) == 2:
        if value == '상병' or value == '병장' or value =='일병' or value =='이병' or value =='하사' or value =='중사' or value =='상사' or value =='원사' or value =='소위' or value =='대위' or value =='중위' or value =='대위' or value =='소령' or value =='중령' or value =='대령':
            return False
        else:
            return True
    else:
        return True
        
def include_rank(value):
    if not_include_rank(value) == True:
        raise ValidationError("계급을 입력하세요!")
    
    
        
# 실습으로 완성해 주세요



# 실습으로 완성해 주세요


# 실습으로 완성해 주세요
def contains_number(value):
    for char in value:
        if char in string.digits:
            return True
    return False    

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8
        ):
            raise ValidationError("비밀번호는 8자 이상이어야 합니다")

    def get_help_text(self):
        return "비밀번호는 8자 이상이어야 합니다"
        
