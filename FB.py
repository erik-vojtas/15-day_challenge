# Step 1: User A can add user B as friend
# • User B gets notified (receives a request)
# • User B can selectively choose to approve some requests
# • If approved, User B is added to the friend list of A and vice versa
# • If not approved, request is simply deleted.


# Step 2: Post on Users’ Wall
# • User A can post on user B’s wall
# • User B gets notified (receives a request)
# • User B has a list of post requests and can selectively choose to approve some requests
# • If approved, User A’s message is added to the wall of B

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.requests = []
        self.posts = []

    def addFriend(self, user):
        req = FriendRequest(self, user)
        user.requests.append(req)

    def postOnFriendsWall(self, user, message):
        req = PostRequest(self, user, message)
        user.requests.append(req)
        return req

    def approve(self, req):
        req.approve()

    def __repr__(self):
        return self.name

class FBrequest:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def reject(self):
        self.receiver.requests.remover(self)

class FriendRequest:
    def __init__(self, sender, receiver):
        FBrequest.__init__(self, sender, receiver)

    def approve(self):
        self.receiver.friends.append(self.sender)
        self.receiver.requests.pop(0)
        self.sender.friends.append(self.receiver)
        print(f"{self.receiver} has approved friends request from {self.sender}.")

    def __repr__(self):
        return f"{self.sender} has sent a friend request to {self.receiver}."

class PostRequest:
    def __init__(self, sender, receiver, message):
        FBrequest.__init__(self,sender,receiver)
        self.message = message

    def approve(self):
        self.receiver.posts.append(self.message)
        self.receiver.requests.remove(self)
        print(f"{self.receiver} has approved post request from {self.sender}")

    def __repr__(self):
        return f"{self.sender} has sent a post request to {self.receiver}."


u1 = User ("Joe")
u2 = User ("Jill")

print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))
print (u2.name + " Friend List = " + str(u2.friends))
print (u2.name + " Friend Requests = " + str(u2.requests))


print (u1.posts)
req = u1.postOnFriendsWall(u2, "Hey, happy birthday")
u2.approve(req)
print(u2.posts)