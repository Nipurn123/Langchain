from langchain_community.document_loaders import YoutubeLoader

# Create a YoutubeLoader instance and load content from the YouTube video
# Replace it with your YouTube URL
# Set add_video_info according to whether you want additional video info or not (True or False)
# Choose language preferences according to your needs
# You can translate the whole script

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=PXov6LXnI0E", add_video_info=True, language=["en", "id"], translation="hi")
content = loader.load()

print(content)
