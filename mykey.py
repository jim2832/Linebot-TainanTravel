LINE_CHANNEL_ACCESS_TOKEN = "YfyqDdoq1Sol2j1cVY3gutr0vtFHr9ZWxs4VFPZ5stgiFZfCKFMboIoX90mD24bTku0TFIOhv88MGxoqQdDHd7Pbix1vFVH/F9DFkfgWsLyfxbzF67JyVQzs5YSaG3oE4oxs6KsH2dO7WIoUF9bjOgdB04t89/1O/w1cDnyilFU="

LINE_CHANNEL_SECRET = "8e6418a16952fc88a423078ae4568183"

LINE_PUSH_TARGET_ID = "U79e56c5d8383938f2ca93b88a1227112"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruction of pushing code to heroku
# git add .
# git commit -m'ok'
# git push heroku master

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruction of cover the previous file
# git commit --amend

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. git add *.c
#    git add 支援萬用字元 (*)，這個範例是一次 git add 所有 .c 檔

# 2. git add -A
#    一次加入所有變更。這個會是 git add 最常用的用法
#    如果要刪除檔案，可以直接將檔案刪除後，用 git add 將刪除檔案這項變更加入到暫存區，之後再提交。如果要重新命名檔案也是相同的方式，但要刪除和重新命名的檔案都需要 git add 過才可以。

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 將本地資料夾推上github
# 1. 在github上新建一個倉庫，建立時有一個https地址，記錄此地址，後面用 
# 2. 開啟git bash，轉到你所要上傳的資料夾目錄下，並輸入git init 
# 3. 將專案新增到倉庫中去：git add .，如果新增某個檔案，可以使用git add xxx 

# 4. 將新增的檔案提交到倉庫：git commit -m "--註釋--" 

# 5. 將倉庫關聯到github：git remote add origin https://xxxx，https為剛才github上建立倉庫的地址 

# 6. 把檔案推送到github倉庫：git push -u origin master，下次推送時，可以把-u去掉


# 注意：

# 在將本地倉庫與GitHub網站上的倉庫進行關聯後，便可進行推送了，但是在第一次進行推送時，需要注意的是，GitHub網站上的倉庫並非是空的，我們在建立時建立了一個README文件，因此需要將兩者進行合併才行。

# git pull --rebase origin master
# 最後，在進行推送即可。

# git push -u origin master
# 這個帶有-u這個引數是指，將master分支的所有內容都提交，第一次關聯之後後邊你再提交就可以不用這個引數了，之後你的每一次修改，你就可以只將你修改push就好了。

# git push origin master