import random
import asyncio
from pyscript import document

# 수도 데이터 (더 추가 가능)
CAPITALS = {
    "한국": "서울", "일본": "도쿄", "중국": "베이징", "미국": "워싱턴",
    "영국": "런던", "프랑스": "파리", "독일": "베를린", "이탈리아": "로마",
    "인도네시아": "자카르타", "인도": "뉴델리", "브라질": "브라질리아",
    "캐나다": "오타와", "호주": "캔버라", "러시아": "모스크바"
}

current_country = ""
score = 0

def get_new_question():
    global current_country
    current_country = random.choice(list(CAPITALS.keys()))
    
    # UI 업데이트
    document.querySelector("#question").innerText = f"{current_country}의 수도는?"
    document.querySelector("#answer").value = ""
    document.querySelector("#result").innerText = ""

async def next_round():
    await asyncio.sleep(1.5)
    get_new_question()

def check_answer(event):
    global score
    user_input = document.querySelector("#answer").value.strip()
    result_element = document.querySelector("#result")
    
    if user_input == CAPITALS[current_country]:
        result_element.innerText = "✅ 정답입니다!"
        result_element.style.color = "#00b894"
        score += 1
        document.querySelector("#score-val").innerText = str(score)
        # 비동기로 다음 문제 호출
        asyncio.create_task(next_round())
    else:
        result_element.innerText = f"❌ 틀렸습니다. 정답은 {CAPITALS[current_country]}입니다."
        result_element.style.color = "#d63031"

# 게임 시작
get_new_question()
