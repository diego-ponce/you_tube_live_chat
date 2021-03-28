# Scrape Live Chat Comments with Selenium and Python

There's a few running YouTube LiveChats which have great running commentary, in particular, for my interest in trains. This script runs a loop which prints chats and the chat author. Updating for a different chat or output other than stdout is left to the user, but since the script is simple, this shouldn't be hard to align to your use case.

## Usage
```
$ python yt_live_chat_log.py
AM458: SB
Mr. Executive #9580: B-VBTSEA
AM458: CN baretable
PNWRailfan: must be one of those "rolling storage" baretables
Dennis Mills: VBTSEA must be lost
Kb7yim: Symbol for the 14:54 should be looked at

```
## Requirements

- Python (built on 3.8)
- Selenium 
- Chrome webdriver (built on 2.38)
- runs on Linux, not sure what issues arise on other OSs

## TODOs

[x] persistent store of commentary
[x] check for new messages
[] filtering (only certain authors, etc)
[] argparse to convert to a command line utility
