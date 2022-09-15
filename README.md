# PUE-BE
![GitHub pull requests](https://img.shields.io/github/issues-pr/PUE-AI-ChatBot/PUE-BE)
> ** :two_hearts: AI 심리상담 챗봇 PUE **  
>
> 퓨처로이컴퍼니 <br>
> 프로젝트 기간 : 2022.08 ~ <br> <br>
> 힘든 사람 누구에게나 ***친구가 되어줄*** <br>
> ***따듯한 위로를 전하는*** AI 챗봇 서비스 <br> 
>

## Goals
코로나 블루로 우울감을 호소하는 사람이 많아지자 상담사 고용을 늘렸지만 여전히 응답률이 저조하였습니다. 이를 위해 정보 제공용 챗봇을 뛰어넘어 가벼운 심리 상담이 가능한 챗봇을 만들고자 하였습니다. 상담이 여려운 시간대에도 상담이 가능하며 챗봇 상담의 높은 접근성으로 기존 상담에 대한 인식을 개선하고자 개발하게 되었습니다.
 
## Developers
<div align="left">
    <table border="1">
        <th><a href="https://github.com/chanbyeongee">이병찬</a></th>
        <tr>
            <td>
                <img src="https://github.com/chanbyeongee.png" width='80' />
            </td>
        </tr>
    </table>
</div>

## File structure
```
│
├─models
│  ├─user         
│  ├─chat        
│  └─statistic
│
├─packages
│  └─pue_AI           //submodule of PUE-AI
│
├─resources
│  ├─chat
│  ├─chatnamespace    //real-time chat resources with SocketIo
│  ├─user
│  ├─statistic
│  └─oauth
│
└──app                //RESTful API server

```

## Environments

### Development

#### Language & Framework
  
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/> <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>   

#### Library
  <img src="https://img.shields.io/badge/Socket.io-black?style=for-the-badge&logo=socket.io&badgeColor=010101"/>   

### Communication
 <img src="https://img.shields.io/badge/ClickUp-7B68EE.svg?style=for-the-badge&logo=ClickUp&logoColor=white"/> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>   

<br>

## Project Settings

> **Essential Required dependency's version**
> ```
> python >= 3.8.x
> flask-socketio >= 5.x
> ```
> * Check your socketio version compatibility in [**HERE**](https://flask-socketio.readthedocs.io/en/latest/intro.html#version-compatibility)
> 

### Install packages dependencies

```bash
> pip install -r requirements.txt
```


### Start server

```bash
python3 app.py
```
  
### Start in background

```bash
nohup python3 -u app.py &

#To take look into logs
tail -f nohup.out

#To shut down server
lsof -i :5000
sudo kill -9 <task-pid>
```
   

## Auto Setup Feature
> *PUE-AI* is implanted into this project as submodule.   
> It has functions which will setup your environmental variables automatically.   
   
### Environment Variable
**function : setup_environ**
* Initiating with PUE-AI package, it will have set your environment variable first.
```
this_dir, this_filename = os.path.split(__file__)

os.environ['CHATBOT_ROOT'] = this_dir

print("Environment Variable Set Successfully. root: %s" % (os.environ['CHATBOT_ROOT'])) 
```

### Download pretrained weights
**function : download_weights**
* Initiating with PUE-AI package, it will have get weights from this [drive](https://drive.google.com/drive/u/0/folders/1M0t0ngQO-TdjeRYoS69C4ZiAqzbN2fIV).
```
 if not os.path.exists(weight_path+"/Emo_weights") :
        os.makedirs(weight_path+"/Emo_weights")

    if not os.path.isfile(weight_path+"/Emo_weights/Emo_weights.index") or Emo_flag:
        print("Downloading Emo pretrained index...")
        output = weight_path+"/Emo_weights/Emo_weights.index"
        gdown.download(loaded["EMO-index-url"], output, quiet=False)
```

## Model and Resources description
> **Detailed descripions are in our [WIKI](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki).**

### Models
#### User
#### Chat
#### Statistic

### Resources
#### Authorization
#### Find by day range
#### Find by number
   
   
   
## DOCUMENTAION

***It might be worse***, if you're missing out our [**WIKI!**](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki).
   

## LICENSE
