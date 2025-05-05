# Web and Chat Text in nltk.corpus

from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat

chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])
