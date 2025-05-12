import subprocess

def convert_240p(source):
    target = remove_mp4_from_sting(source) + '_240p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd240 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)

def convert_480p(source):
    target = remove_mp4_from_sting(source) + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)


def convert_720p(source):
    target = remove_mp4_from_sting(source) + '_720p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)
    # new_file_name = source + '_720p.mp4'
    # cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_file)
    # run = subprocess.run(cmd, capture_output=True)

def convert_1080p(source):
    target = remove_mp4_from_sting(source) + '_1080p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)


def remove_mp4_from_sting(s):
    s:str = s
    return s.replace('.mp4', '')