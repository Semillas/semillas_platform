#!/bin/zsh
source ~/.zshrc
dm start default
#sleep(10)
eval $(/usr/local/bin/docker-machine env)
#sleep(16)
dc -f dev.yml up
echo "DALE CAÑA!!!"
