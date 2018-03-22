#!/bin/sh

docker build -t "praekeltfoundation/gem-molo-unicore-redirect" .

pytest
