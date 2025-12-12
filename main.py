# 설정
from panda3d.core import loadPrcFileData, AntialiasAttrib
loadPrcFileData('', 'framebuffer-multisample 1')
loadPrcFileData('', 'multisamples 4')
loadPrcFileData('', 'render-mode forward')

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor
import random

app = Ursina()
mouse.visible = False
render.setAntialias(AntialiasAttrib.MAuto)

# 안개
scene.fog_color = color.black
scene.fog_density = 0.05

# 맵: 메인 복도
main_floor = Entity(model='cube', position=(0, 0, 0), scale=(10, 1, 100),color=color.white, collider='box', texture='assets/돌.png', texture_scale=(5,50))
main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(10, 1, 100), color=color.white, collider='box', texture='assets/천장.png', texture_scale=(5,50))

main_left_wall_bottom = Entity(model='cube', position=(-5, 1.25, -5), scale=(1, 2.5, 110), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
main_left_wall_top = Entity(model='cube', position=(-5, 6.25, -5), scale=(1, 7.5, 110), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))
main_right_wall_bottom = Entity(model='cube', position=(5, 1.25, 5), scale=(1, 2.5, 110), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
main_right_wall_top = Entity(model='cube', position=(5, 6.25, 5), scale=(1, 7.5, 110), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))

# 타일
tile_entities = []
for a in range(-38, 38):
    tile_entities.append(Entity(model='cube', position=(0, 0.55, a*1.33), scale=(1.33, 0, 1.33), texture='assets/yellow_tile.jpg'))
for b in range(45, 105):
    tile_entities.append(Entity(model='cube', position=(-50, 0.55, b*1.33), scale=(1.33, 0, 1.33), texture='assets/yellow_tile.jpg'))
for c in range(-105, -45):
    tile_entities.append(Entity(model='cube', position=(50, 0.55, c*1.33), scale=(1.33, 0, 1.33), texture='assets/yellow_tile.jpg'))

# 맵: 앞쪽 구역
front_floor = Entity(model='cube', position=(-25, 0, 55), scale=(60, 1, 10), color=color.white, collider='box', texture='assets/돌.png', texture_scale=(30, 5))
front_ceiling = Entity(model='cube', position=(-25, 10, 55), scale=(60, 1, 10), color=color.white, collider='box', texture='assets/천장.png', texture_scale=(30, 5))
Entity(model='cube', position=(-30, 1.25, 50), scale=(50, 2.5, 1), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(-30, 6.25, 50), scale=(50, 7.5, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))
Entity(model='cube', position=(-20, 1.25, 60), scale=(50, 2.5, 1), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(-20, 6.25, 60), scale=(50, 7.5, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))

front_floor_2 = Entity(model='cube', position=(-50, 0, 80), scale=(10, 1, 60), color=color.white, collider='box', texture='assets/돌.png', texture_scale=(5,30))
front_ceiling_2 = Entity(model='cube', position=(-50, 10, 80), scale=(10, 1, 60), color=color.white, collider='box', texture='assets/천장.png', texture_scale=(5,30))
Entity(model='cube', position=(-55, 1.25, 75), scale=(1, 2.5, 50), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(-55, 6.25, 75), scale=(1, 7.5, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))
Entity(model='cube', position=(-45, 1.25, 85), scale=(1, 2.5, 50), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(-45, 6.25, 85), scale=(1, 7.5, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))

# 맵: 뒤쪽 구역
back_floor = Entity(model='cube', position=(25, 0, -55), scale=(60, 1, 10), color=color.white, collider='box', texture='assets/돌.png', texture_scale=(30, 5))
back_ceiling = Entity(model='cube', position=(25, 10, -55), scale=(60, 1, 10), color=color.white, collider='box', texture='assets/천장.png', texture_scale=(30, 5))
Entity(model='cube', position=(30, 1.25, -50), scale=(50, 2.5, 1), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(30, 6.25, -50), scale=(50, 7.5, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))
Entity(model='cube', position=(20, 1.25, -60), scale=(50, 2.5, 1), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(20, 6.25, -60), scale=(50, 7.5, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))

back_floor_2 = Entity(model='cube', position=(50, 0, -80), scale=(10, 1, 60), color=color.white, collider='box', texture='assets/돌.png', texture_scale=(5,30))
back_ceiling_2 = Entity(model='cube', position=(50, 10, -80), scale=(10, 1, 60), color=color.white, collider='box', texture='assets/천장.png', texture_scale=(5,30))
Entity(model='cube', position=(55, 1.25, -75), scale=(1, 2.5, 50), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(55, 6.25, -75), scale=(1, 7.5, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))
Entity(model='cube', position=(45, 1.25, -85), scale=(1, 2.5, 50), collider='box', texture='assets/wall_1.jpg', texture_scale=(16, 2.5))
Entity(model='cube', position=(45, 6.25, -85), scale=(1, 7.5, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 7.5))

