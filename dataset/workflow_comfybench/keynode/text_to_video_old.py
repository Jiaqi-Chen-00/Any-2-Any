# create nodes by instantiation
ksampler_3 = KSampler(seed=1103641334004632, control_after_generate="""randomize""", steps=20, cfg=2.5, sampler_name="""euler""", scheduler="""karras""", denoise=1)
svd_img2vid_conditioning_12 = SVD_img2vid_Conditioning(width=1024, height=576, video_frames=24, motion_bucket_id=127, fps=8, augmentation_level=0)
videolinearcfgguidance_14 = VideoLinearCFGGuidance(min_cfg=1)
imageonlycheckpointloader_15 = ImageOnlyCheckpointLoader(ckpt_name="""svd_xt_1_1.safetensors""")
checkpointloadersimple_16 = CheckpointLoaderSimple(ckpt_name="""sd_xl_base_1.0.safetensors""")
ksampler_17 = KSampler(seed=307393744025667, control_after_generate="""randomize""", steps=15, cfg=8, sampler_name="""uni_pc_bh2""", scheduler="""normal""", denoise=1)
