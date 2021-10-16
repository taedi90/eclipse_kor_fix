
# karabiner 적용 경로 : ~/.config/karabiner/assets/complex_modifications

import fragments

# 한글 키
kor_keys = ['q','w','e','r','t','y','u','i','o','p','a','s','d',
            'f','g','h','j','k','l','z','x','c','v','b','n','m']

# 영문 키
eng_keys = ['q','w','e','r','t','y','u','i','o','p','a','s','d',
            'f','g','h','j','k','l','z','x','c','v','b','n','m']

# 한글 입력에 영향 주지 않는 키
escape_keys = ['1','2','3','4','5','6','7','8','9','0',
                'hyphen','equal_sign','grave_accent_and_tilde',
                'open_bracket','close_bracket','backslash','semicolon',
                'quote','comma','period','slash','spacebar']

# 한글 입력 직후 영향을 주거나 받는 키
affected_keys = ['return_or_enter','delete_or_backspace','left_control',
                    'left_option','left_command','tab']
affected_arrows = ['left_arrow','up_arrow','right_arrow','down_arrow']
affected_buttons = ['button1','button2','button3','button4','button5']

heldDownThreshold = '200' # 키 누름 반응속도, 너무 작게 입력하면 키가 중복입력됨





# json 텍스트 만들기
temp = [] # fragments 가 조합 될 리스트

temp.append(fragments.header) # header


temp_body = []
for i in kor_keys:
    temp_body.append(fragments.kor.replace('key_name', i))

for i in eng_keys:
    temp_body.append(fragments.eng.replace('key_name', i))

for i in escape_keys:
    temp_body.append(fragments.escape.replace('key_name', i))
    
for i in affected_arrows:
    temp_body.append(fragments.affected_arrow.replace('key_name', i))

for i in affected_keys:
    temp_body.append(fragments.affected_key.replace('key_name', i))

for i in affected_buttons:
    temp_body.append(fragments.affected_button.replace('key_name', i))
    
temp_body.append(fragments.rcmd_to_koreng) # r_cmd 버튼 한영키로 사용하지 않을 경우 설정안해도 됨

temp.append(','.join(temp_body)) # modification 간 ','로 구분


temp.append(fragments.footer) # footer


json = ''.join(temp).replace('heldDownThreshold', heldDownThreshold) # temp를 결합

# 파일로 변환
with open('eclipse_kor_fix.json', 'w', encoding="utf-8")as make_file:
        make_file.write(json)