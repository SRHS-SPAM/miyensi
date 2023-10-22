# 게임에서 사용할 캐릭터를 정의합니다
define a = Character("주인공")
define b = Character("...")

# 여기에서부터 게임이 시작합니다.
label start:
    "원하는 과를 선택해 주세요"
    menu :
        "설계과" :
            jump Bomipart
        "제어과" :
            jump kimfallpart
        "시스템과" :
            jump hanchungpart
        "군특성화" :
            jump sorapart
    return
label Bomipart:
    b "오늘 새로운 전학생이 왔습니다~"
    
    return
label kimfallpart:
    b "오늘 새로운 전학생이 왔습니다~"
    
    return
label hanchungpart:
    b "오늘 새로운 전학생이 왔습니다~"
    
    return
label sorapart:
    b "오늘 새로운 전학생이 왔습니다~"
    
    return
