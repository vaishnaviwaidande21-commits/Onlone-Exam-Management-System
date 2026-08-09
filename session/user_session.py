current_user = {}


def set_user(user_id, name, role):

    current_user["id"] = user_id
    current_user["name"] = name
    current_user["role"] = role



def get_user():

    return current_user



def clear_user():

    current_user.clear()