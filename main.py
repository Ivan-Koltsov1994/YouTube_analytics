from src.Dataclass import Channel

channel_vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # id канала Вдудь

channel_vdud .print_info() # информация о канале

print(channel_vdud.title)
print(channel_vdud.video_count)
print(channel_vdud.url)
channel_vdud.channel_id = 'new_id'
print(Channel.get_service())
channel_vdud.record_to_json('vdud.json')
