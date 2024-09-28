import io
from google.oauth2 import service_account
from google.cloud import speech

# 構造語音客戶端對象來連接到語音
client_file = 'SLL_demo.json'

# 傳遞客戶端文件路徑來創建credentail對象
credentials = service_account.Credentials.from_service_account_file(client_file)

# 當創建語音客戶端對象時，能通過credentail參數來驗証連接或應用程序 在這裡，我們的客戶端名稱是client
client = speech.SpeechAsyncClient(credentials=credentials)

# load the audio file 以後應該會改成變數
# with io.open(audio_file, 'rb') as f:：以二进制读取模式 ('rb') 打开指定的音频文件。with 语句确保文件在使用完毕后自动关闭。
audio_file = 'japan.wav'
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

# 宣告音頻metadata / Set language_code='und' (for "undetermined")  D: 'en-US'
#
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='und',
)

response = client.recognize(config=config, audio=audio)

print(response)

"""for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))"""

