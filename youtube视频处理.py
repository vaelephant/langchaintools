from youtube_transcript_api import YouTubeTranscriptApi   # type: ignore

from pytube import YouTube   # type: ignore
# 视频ID 
video_id = "iHrZKQQpuJQ"
yt = YouTube(f"https://youtu.be/{video_id}")

print(yt.title)
print(yt.description)


# 获取字幕并翻译
# 列出可用字母
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
# print(transcript_list)
# 获取字幕
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
# print(transcript)
content = ""
for item in transcript:
    # print(item['text'])
    if item['text'] != "[Music]":
        content += item['text'] + " "
# print(content)


# 翻译字幕
transcript = transcript_list. find_transcript(['en'])
translated_transcript = transcript. translate('zh-Hans')

content = ""
for item in translated_transcript.fetch():
    if item['text'] != "［音乐］":
        content += item['text'] + ""
print(content)

#下面的langchain的开发

print("下面是langchain的开发")


from langchain_community.document_loaders import YoutubeLoader # type: ignore
print("="*100)
urls = [
    "https://www.youtube.com/watch?v=iHrZKQQpuJQ",
    "https://www.youtube.com/watch?v=UFjMfgBI82o",
]
docs = []
for url in urls: 
    docs.extend(
        YoutubeLoader.from_youtube_url(
            url,
            add_video_info=True,
            translation="zh-Hans" 
            ).load()
    )
doc = docs[0]
print(doc)

print("-"*100)
#这里没有做内容输出循环，只输出了一个

print("标题:", doc.metadata["title"])
print("作者:", doc.metadata["author"])
print("发布:", doc.metadata["publish_date"])
print("图片:", doc.metadata["thumbnail_url"])
print("内容:", doc. page_content.replace("\n", " "))