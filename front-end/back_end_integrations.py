import requests

base_url = 'http://localhost:8080'
auth = ('user', 'pass')


class RequestException(Exception):
    pass


def checkRequestSuccessful(r):
    if r.status_code != 200:
        raise RequestException(f'Something went wrong when handling this request {r.content}')


def login(login_details):
    """
    :param login_details: a tuple containing the username and password in that order
    :return: the userId which is used to send other requests

    IMPORTANT:
    --- CALL THIS METHOD BEFORE YOU DO ANYTHING, IT SETS A GLOBAL VARIABLE NEEDED FOR THE OTHER FUNCTIONS TO WORK ---
    """

    global auth
    r = requests.post(f"{base_url}/auth/login", auth=login_details)
    checkRequestSuccessful(r)
    auth = login_details
    return r.json()['message']



def signUp(auth):
    """
    :param auth: a tuple containing the username and password in that order
    :return: True if successful else an exception is raised
    """
    r = requests.post(f"{base_url}/auth/signup", json={'username': auth[0], 'password': auth[1]})
    checkRequestSuccessful(r)
    return True


def setProfilePicture(file_dir, user_id):
    """
    :param file_dir: the location of the file
    :param user_id: the id of the user to set the profile picture of
    :return: True if successful else an exception is raised
    """
    global auth
    files = {'file': open(file_dir, 'rb')}
    r = requests.post(f'{base_url}/user/{user_id}/profile-picture', files=files, auth=auth)


def getProfilePicture(file_name, user_id):
    """
    :param file_name: name of the file to save it to (don't put file extensions)
    :param user_id: id of the user you want the profile picture of
    :return: the name of the newly created image or raises an exception if unsuccessful
    """
    r = requests.get(f'{base_url}/user/{user_id}/profile-picture', auth=auth)
    checkRequestSuccessful(r)
    location = f'{file_name}.png'
    image = open(location, 'wb')
    image.write(r.content)
    return location


def getUserFriends(user_id):
    """
    :param user_id: the id of the user you are interested in
    :return: a list of dictionaries representing the friends should look something like this:
    [
        {
            "userId": 42069,
            "username": "Bobbert",
            "password": "", # set blank for obvious reasons
            "growthAmount": 69696969696,
            "profilePicture": SOME BYTES GO HERE

        }
    ]

    Note:
    Don't try to convert the bytes in the "profilePicture" value to an image. This won't work and idk any way around
    this. Instead you would have to call getProfilePicture on each userId, if I find a better way I will fix this
    but for now it will have to do. This may or may not slow down the app significantly making that many REST calls
    but we'll see if it becomes a significant problem
    """
    r = requests.get(f"{base_url}/user/{user_id}/friends", auth=auth)
    checkRequestSuccessful(r)
    return r.json()['message']


def addFriend(user_id, friend_id):
    """
    :param user_id: the id of the user the friend request is sent to
    :param friend_id: the id of the user who send the friend request
    :return: True if the action was successful, raises Exception if it fails
    """
    r = requests.get(f'{base_url}/user/{user_id}/add-friend/{friend_id}', auth=auth)
    checkRequestSuccessful(r)
    return True


def getGrowth(user_id):
    """
    :param user_id: the id of the user you are interested in
    :return: the amount of "cat growth" the user has done or raises exception if failed
    """
    r = requests.get(f'{base_url}/user/{user_id}/growth',auth=auth)
    checkRequestSuccessful(r)
    return r.json()['message']


def setGrowth(user_id, growth_increase):
    """
    :param user_id: id of the user you
    :param growth_increase: the amount to increase the "cat growth" by
    :return: True if successful else raises an exception
    """
    r = requests.put(f'{base_url}/user/{user_id}/addGrowth/{growth_increase}', auth=auth)
    checkRequestSuccessful(r)
    return True


def addPost(user_id, caption):
    """
    :param user_id: the id of the user posting
    :param caption: the caption for the post
    :return: the post id
    NOTE:
    --- You need to add the image after this by calling the setPostImage method with the id returned ---
    """
    r = requests.post(f'{base_url}/user/{user_id}/post', json={'caption': caption}, auth=auth)
    checkRequestSuccessful(r)
    return r.json()['message']


def getGoal(user_id, title):
    """
    :param user_id: id of the user who owns the goal
    :param title: title of the goal
    :return: a dictionary representing the goal. Should look something like this:
    {
        "userId": 3,
        "title": "reestablish the soviet union,
        "startDate": 3826378216983,
        "endDate": 32738972198372,
        "timeSpent": 42069,
        "description": "I love communism"
        "isComplete": False

    }
    NOTE:
    The time values are in Unix time. This is basically the number of seconds since a specific date in time. This is
    there is likely some Python library to convert from a normal time format to Unix and vice versa. I set it up this
    way cause it's convenient in terms of data transfer.
    """
    r = requests.get(f'{base_url}/user/{user_id}/goal/{title}', auth=auth)
    checkRequestSuccessful(r)
    return r.json()['message']


def addGoal(user_id, title, start, end, description, is_complete = False, time_spent = 0):
    """
    :param user_id: id of the user who will own the goal
    :param title: title of the goal
    :param start: day to start the goal (Unix Time)
    :param end: day to complete the goal (Unix Time)
    :param time_spent: time spent on the goal (seconds)
    :param description: description of the goal
    :param is_complete: whether the goal was complete or not
    :return: True if successful other wise throws an exception
    NOTE:
    Notice you cannot set the goal icon here. I cannot seem to find a way to send the bytes of the image here to to save
    it. You will have to set it separately
    """
    json = {

        "userId": user_id,
        "title": title,
        "startDate": start,
        "endDate": end,
        "timeSpent": time_spent,
        "description": description,
        "isComplete": is_complete

    }
    r = requests.post(f'{base_url}/user/{user_id}/addGoal', json=json, auth=auth)
    checkRequestSuccessful(r)
    return True


def getUsersGoals(user_id):
    """
    :param user_id: the id of the user you are interest
    :return: a list of dictionaries representing all the user's goals. Should look like this:
    [
        {
            "userId": 3,
            "title": "reestablish the soviet union,
            "startDate": 3826378216983,
            "endDate": 32738972198372,
            "timeSpent": 42069,
            "description": "I love communism"
            "isComplete": False
        }

    ]
    """
    r = requests.get(f'{base_url}/user/{user_id}/goals', auth=auth)
    checkRequestSuccessful(r)
    return r.json()['message']

# signUp(('user', 'pass'))
# signUp(('stalin', 'hi'))
# signUp(('wee', 'woo'))
# addFriend(1, 6)
# addFriend(1, 7)

# print(getUsersGoals(2))
# print(addGoal(1, 'Learn Djano', 1609459200, 1624233600, 0, "It's a python web framework", False))
# print(getGoal(1, 'Learn Djano'))
