from typing import List
from dataclasses import dataclass

@dataclass
class InstagramUser:
    name: str

@dataclass
class Reaction:
    reaction: str
    actor: InstagramUser

@dataclass
class Share:
    link: str
    text: str
    original_content_owner: str

@dataclass
class File:
    uri: str
    creation_timestamp: int
    datatype: str

@dataclass
class InstagramMessage:
    sender: InstagramUser
    text: str
    timestamp: int
    photos: List[File] = None
    audios: List[File] = None
    videos: List[File] = None
    reactions: List[Reaction] = None
    call_duration: int = None
    share: Share = None
    is_unsent: bool = None


def parse_messages(msgs):
    messages = []
    for m in msgs:
        message = InstagramMessage(
            sender=m["sender_name"],
            text=m.get("content"),
            timestamp=m["timestamp_ms"],
            call_duration=m.get("call_duration"),
            is_unsent=m.get("is_unsent")
        )
        if "audio_files" in m:
            audios = []
            for a in m["audio_files"]:
                audios.append(File(uri=a["uri"], creation_timestamp=a.get("creation_timestamp"), datatype="audio"))
            message.audios = audios
        if "videos" in m:
            videos = []
            for a in m["videos"]:
                videos.append(File(uri=a["uri"], creation_timestamp=a.get("creation_timestamp"), datatype="video"))
            message.videos = videos
        if "photos" in m:
            photos = []
            for a in m["photos"]:
                photos.append(File(uri=a["uri"], creation_timestamp=a.get("creation_timestamp"), datatype="photos"))
            message.photos = photos
        if "reactions" in m:
            reactions = []
            for a in m["reactions"]:
                reactions.append(Reaction(reaction=a["reaction"], actor=a["actor"]))
            message.reactions = reactions
        if "share" in m:
            share = Share(
                link=m["share"].get("link"),
                text=m["share"].get("share_text"),
                original_content_owner=m["share"].get("original_content_owner")
            )
            message.share = share
        messages.append(message)
    return sorted(messages, key=lambda x: x.timestamp)
        