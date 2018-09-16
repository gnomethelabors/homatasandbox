#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import traceback
import os,sys
import csv,json

#---------------------------------------------------
def text_speech(filename, text, locale="ja"):
    """
    テキストデータを音声再生する
    @param  text 音声再生するテキストデータ
    @param  locale テキストのロケール
    @return なし
    """
    from watson_developer_cloud import TextToSpeechV1
    from os.path import join, dirname

    try:
        # IBM Cloud param
        inifile = configparser.ConfigParser()
        inifile.read('./config.ini', 'UTF-8')
        usr = inifile.get('text to speech', 'usr')
        pwd = inifile.get('text to speech', 'pwd')

        if locale == "ja":
            voice = "ja-JP_EmiVoice"
        else:
            voice = "US_LisaVoice"

        text_to_speech = TextToSpeechV1(username=usr,password=pwd)

        with open(join(dirname(__file__), filename), 'wb') as audio_file:
            mp3data = text_to_speech.synthesize(text, accept='audio/mp3', voice=voice).get_result().content
            audio_file.write(mp3data)

    except Exception as e:
        traceback.print_exc()
        sys.exit()

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

        """
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        time.sleep(mp3_length + 0.25)
        pygame.mixer.music.stop()
        """

        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        # pygame.mixer.music.play(-1)
        #time.sleep(mp3_length + 0.25)
        #pygame.mixer.music.stop()

        while True:
            pygame.time.delay(1)

    except Exception as e:
        traceback.print_exc()
        sys.exit()

#---------------------------------------------------
def main():

    filename = 'test.mp3'
    text = "東京の今日の天気は晴れ、最高気温は25度、最低気温は19度の予報です。"

    #text_speech(filename, text)
    mp3play(filename)

#---------------------------------------------------
if __name__ == "__main__":
    #argv = sys.argv
    #argc = len(argv)  # 引数の個数

    main()

    print("done")