class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes



username = input()
content = input()
comment = Comment(username, content)
print(comment.username)
print(comment.content)