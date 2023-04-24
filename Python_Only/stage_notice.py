class StageNotice:
    """게임 스테이지에 대한 정보를 출력합니다.
        staticmethod는 클래스에 속하지만 인스턴스에 속하지 않으며,
        인스턴스를 통하지 않고 클래스 이름으로 직접 호출할 수 있다."""

    @staticmethod
    def stage_clear(stage_num):
        """스테이지 클리어 안내 메시지를 출력합니다."""
        print(f"Stage {stage_num} Clear!\n")

    @staticmethod
    def last_location(stage):
        """현재 스테이지의 발사체 마지막 위치를 출력합니다."""
        print(f"발사체의 마지막 위치는 다음과 같다. : {stage.get_last_location()}")

    @staticmethod
    def tank_position(stage):
        """현재 스테이지의 탱크 위치를 출력합니다."""
        print(f"현재 단계 탱크의 위치는 다음과 같다. : {stage.get_tank_position()}")

    @staticmethod
    def target_positions(stage):
        """현재 스테이지의 목표물 위치를 출력합니다."""
        print(f"현재 단계 목표물의 위치는 다음과 같다. : {stage.get_target_positions()}")
