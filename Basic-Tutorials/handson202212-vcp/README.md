(2022-12-23 学認クラウドオンデマンド構築サービスセミナー)

# さくらのクラウドとVCPポータブル版によるオンデマンド構築サービスの活用

今回のハンズオンでは、さくらのクラウドに「VCP ポータブル版」を構築し、
VCコントローラの管理までの流れを確認します。
この環境を利用し、オンデマンド構築サービスの仕組みと基本的な使い方を実習します。

さらに、オンデマンド構築サービス上に「複数人で利用可能な軽量 Python 実習環境 (JupyterHub) 」
の配備と、そのカスタマイズ方法などについて実習します。

## 各実習ページへのリンク

### 1. VCPポータブル版の構築

[Setup-VCP-Portable.md](./Setup-VCP-Portable.md)

さくらのクラウドに「VCPポータブル版」を構築し、VCコントローラの管理手順を確認します。

1. さくらのクラウドでの環境構築 
    - コントロールパネルへログインし、サーバの作成とネットワーク設定を行います。

2. VCPポータブル版の実行
    - 作成したサーバにSSHでログインし、VCPポータブル版を起動します。

3. VCコントローラの管理
    - VCPポータブル版において、VCコントローラの管理コマンド群を実行します。

### 2. Jupyter Notebook 入門

[JupyterNotebook_Introduction.ipynb](./JupyterNotebook_Introduction.ipynb)

Jupyter Notebookの基本操作と、NIIクラウド運用チームによるプラグイン拡張の一部について説明します。

### 3. VCノードの起動、削除

[sakura-101-VCノードの起動、削除.ipynb](./sakura-101-VCノードの起動、削除.ipynb)

VCP SDKを利用してさくらのクラウドにVCノードを起動し、VCPの基本的な使い方を確認します。

### 5. VCP演習-JupyterHub

[sakura-403-VCP演習-JupyterHub.ipynb](./sakura-403-VCP演習-JupyterHub.ipynb)

VCPを活用したアプリケーションとして、The Littlest JupyterHub を構築します。
