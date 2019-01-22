#!/usr/bin/env bash

http https://httpbin.org/anything

http -a user:password https://httpbin.org/anything

http POST https://httpbin.org/anything a=b c=d
