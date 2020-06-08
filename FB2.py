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


# Step 3: Wall Posts
# • User A can post a status update on his/her Profile page
# • All friends of A get notified of this update
# • Friends can comment/like/share this update


class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.requests = []
        self.posts = []
        self.wall = Wall(self)

    def addFriend(self, user):
        req = FriendRequest(self, user)
        user.requests.append(req)

    def postOnFriendsWall(self, user, message):
        req = PostRequest(self, user, message)
        user.requests.append(req)
        return req

    def approve(self, req):
        req.approve()

    def post(self, post):
        p = Post(self, post)
        self.wall.add(p)
        return p

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
        FBrequest.__init__(self, sender, receiver)
        self.message = message

    def approve(self):
        self.receiver.posts.append(self.message)
        self.receiver.requests.remove(self)
        print(f"{self.receiver} has approved post request from {self.sender}.")

    def __repr__(self):
        return f"{self.sender} has sent a post request to {self.receiver}."

class Wall:
    def __init__(self, user):
        self.user = user
        self.posts = []

    def add(self, post):
        self.posts.append(post)

    def __repr__(self):
        s = ""
        for x in self.posts:
            s += str(x) + "\n"
        return f"The wall of {self.user}:\n{s}"

class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.sharedBy = []
        self.likedBy = []
        self.comments = []

    def addComment(self, user, comment):
        c = Comment(user, comment)
        self.comments.append(c)
        print(f"{user.name} has added a comment: {c.commentText} to post: {self.text}.")


    def __repr__(self):
        return f"{self.user.name} wrote {self.text}."


class Comment:
    def __init__(self, user, commentText):
        self.user = user
        self.commentText = commentText
        self.likedBy = []
        self.replies = []

    def __repr__(self):
        return self.commentText


u1 = User ("Joe")
u2 = User ("Jill")

print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))
print (u2.name + " Friend List = " + str(u2.friends))
print (u2.name + " Friend Requests = " + str(u2.requests))
print("---------------------------------")

print (u1.posts)
req = u1.postOnFriendsWall(u2, "Hey, happy birthday")
u2.approve(req)
print(u2.posts)

print("---------------------------------")
p1 = u1.post("What a lovely weekend...")
print(u2.wall)
p2 = u2.post("Sunny and warm!")
print(u2.wall)
print(u1.wall)
print("---------------------------------")
p1.addComment(u2, "You are right")
print(p1.comments)
