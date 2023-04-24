class UserInput:
    """유저로부터 입력을 받는 클래스 
    (이 게임은 각도와 강도만 받지만 원래라면 탱크 이동과 그 외 여러가지를 여기서 처리합니다.)"""
    
    def receive_input(self):
        """각도와 강도를 입력 받습니다."""
        while True:
            try:
                angle = float(input("각도를 입력하세요: "))
                power = float(input("강도를 입력하세요: "))
                return angle, power
            except ValueError:
                print("숫자 값을 입력하세요.")