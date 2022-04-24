#!/bin/bash
for i in {1..15}; do docker stats --no-stream --format "table {{.CPUPerc}}" server1 | tail -n 1 | ts '[%Y-%m-%d %H:%M:%S]' >> log; done