# NPC 설정
npc = Entity(position=(-1.5, 0.5, 45), scale=(1.25, 1.25, 1.25), collider='box', enabled=False)
actor = Actor('assets/npc.glb')
actor.reparent_to(npc)
actor.loop('Armature|mixamo.com|Layer0')

# 플레이어 및 변수
player = FirstPersonController()
player.position = (0, 2, -50)
player.cursor.visible = False
player.gravity = 0.5
player.speed = 7.5
default_fov = camera.fov
enemy_speed = 115

anomalies = 0
direction = 0
direction_haveto = 0
exit_count = 0
npc_dir = -1

# 표지판 및 UI
sign_ceiling = Entity(model='cube', position=(0, 8, 25), scale=(8, 1, 0.1), texture=f'assets/exit_{exit_count}_ceiling.jpg')
sign_main_walls = []
for z in [-30, -10, 10, 30]:
    sign_main_walls.append(Entity(model='quad', position=(-4.49, 2.7, z), scale=(16, 9), rotation_y=-90, texture='assets/메인복도.png'))
    sign_main_walls.append(Entity(model='quad', position=(4.49, 2.7, z), scale=(16, 9), rotation_y=90, texture='assets/메인복도.png'))

sign_wall_front = Entity(model='cube', position=(4.4, 4.5, 55), scale=(0.1, 3.8, 2), texture='assets/exit_0_wall.jpg', texture_scale=(-1, 1))
sign_wall_back = Entity(model='cube', position=(-4.4, 4.5, -55), scale=(0.1, 3.8, 2), texture='assets/exit_0_wall.jpg')
exitgate = None

black_screen = Entity(model='quad', scale=(20, 20), color=color.black, visible=False)
enemy = None

clear_bg = Entity(parent=camera.ui, model='quad', scale=(2, 1), color=color.black, z=-1, visible=False)
clear_text = Text(text='GAME CLEAR', parent=camera.ui, scale=3, color=color.red, origin=(0,0), z=-2, visible=False)

# 오디오
try: bgm = Audio('sounds/Inside the Drain Pipe - Super Mario Galaxy 2.mp3', loop=True, autoplay=True)
except: bgm = None

try: knock_sound = Audio('sounds/knock.mp3', loop=False, autoplay=False)
except: knock_sound = None

current_sound = None
def play_sound(sound):
    global current_sound
    if current_sound: current_sound.stop()
    current_sound = sound
    if current_sound: current_sound.play()

# 함수
def reset_anomalies():
    scene.fog_density = 0.02
    scene.fog_color = color.black
    camera.rotation_z = 0
    camera.fov = default_fov
    npc.enabled = False
    npc.scale = (1.25, 1.25, 1.25)
    player.speed = 7.5
    
    for t in tile_entities: t.texture = 'assets/yellow_tile.jpg'
    
    main_floor.color = front_floor.color = front_floor_2.color = back_floor.color = back_floor_2.color = color.white
    if knock_sound: knock_sound.stop()

def update_signs():
    global sign_ceiling, sign_main_walls, sign_wall_front, sign_wall_back, exitgate
    
    # 천장 표지판
    destroy(sign_ceiling)
    tex_ceiling = 'assets/빨간표지판.jpg' if anomalies == 9 else f'assets/exit_{min(exit_count, 8)}_ceiling.jpg'
    sign_ceiling = Entity(model='cube', position=(0, 8, 25), scale=(8, 1, 0.1), texture=tex_ceiling)

    # 벽 포스터
    for s in sign_main_walls: destroy(s)
    sign_main_walls.clear()
    
    target_poster_idx = -1
    if 12 <= anomalies <= 19:
        target_poster_idx = anomalies - 12
    
    current_idx = 0
    for z in [-30, -10, 10, 30]:
        for x_pos, rot in [(-4.49, -90), (4.49, 90)]:
            if current_idx == target_poster_idx:
                tex = f'assets/이상현상{random.randint(1, 6)}.png'
            else:
                tex = 'assets/메인복도.png'
                
            sign_main_walls.append(Entity(model='quad', position=(x_pos, 2.7, z), scale=(16, 9), rotation_y=rot, texture=tex))
            current_idx += 1

    # 출구 표지판
    if sign_wall_front: destroy(sign_wall_front)
    if sign_wall_back: destroy(sign_wall_back)
    
    if anomalies == 11:
        tex_name = 'assets/이상현상_포스터.jpg'
    else:
        tex_name = f'assets/exit_{min(exit_count, 8)}_wall.jpg'

    sign_wall_front = Entity(model='cube', position=(4.4, 4.5, 55), scale=(0.1, 3.8, 2), texture=tex_name, texture_scale=(-1, 1))
    sign_wall_back = Entity(model='cube', position=(-4.4, 4.5, -55), scale=(0.1, 3.8, 2), texture=tex_name)

    # 탈출구 및 이상현상
    if exitgate: destroy(exitgate)
    exitgate = Entity(model='cube', position=(0, 2.7, 0), scale=(16, 9, 16), texture='assets/출구.png') if exit_count == 9 else None

    if anomalies == 2: # 붉은 바닥
        main_floor.color = front_floor.color = front_floor_2.color = back_floor.color = back_floor_2.color = color.red
    elif anomalies == 3: # 거대 NPC
        npc.enabled = True; npc.scale = (3.5, 3.5, 3.5)
    elif anomalies == 4: # 카메라 반전
        camera.rotation_z = 180
    elif anomalies == 5: # 시야 왜곡
        camera.fov = 120
    elif anomalies == 6: # 일반 NPC
        npc.enabled = True; npc.scale = (1.25, 1.25, 1.25)
    elif anomalies == 7: # 초록 타일
        for t in tile_entities: t.texture = 'assets/green_tile.jpg'
    elif anomalies == 8: # 노크 소리
        if knock_sound: knock_sound.play()

