# 需求文档

1. 数据模型
   
    user 类
    ```python
    class userinfo(db.Model):
        # 表的别名
        __tablename__ = "表别名"
      
        id = db.Column(db.Integer, primary_key = True, nullable = False)
        ...
    class user_status(db.Model):
        stas = db.Column(db.Booler, primary_key = True, nullable = False)
        
   ```
2. API接口规范
