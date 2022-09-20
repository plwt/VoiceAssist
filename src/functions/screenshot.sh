#!/bin/bash

xfce4-screenshooter --fullscreen --save ~/Desktop/"Screenshot $(date -d today "+%Y-%m-%d %H:%M").png";history -d $(history 1)