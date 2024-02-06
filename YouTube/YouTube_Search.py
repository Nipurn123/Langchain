# %pip install --upgrade --quiet  youtube_search

from langchain.tools import YouTubeSearchTool

tool = YouTubeSearchTool()

print(tool.run("Albert Einstein"))