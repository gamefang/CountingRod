- 加入`res`文件夹图片至`images/bmpfnt/rod`

- rod_numerals.py放入`python-packages`目录

- 脚本添加

```python
# 导入库
init python:
    import rod_numerals
    rod = rod_numerals.Rod()
    teststr = rod.img_text(12345)

# 直接输出文字
label splashscreen:
    story '[teststr]'
```
