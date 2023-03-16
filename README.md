# git指令

### git --version 
-查詢版本

### 建立基本資訊
- git config --global user.name han
- git config --global user.email dubisthan@gmail.com

### 查找config
- git config --list

### 建立倉庫
-git init

### 觀察狀態
- git status(untrack,added,moified,deleted)

### 加入暫存區
- git add filename
- git add . (folder全檔案)

### 觀察object
- git cat -file -p sha1(檔案名稱)
   -內容
- git cat -file -t sha1(檔案名稱)
 -型態
- git cat -file -s sha1(檔案名稱)
 -大小

### 觀察暫存區的檔案
-git ls-files
-git ls-files -s

### 將暫存區檔案加入倉庫
-git commit -m"message"
-git commit -am  (以確認後的增加和message)
-git commit --amend (保留之前紀錄+修改message)

### 查看目前commit狀態與歷程(q離開)
-git log
-git log --oneline

### 手動刪除恢復檔案
-git restore

### 指令刪除(少用)
- git rm-f filename(手動刪除+git add)
	-git restore --staged filename(需要寫兩次才能復原)

### 將檔案搬離暫存/倉庫區
-git rm --cached filename

### 分支指令
-git brunch

### 新增分支
-git brunch filename

###刪除分支
-git brunch -D filename

### 切換分支
-git checkout branch-name
 
### 新增branch+checkout
-git checkout -b filename 

### 更改分支名稱
-git brunch -m filename filename2 

### 合併分支
-git checkout master
	-git merge test

### 衝突處理 

### 反悔合併
-git merge --abort

### 切換commit
-git checkout master

### 回到過去的commit
-git reset commit-object

### 規定雲端Git Hub網址
-git remove add origin https://github.com/ichbinhan/git-demo

### 推送指令
-git push -u origin master
-git push (已綁定分支)