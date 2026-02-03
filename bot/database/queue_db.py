from bot.database.mongo import db

queue = db.queue

def add_song(chat_id, data):
    queue.insert_one({"chat_id": chat_id, "data": data})

def get_queue(chat_id):
    return list(queue.find({"chat_id": chat_id}))

def pop_song(chat_id):
    song = queue.find_one({"chat_id": chat_id})
    if song:
        queue.delete_one({"_id": song["_id"]})
    return song

def clear_queue(chat_id):
    queue.delete_many({"chat_id": chat_id})
