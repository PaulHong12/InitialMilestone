config = dict(
    # train
    mode = 'test',
    timm_model_name = 'mobilenetv3_large_100.ra_in1k',
    img_size = 224,
    ckpt_load_path =  '/home/wuyou/workspace/Classification_pytorch/log/2024-05-14-13-18-18_train/best.pt',
    dataset_dir = '/home/wuyou/workspace/Classification_pytorch/train_folder',
    epoch = 5000,
    bs = 64,
    lr = 1e-3,
    log_dir = './log',
    log_interval = 50,
    pretrain = True,
    froze = False,
    optim_type = 'adam',
    resume = None,  # 'log/2024-02-05-21-28-59_train/epoch_9.pt',
    seed=22,
    # eval
    eval_log_dir = '/home/wuyou/workspace/Classification_pytorch/log/2024-05-14-13-18-18_train',
    # test
    # french_fries/3171053.jpg 3897130.jpg 3393816.jpg club_sandwich/3143042.jpg
    img_path = '/home/wuyou/workspace/deepslide2_balance/patches_eval_test',
    save_res_dir = './result'
)