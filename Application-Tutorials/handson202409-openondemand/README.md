(2024-09 学認クラウドオンデマンド構築サービスセミナー)

# 学認クラウドオンデマンド構築サービスを使用した OpenHPC + Open OnDemand の体験ハンズオン

今回のハンズオンでは、Amazon Web Services (AWS) 上に、HPCクラスタを容易に利用するためのWebポータル「Open OnDemand」を構築し、
ジョブのスケジューリングと実行、Jupyter Notebook環境を利用したインタラクティブな操作とデータの可視化を体験し、
Open OnDemandのポータルとしての有用性を実感いただきます。

また、ディスカッションを交えながら、クラウド上の HPC クラスタを利用する上での課題と対応案や利用状況の共有を行います。

## 各実習ページへのリンク

### Jupyter Notebook 入門

Jupyter Notebookの基本操作と、NIIクラウド運用チームによるプラグイン拡張の一部について説明します。

- [JupyterNotebook_Introduction.ipynb](./hands-on/101/JupyterNotebook_Introduction.ipynb)

### Open OnDemandの構築・活用

#### Open OnDemand構築

本日のハンズオンでは事前に [OpenHPC-v2](./hands-on/OpenHPC-v2/) テンプレートを用いて構築したOpenHPC (SLULRM) クラスタが事前に用意された状態から開始します。

以下のNotebookを順番に実行し、HPCクラスタのマスターノード上にOpen OnDemandを構築します。

- [OpenOnDemand/010-インストール](./hands-on/OpenOnDemand/010-インストール.ipynb)
- [OpenOnDemand/020-フロントエンドのセットアップ](./hands-on/OpenOnDemand/020-フロントエンドのセットアップ.ipynb)
- [OpenOnDemand/030-ジョブ実行環境の設定](./hands-on/OpenOnDemand/030-ジョブ実行環境の設定.ipynb)
- [OpenOnDemand/040-ジョブの実行](./hands-on/OpenOnDemand/040-ジョブの実行.ipynb)

#### Open OnDemandの活用

HPCクラスタとOpen OnDemandを活用し、HPCジョブとしてLinpackベンチマーク、JupyterNotebookサーバを実行します。

- [OpenOnDemand/050-JupyterNotebookのセットアップ](./hands-on/OpenOnDemand/050-JupyterNotebookのセットアップ.ipynb)
- [OpenOnDemand/060-JupyterNotebookジョブの実行](./hands-on/OpenOnDemand/060-JupyterNotebookジョブの実行.ipynb)
- [OpenOnDemand/070-Linpackフロントエンドの作成](./hands-on/OpenOnDemand/070-Linpackフロントエンドの作成.ipynb)
- [OpenOnDemand/080-Linpackの実行](./hands-on/OpenOnDemand/080-Linpackの実行.ipynb)

## ハンズオン環境概略図

![](images/000-004-handson.png)
