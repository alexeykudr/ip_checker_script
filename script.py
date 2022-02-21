import requests
import ssl
import time



def send_telegram(text: str):
    
    with open("keys.txt", "r") as f:
        file_data = f.readlines()
           
    token = str(file_data[0].strip())
    
    url = "https://api.telegram.org/bot"
    channel_id = str(file_data[1].strip())
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")
    

def get_ip():
    r = requests.get('https://api.ipify.org?format=json')
    data = r.json()
    try:
        return data['ip']
    except Exception as e:
        print(e.args)
        time.sleep(10)
        r_2 = requests.get('https://api.ipify.org?format=json')
        data_2 = r_2.json
        if data_2:
            return data_2['ip']
        raise Exception("get ip function error")
    
def main():
        while True:
            current_ip = get_ip()
            print('Текущий IP {}'.format(current_ip))
            time.sleep(60 * 30)
            now_ip = get_ip()
            print('IP после спячки {}'.format(now_ip))
        
            if current_ip != now_ip:
                print('IP поменялся с {} на {}'.format(current_ip, now_ip))
                
                send_telegram(text=
                            'Поменялся адрес ip , был {} стал {}'.format(current_ip, now_ip))
                current_ip = now_ip
            print(current_ip + " " + time.ctime())
            
    
    
if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    main()