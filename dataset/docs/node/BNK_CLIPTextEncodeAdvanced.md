- `BNK_CLIPTextEncodeAdvanced`: The BNK_CLIPTextEncodeAdvanced node description.
    - Parameters:
        - `token_normalization`: Type should be `['none', 'mean', 'length', 'length+mean']`.
        - `weight_interpretation`: Type should be `['comfy', 'A1111', 'compel', 'comfy++', 'down_weight']`.
    - Inputs:
        - `text`: Type should be `STRING`.
        - `clip`: Type should be `CLIP`.
    - Outputs:
        - `CONDITIONING`: Type should be `CONDITIONING`.
