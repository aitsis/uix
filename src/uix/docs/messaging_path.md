# UIX Messaging Path
## Initialization


| Browser | UIX |
| ------ | ------- |
| GET -> index.html | app -> route -> createHTML|
|index.html + main.js load| |
|onload -> socket connection| Create Session Instance|
|socket - >emit -> (id = ait-uix),init | app->from_client
|| Run Pipes|
|| session->clientHandler |
|| Create Elements |
|| Render -> text |
|| socket-> send -> init_content -> text|
|main.js -> from_server||
|init_content -> Create OuterHTML from text||

