# d = {}
# with open("Download_inputs1.txt") as f:
#     for line in f:
#        (key, val) = line.split()
#        d[key] = val
# print(d)

# import youtube_dl
# ydl_opts = {'outtmpl': '/run/media/manjgn_raghu/INTENSO/RaSWPr/NiPyPrj/PyQtYTdlGit/Dws/file_name'}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=Bdf-PSJpccM'])

from __future__ import unicode_literals
import youtube_dl
ydl_opts = {'outtmpl': '/run/media/manjgn_raghu/INTENSO/RaSWPr/NiPyPrj/PyQtYTdlGit/Dws/foo'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

