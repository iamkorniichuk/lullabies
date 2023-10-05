from datetime import timedelta
from mutagen import File as AudioFile


def update_duration(sender, instance, raw, using, update_fields, **kwargs):
    if instance.audio:
        audio_info = AudioFile(instance.audio).info
        instance.duration = timedelta(seconds=audio_info.length)
