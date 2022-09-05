import os,json

def setup_environ():
    this_dir, this_filename = os.path.split(__file__)

    os.environ['CHATBOT_ROOT'] = this_dir

    print("Environment Variable Set Successfully. root: %s" % (os.environ['CHATBOT_ROOT']))

def download_weights():

    print("Check each weights version and update if they have to.")

    config_url = 'https://drive.google.com/u/0/uc?id=1lSjmYdxyLMwsVjTuFPoZ2zabQbP2f56e&export=download'

    import gdown
    this_dir = os.environ['CHATBOT_ROOT']
    Emo_version = NER_version = GD_version = "1.0.0"

    if os.path.isfile(this_dir+"/resources/config.json"):
        with open(this_dir+"/resources/config.json",'r') as f :
            loaded = json.load(f)
            Emo_version = loaded["EMO-weights-version"]
            NER_version = loaded["NER-weights-version"]
            GD_version = loaded["GD-weights-version"]

    output = this_dir.replace("\\", "/") + "/resources/config.json"
    gdown.download(config_url, output, quiet=False)

    with open(this_dir + "/resources/config.json", 'r') as f:
        loaded = json.load(f)
        Emo_flag = not loaded["EMO-weights-version"] == Emo_version
        NER_flag = not loaded["NER-weights-version"] == NER_version
        GD_flag = not loaded['GD-weights-version'] == GD_version




    weight_path = this_dir.replace("\\","/") + "/resources/weights"

    if not os.path.exists(weight_path+"/Emo_weights") :
        os.makedirs(weight_path+"/Emo_weights")

    if not os.path.isfile(weight_path+"/Emo_weights/Emo_weights.index") or Emo_flag:
        print("Downloading Emo pretrained index...")
        output = weight_path+"/Emo_weights/Emo_weights.index"
        gdown.download(loaded["EMO-index-url"], output, quiet=False)

    # if not os.path.isfile(weight_path+"/Emo_weights/checkpoint") or Emo_flag:
    #     print("Downloading Emo checkpoint...")
    #     output = weight_path+"/Emo_weights/checkpoint"
    #     gdown.download(loaded["EMO-check-url"], output, quiet=False)

    if not os.path.isfile(weight_path+"/Emo_weights/Emo_weights.data-00000-of-00001") or Emo_flag:
        print("Downloading Emo pretrained weights...")
        output = weight_path+"/Emo_weights/Emo_weights.data-00000-of-00001"
        gdown.download(loaded["EMO-data-url"], output, quiet=False)

    if not os.path.exists(weight_path + "/NER_weights"):
        os.makedirs(weight_path + "/NER_weights")

    if not os.path.isfile(weight_path+"/NER_weights/NER_weights.index") or NER_flag:
        print("Downloading NER pretrained index...")
        output = weight_path+"/NER_weights/NER_weights.index"
        gdown.download(loaded["NER-index-url"], output, quiet=False)

    # if not os.path.isfile(weight_path+"/NER_weights/checkpoint") or NER_flag:
    #     print("Downloading NER checkpoint...")
    #     output = weight_path+"/Emo_weights/checkpoint"
    #     gdown.download(loaded["NER-check-url"], output, quiet=False)

    if not os.path.isfile(weight_path+"/NER_weights/NER_weights.data-00000-of-00001") or NER_flag:
        print("Downloading NER pretrained weights...")
        output = weight_path+"/NER_weights/NER_weights.data-00000-of-00001"
        gdown.download(loaded["NER-data-url"], output, quiet=False)

    if not os.path.exists(weight_path + "/GD_weights"):
        os.makedirs(weight_path + "/GD_weights")
    
    if not os.path.isfile(weight_path+"/GD_weights/GD_weights.h5") or GD_flag:
        print("Downloading Transformer pretrained index...")
        output = weight_path+"/GD_weights/GD_weights.h5"
        gdown.download(loaded["GD-h5-url"], output, quiet=False)


    print("Setup has just overed!")