#!/bin/bash

html=$(wget -qO- http://minimalmaxims.com/)
quote_regex='<span class="quotable-quote"><p>([a-zA-Z0-9 ;’,‘?:\.—\-]+)<\/p>'
author_regex='<cite class="quoteable-author">([a-zA-Z0-9— ;\.\-]+)<\/cite>'

if [[ $html =~ $quote_regex ]]; then
    quote=${BASH_REMATCH[1]}
else
    echo $html
fi

if [[ $html =~ $author_regex ]]; then
    author=${BASH_REMATCH[1]}
fi

echo
echo $quote | fold -w 70 -s
echo
echo "     $author"
echo
