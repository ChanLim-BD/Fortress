from game_controller import GameController
from constants import GAME_CLEAR, MAX_STAGE_NUM

def main():
    # 게임 객체 생성
    game_controller = GameController()

    # 게임 루프 (설정 상, MAX_STAGE_NUM단계 클리어할 때 까지)
    # for _ in range(MAX_STAGE_NUM):
    while True:
        # 게임을 시작한다.
        game_controller.start_game()
        # 게임을 업데이트
        if game_controller.update_game() == GAME_CLEAR:
                # 스테이지 클리어하면 다음 스테이지로 이동 및 게임 클리어시 종료
            game_controller.end_game()
        else:
            # 게임 업데이트 실패 시 유저 입력을 다시 받음
            continue


if __name__ == '__main__':
    main()
