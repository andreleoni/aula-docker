#!/bin/bash

if [ $# -eq 0 ]; then
  /usr/games/cowsay "olá, pessoal!"
else
 /usr/games/cowsay "$@"
fi
