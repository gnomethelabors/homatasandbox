#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import os,sys
import csv,json

#---------------------------------------------------
def text_speech(text, locale):
    """
    テキストデータを音声再生する
    @param  text 音声再生するテキストデータ
    @param  locale テキストのロケール
    @return なし
    """

    from watson_developer_cloud import SpeechToTextV1
    import json

    # define
    user = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    pswd = "xxxxxxxxxxxx"
    audio_file = open("voice.wav", "rb")
    cont_type = "audio/wav"
    lang = "ja-JP_BroadbandModel"

    # watson connection
    stt = SpeechToTextV1(username=user, password=pswd)
    result_json = stt.recognize(audio=audio_file, content_type=cont_type, model=lang)

    # print
    for i in range(len(result_json["results"])):
        print(result_json["results"][i]["alternatives"][0]["transcript"])

    # json file save
    result = json.dumps(result_json, indent=2)
    f = open("result.json", "w")
    f.write(result)
    f.close()

#---------------------------------------------------
def mp3play(filename):
    """
    mp3データを音声再生する
    @param  filename 再生するmp3データ
    @return なし
    """
    from mutagen.mp3 import MP3 as mp3
    import pygame
    import time

    try:
        pygame.mixer.init()

        pygame.mixer.music.load(filename)  # 音源を読み込み
        mp3_length = mp3(filename).info.length  # 音源の長さ取得
        pygame.mixer.music.play(1)  # 再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
        #pygame.mixer.music.play(-1)
        time.sleep(mp3_length + 0.25)  # 再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
        pygame.mixer.music.stop()  # 音源の長さ待ったら再生停止

        '''
        while True:
            pygame.time.delay(1)
        '''

    except Exception as e:
        traceback.print_exc()

#---------------------------------------------------
def main():
    mp3play("Sample Student Speech.mp3")

if __name__ == "__main__":
    #argv = sys.argv
    #argc = len(argv)  # 引数の個数

    main()
