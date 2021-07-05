#! /bin/bash
# docker-composeで--gpusオプションが指定できず動作確認がしにくい。そのためシェルスクリプトにした。
# ポータブル版、サービス版でAppコンテナイメージを共通化するためharborにあるイメージを使用する
docker run -td --gpus all --name openpose -v $PWD/data:/root/data -v $PWD/result:/root/result -v $PWD/result2:/root/result2 harbor.vcloud.nii.ac.jp/vcp/openpose:handson_20.11
