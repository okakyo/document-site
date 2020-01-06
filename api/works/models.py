from django.db import models

"""
Document Model:
    @param: title(String) : 記事のタイトル
    @param: description(Text) : 記事の内容
    @param: author: 記事の作成者(or 登録者)
    @param: create_at(Date) : 作成日時
    @param: update_at(Date) : 更新日時
"""
class DocumentModel(models.Model):
    title=models.CharField(nullable=False)
    description=models.FilePathField(nullable=False)
    created_at=models.DateField(auto_now=True,auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

