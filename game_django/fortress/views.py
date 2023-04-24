from django.shortcuts import render
from django.views import View
from .models import Game

class GameView(View):
    def get(self, request):
        game = Game.create_game()

        request.session['game_id'] = game.id
        return render(request, 'game.html', {'game': game})

    def post(self, request):

        game_id = request.session.get('game_id')
        game = Game.objects.get(id=game_id)
        
        try:
            angle = float(request.POST.get('angle'))
            power = float(request.POST.get('power'))
        except (ValueError, TypeError):
            # 값이 없거나 잘못된 값이 들어오면 기본값을 사용합니다.
            angle = 45
            power = 45

        game.fire_projectile(angle, power)


        if game.update_projectiles(0.01):
            game.next_stage()
            if game.stage_manager.current_stage == 3:
                game.is_game_over = True
            print("명중!")


        projectile_positions = []
        target_positions = []

        if game.notice_last_location():
            last_location_pos = tuple(game.notice_last_location()[0])
            print("목표물의 위치는 다음과 같다. : {0}\n".format(game.notice_target()))
            target_positions.append(tuple(game.notice_target()))
            print("발사체의 마지막 위치는 다음과 같다. : {0}\n".format(last_location_pos))
            projectile_positions.append(last_location_pos)

        context = {'game': game, 'projectile_positions': projectile_positions, 'target_positions': target_positions}
        if game.is_game_over:
            context['game_over_message'] = "게임이 종료되었습니다."   
        
        return render(request, 'game.html', context)