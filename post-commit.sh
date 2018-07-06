#!/bin/bash

wget_exists=$(which wget > /dev/null; echo $?)

if [[ $wget_exists == 1 ]]; then
    exit
fi

html=$(wget -qO- http://minimalmaxims.com/)
quote_regex='<span class="quotable-quote"><p>([a-zA-Z0-9 ;’,‘?:\.—\-]+)<\/p>'
author_regex='<cite class="quoteable-author">([a-zA-Z0-9— ;\.\-]+)<\/cite>'

if [[ $html =~ $quote_regex ]]; then
    quote=${BASH_REMATCH[1]}
fi

if [[ $html =~ $author_regex ]]; then
    author=${BASH_REMATCH[1]}
fi

if [[ ! -z $quote && ! -z $author ]]; then
    echo
    echo $quote | fold -w 70 -s
    echo
    echo "     $author"
    echo
fi
