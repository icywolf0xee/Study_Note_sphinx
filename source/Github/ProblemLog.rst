=====
问题记录
=====


1.Git-提交时On branch master Your branch is up to date with
======
    参考：https://blog.csdn.net/qq_36079972/article/details/100279562

    最新更新时间:2023.12.31
    
    1.新建一个分支
        >>> git branch newbranch
    2.切换到你的新分支
        >>> git checkout newbranch
    3.将你的改动提交到新分支上
        >>> git add .
        >>> git commit -m "newbranch"
    4.切换会主分支
        >>> git checkout master
    5.将新分支提交的改动合并到主分支上
        >>> git merge newbranch 
    6.push代码
        >>> git push -u origin master
    7.删除分支
        >>> git branch -D newbranch
