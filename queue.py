from collections import defaultdict, deque

queues = defaultdict(deque)

def add_song(chat_id, song):
    queues[chat_id].append(song)

def get_queue(chat_id):
    return list(queues[chat_id])

def pop_song(chat_id):
    if queues[chat_id]:
        return queues[chat_id].popleft()
    return None

def clear_queue(chat_id):
    queues[chat_id].clear()
