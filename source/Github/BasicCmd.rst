=========
基础操作
=========

最后更新日期:2023.12.31

绑定用户操作
==================

    全局配置，对所有代码库生效

        >>> git config --global user.name "你的名字"

        >>> git config --global user.email "你的邮箱"


    局部配置，只对当前的代码库有效

        >>> git config --local user.name "你的名字"

        >>> git config --local user.email "你的邮箱"

    查看配置信息
        >>> git config --list

----

绑定ssh
==================
    使用下面的命令创建ssh密钥
        >>> ssh-keygen -t rsa -C "邮箱地址"
    之后生成的对应路径下的ssh文件，将pub后缀文件复制到github菜单中即可，添加到
    |setting->SSH and GPG keys->New SSH key


----

创建步骤(一般在git下创建项目之后会有直接相关指令)
================
    初始化git库
        >>> git init <该文件下子文件夹>

    远程关联
        >>> git remote add [alias] [url]
    远程关联完成后即可上传

----

下载文件
===============
    克隆文件夹用于初次下载一般取git协议地址。http协议地址每次push都需要输入token，token的username是邮箱而非用户名
        clone命令：url是仓库地址，directory是本地目录
        >>> git clone <url> [directory]


    拉取命令用于更新项目
        pull命令
            >>> git pull [options] [<repository> [<refspec>…]]
        示例:以下是一些示例 -

            >>> git pull <远程主机名> <远程分支名>:<本地分支名> 
        
        比如，要取回origin主机的next分支，与本地的master分支合并，需要写成下面这样 -

            >>> git pull origin next:master
        
        如果远程分支(next)要与当前分支合并，则冒号后面的部分可以省略。上面命令可以简写为：

            >>> git pull origin next
        
        上面命令表示，取回origin/next分支，再与当前分支合并。实质上，这等同于先做git fetch，再执行git merge。

            >>> git fetch origin
            >>> git merge origin/next

----

上传文件
=================
    一般流程(上传全部文件)
        >>> git add .
        >>> git commit -m "注释"
        >>> git push -u origin master (目标分支，个人项目一般只有这个分支，详细操作到团队操作)


----

Git 基本指令的使用
=================
    下面介绍一下git中常用的几种命令：

    配置信息
        >>> git config
    添加文件到缓存命令
        >>> git add
    查看文件的状态命令
        >>> git status
    查看更新的详细信息命令
        >>> git diff
    提交命令
        >>> git commit
    取消缓存命令
        >>> git reset HEAD
    删除命令
        >>> git rm
    移动或重命名命
        >>> git mv
    查看提交历史
        >>> git log
        ::
            -oneline ：查看历史记录的简洁版本
            -graph ：查看历史中什么时候出现了分支、合并
            -reverse ：逆向显示所有日志
            -author ：查找指定用户的提交日志
            -since、–before、 --until、–after： 指定帅选日期
            -no-merges ：选项以隐藏合并提交



分支指令
=================
    创建分支,没有BranchName就是查看分支
        >>> git branch <BranchName>
    切换分支
        >>> git checkout <TargetBranch>
    删除分支
        >>> git branch -D <TargetBranch>
    合并目标分支到当前分支
        >>> git merge <TargetBranch>




仓库指令
=============
    添加远程仓库
        >>> git remote add
    查看当前的远程仓库
        >>> git remote
    提取远程仓仓库
        >>> git fetch
        >>> git pull
        ::
            git fetch和git pull的区别：
            git fetch：相当于是从远程获取最新版本到本地，不会自动合并。
            git pull：相当于是从远程获取最新版本并merge到本地。
            git pull 指令的完整用法是 git pull <远程主机名> <远程分支名>:<本地分支名>

    推送到远程仓库
        >>> git push
    删除远程仓库
        >>> git remote rm