- `[Comfy3D] TripoSR`: The [Comfy3D] TripoSR node description.
    - Parameters:
        - `geometry_extract_resolution`: Type should be `INT`.
        - `marching_cude_threshold`: Type should be `FLOAT`.
    - Inputs:
        - `tsr_model`: Type should be `TSR_MODEL`.
        - `reference_image`: Type should be `IMAGE`.
        - `reference_mask`: Type should be `MASK`.
    - Outputs:
        - `mesh`: Type should be `MESH`.
