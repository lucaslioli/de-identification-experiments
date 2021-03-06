def set_params(args):

    params = {}

    # General settings
    params['CRF_MODEL'] = 'models/{}-crf.model'.format(args[1])
    params['STANFORD_PATH'] = "/home/pc/nltk_data/StanfordNLP/stanford-postagger-full-2017-06-09"

    # MEDDOCAN dataset settings
    if(args[1] == "meddocan"):
        params['POS_TAGGER'] = "spanish-ud"
        params['DATA_PATH'] = "dataset/MEDDOCAN"
        params['LANGUAGE'] = "spanish"

    # MEDDOCAN hard dataset settings
    elif(args[1] == "meddocan-hard"):
        params['POS_TAGGER'] = "spanish-ud"
        params['DATA_PATH'] = "dataset/MEDDOCAN-hard"
        params['LANGUAGE'] = "spanish"

    # i2b2 dataset settings
    elif(args[1] == "i2b2"):
        params['POS_TAGGER'] = "english-bidirectional-distsim"
        params['DATA_PATH'] = "dataset/2014i2b2"
        params['LANGUAGE'] = "english"
    else:
        return {}

    params['PRINT_VERBOSE'] = False
    params['PRINT_CHECK'] = False

    # Settings to print (or not) the training verbose and check labels
    if(len(args) == 3):
        if(args[2] == "-verbose"):
            params['PRINT_VERBOSE'] = True

        elif(args[2] == "-check"):
            params['PRINT_CHECK'] = True

    elif(len(args) == 4):
        params['PRINT_VERBOSE'] = True
        params['PRINT_CHECK'] = True

    return params