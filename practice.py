import datetime

travel = input("여행출발일이 올해 인가요 (Yes/No): ").strip().lower()

if travel == "yes":
  year = datetime.datetime.now().year
elif travel == "no":
  while True:
    try:
      year = int(input("그럼 몇 년도인가요? (예: 2027): "))
      break
    except ValueError:
      print("숫자로 정확히 입력해주세요.")
else:
  print("Yes or No로 정확히 입력해주세요")
  exit() 
  

month = int(input("몇달의 출발 하나요(숫자만): "))
day = int(input("몇일에 출발 하나요(숫자만): "))

today = datetime.datetime.now().date()
while True:
  try:
    travel_day = datetime.datetime(year, month, day).date()
    break
  except ValueError:
    print("존재하지 않는 날짜 입니다")
    exit()

legend_day = travel_day - today

if legend_day.days > 0:
  print(f"여행 출발까지 {legend_day.days}일 남았습니다")
elif legend_day.days == 0:
  print("여행 당일입니다")
else:
  print("여행일이 이미 지났습니다") 