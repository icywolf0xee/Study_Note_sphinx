

=========
团队操作
=========

最后更新日期:2023.12.31

参考：https://blog.csdn.net/whc18858/article/details/133209975

分支管理策略
=========
    Git分支策略允许开发人员在一个项目上进行协作，同时跟踪更改并维护多个版本的代码库。主流的分支管理策略有 Trunk-Based Development、Feature Branching、Git Flow等等，本文将基于较为简单的 Feature Branching 分支管理策略展开。虽然分支管理策略多种多样，但最好的策略一定是与你的团队特征和项目需求相匹配的。

    1.什么是Feature Branching？
    在实际开发中，master 分支非常强调环境的稳定性。因此当我们要开发新的功能或者特性时，需要从 master 分支上拉取 feacture 分支，这样开发者就能在 feacture 分支上独立开发而不影响主分支。当完成开发后，需要提交 pull request 将 feacture 分支合并回 master 分支中。 通过 pull request ，仓库中的其他成员能对即将 merge 的代码进行审核并提出建议，从而保证了安全可靠性。


    2.Feature Branching如何工作？
        创建 feacture 分支：feacture 分支一定是从 master 分支上拉取的
        在 feacture 分支上完成开发：通常一个分支就对应着一个特定的功能
        提交 pull request：请求将分支合并回 master 分支
        审查批准：其他开发人员如果对你的代码满意的话，就会同意将你的分支合并到 master 分支。通过代码审查，我们通常能在分支 merge 回主分支前发现错误
        清理：完成开发后，应该及时将没用的 feacture 分支删除，保持代码仓库的整洁

多人协作一：单分支
==============
    1.创建分支
        在克隆代码之后，通过对应命令创建分支，通常有两种创建方法
            1.远程创建

            2.本地创建，使用命令创建分支 

            >>> git push origin <branchname>

        在更新代码之后需要利用  git pull   拉取最新数据  

    2.工程主要在分支上开发
        完成之后，提交到对应分支上
        ::
            在push时如果仓库版本高于本地版本则会冲突导致失败，在开发前务必拉取最新数据

    3.合并分支
        合并分支也有两种方式：

        1.提交 pull request，通过代码审验后合并到 master 分支

        2.在本地 master 分支上合并后再 push 到远端的 master 分支

    4.清理分支
        完成合并后，就可以将没用的 feacture 分支删除。删除分支也有两种方式：
        
        1.在远端和本地分别删除 feacture 分支
        
        2.在本地删除 feacture 分支后推送到远端



多人协作二：多分支
==================
    多人在单分支上协作开发时，经常需要解决冲突的问题；而使用多分支，各个开发者在各自的分支上独立开发，只需要在最后合并分支时解决冲突即可。

    大部分步骤与单分支相似

