import deephistopath.wsi.filter as filter
import deephistopath.wsi.slide as slide
import deephistopath.wsi.tiles as tiles
import os 
os.environ["OPENBLAS_MAIN_FREE"] = "1"

# slide.multiprocess_training_slides_to_images()
# filter.multiprocess_apply_filters_to_images()
tiles.multiprocess_filtered_images_to_tiles()
