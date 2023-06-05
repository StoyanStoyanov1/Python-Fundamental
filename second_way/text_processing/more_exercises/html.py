class HTML:
    _html = []

    def __init__(self, article, content_of_article, comments_about_article):
        self.article = article
        self.content_of_article = content_of_article
        self.comments_about_article = comments_about_article

    def html(self):
        self._html.append(f"<h1>\n  {self.article}\n</h1>")
        self._html.append(f"<article>\n {self.content_of_article}\n</article>")

        for comment in self.comments_about_article:
            self._html.append(f"<div>\n {comment}\n</div>")

        return "\n".join(self._html)


article = input()
content_of_article = input()
comments = []

while True:
    comment = input()
    if comment == "end of comments":
        break
    comments.append(comment)

print(HTML(article, content_of_article, comments).html())