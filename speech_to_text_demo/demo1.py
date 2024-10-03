import io
from google.oauth2 import service_account
from google.cloud import speech

# 構造語音客戶端對象來連接到語音
client_file = 'SLL_demo.json'

# 傳遞客戶端文件路徑來創建credentail對象
credentials = service_account.Credentials.from_service_account_file(client_file)

# 當創建語音客戶端對象時，能通過credentail參數來驗証連接或應用程序 在這裡的客戶端名稱是client
client = speech.SpeechClient(credentials=credentials)

# load the audio file 以後應該會改成變數
# with io.open(audio_file, 'rb') as f:：以二进制读取模式 ('rb') 打开指定的音频文件。with 语句确保文件在使用完毕后自动关闭。
audio_file = 'japan.wav'
with io.open(audio_file, 'rb') as f:
    content = f.read()
audio = speech.RecognitionAudio(content=content)

# 宣告音頻metadata / Set language_code='und' (for "undetermined")  D: 'en-US' 'ja-JP' 'yue-Hant-HK' 'cmn-Hans-CN'
# for loop find the best confidence !!! 越多language_codes 越多api
language_codes = ['ja-JP']
best_confidence = 0
best_transcript = ''
best_language = ''

for language_code in language_codes:
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code=language_code,
        model='default'
    )
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        confidence = result.alternatives[0].confidence
        if confidence > best_confidence:
            best_confidence = confidence
            best_transcript = result.alternatives[0].transcript
            best_language = language_code

print(f"Best Transcript ({best_language}): {best_transcript} (Confidence: {best_confidence})")
#Output: Best Transcript (ja-JP): 桜... (Confidence: 0.9265390038490295)

#    print(f"Results for {language_code}:")
#    print(response)

"""for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))"""

STToutput = best_transcript