def restart_game():
    global exit_count, anomalies, enemy, direction_haveto
    exit_count = 0
    anomalies = 0
    direction_haveto = 0
    player.position = (0, 2, -50)
    player.rotation = (0, 0, 0)
    reset_anomalies()
    update_signs()
    
    if enemy: destroy(enemy); enemy = None
    black_screen.visible = False
    clear_bg.visible = False
    clear_text.visible = False
    player.enabled = True

def update():
    global npc_dir, anomalies, direction, direction_haveto, exit_count, enemy, enemy_speed

    # NPC 이동
    if npc.enabled:
        if npc_dir == -1 and npc.position.z < -45:
            npc_dir = 1; npc.rotate((0, 180, 0))
        elif npc_dir == 1 and npc.position.z > 45:
            npc_dir = -1; npc.rotate((0, -180, 0))
        npc.set_position((npc.position.x, npc.position.y, npc.position.z + npc_dir * 2 * time.dt))

    # 무한 루프 (앞쪽)
    if player.position.x < -25 and player.position.z > 50:
        player.set_position((50 + player.position.x, player.position.y, -110 + player.position.z))
        direction = 0
        reset_anomalies()

        if direction_haveto == direction:
            exit_count += 1
            if exit_count == 8: anomalies = 10
            elif exit_count == 9: anomalies = 0
            else: anomalies = random.randint(2, 19) if random.randint(0, 1) else 0
            
            if anomalies > 0: direction_haveto = 1 if direction_haveto == 0 else 0
            update_signs()
        else: restart_game()

    # 무한 루프 (뒤쪽)
    elif player.position.x > 25 and player.position.z < -50:
        player.set_position((-50 + player.position.x, player.position.y, 110 + player.position.z))
        direction = 1
        reset_anomalies()

        if direction_haveto == direction:
            exit_count += 1
            if exit_count == 8: anomalies = 10
            elif exit_count == 9: anomalies = 0
            else: anomalies = random.randint(2, 19) if random.randint(0, 1) else 0

            if anomalies > 0: direction_haveto = 1 if direction_haveto == 0 else 0
            update_signs()
        else: restart_game()

    # 적 로직 (이상현상 10)
    if anomalies == 10:
        if not enemy:
            enemy = Entity(model='cube', position=(0, 4, 0), scale=(6, 8, 0.1), texture='assets/람브.png')
            try: play_sound(Audio('sounds/여자 비명.mp3', loop=False))
            except: pass
    else:
        if enemy: destroy(enemy); enemy = None

    if enemy:
        target_pos = player.position
        top_junction_z = 45
        bottom_junction_z = -45

        # 길찾기
        if player.z > top_junction_z and enemy.z < top_junction_z:
            target_pos = Vec3(0, enemy.y, top_junction_z)
        elif player.z < bottom_junction_z and enemy.z > bottom_junction_z:
            target_pos = Vec3(0, enemy.y, bottom_junction_z)
        elif player.z < top_junction_z and enemy.z > top_junction_z:
            target_pos = Vec3(0, enemy.y, top_junction_z)
        elif player.z > bottom_junction_z and enemy.z < bottom_junction_z:
            target_pos = Vec3(0, enemy.y, bottom_junction_z)

        # 적 이동
        enemy.look_at(Vec3(target_pos.x, enemy.y, target_pos.z))
        enemy.position += enemy.forward * enemy_speed * time.dt
        
        # 게임 오버 체크
        diff = player.position - enemy.position
        diff.y = 0
        if diff.length() < 1: 
            restart_game()

    # 클리어 체크
    if exitgate:
        if (player.position - exitgate.position).length() < 10 and not clear_bg.visible:
            try:
                if bgm: bgm.stop()
                play_sound(Audio('sounds/Sonic Adventure 2 Music - Level Clear.mp3', loop=False))
            except: pass
            
            player.enabled = False
            mouse.visible = True
            clear_bg.visible = True
            clear_text.visible = True

app.run()