import os

# Languages
ENGLISH_LANGUAGE = "English"
JAPANASE_LANGUAGE = "Japanese"
ALL_LANGUAGE = "All"

LANGUAGES_MODE_AVAILABLE = [ENGLISH_LANGUAGE, JAPANASE_LANGUAGE, ALL_LANGUAGE]
LANGUAGES_SUPPORTED = [ENGLISH_LANGUAGE, JAPANASE_LANGUAGE]

# DATASET PATHS #
DATASET_FOLDER = "dataset/"

# FONTS DATASET #
DATASET_FONTS_FOLDER = DATASET_FOLDER + "fonts/"
DATASET_FONTS_FILES_FOLDER = DATASET_FONTS_FOLDER + "files/"
DATASET_FONTS_ZIPPED_FOLDER = DATASET_FONTS_FOLDER + "zipped/"
DATASET_FONTS_UNZIPPED_FOLDER = DATASET_FONTS_FOLDER + "unzipped/"
DATASET_FONTS_DOWNLOADS_FOLDER = DATASET_FONTS_FOLDER + "downloads/"
DATASET_FONTS_RENDER_TEST_FILE = DATASET_FONTS_FOLDER + "japanase_test_text.txt"
DATASET_FONTS_VIABLE_FONTS_FILE = DATASET_FONTS_FOLDER + "viable_fonts.csv"

# TEXTS DATASET #
DATASET_TEXT_FOLDER = DATASET_FOLDER + "texts/"
# DATASET_TEXT_FILES_FOLDER = DATASET_TEXT_FOLDER + "files/"
DATASET_TEXT_JESC_DIALOGUES_FOLDER = DATASET_TEXT_FOLDER + "jesc_dialogues/"
DATASET_TEXT_RAW_JESC_DIALOGUES_FILE = DATASET_FOLDER + "raw.tar.gz"

# IMAGES DATASET #
DATASET_IMAGES_FOLDER = DATASET_FOLDER + "images/"
DATASET_IMAGES_FILES_FOLDER = DATASET_IMAGES_FOLDER + "files/"
DATASET_IMAGES_SPEECH_BUBBLES_FOLDER = DATASET_IMAGES_FOLDER + "speech_bubbles/"
DATASET_IMAGES_SPEECH_BUBBLES_SEGMENTED_FOLDER = DATASET_IMAGES_FOLDER + \
    "speech_bubbles_segmented/"
DATASET_IMAGES_UNSPLITTED_SPEECH_BUBBLES_SINGLE_FOLDER = DATASET_IMAGES_FOLDER + \
    "unsplitted_speech_bubbles_single/"
DATASET_IMAGES_UNSPLITTED_SPEECH_BUBBLES_MULTIPLE_FOLDER = DATASET_IMAGES_FOLDER + \
    "unsplitted_speech_bubbles_multiple/"

DATASET_IMAGES_DANBOORU_IMAGES_FOLDER = DATASET_IMAGES_FOLDER + "tagged-anime-illustrations/"\
    "danbooru-images/danbooru-images/"
DATASET_IMAGES_SPEECH_BUBBLES_WRITING_AREAS_FILE = DATASET_IMAGES_FOLDER + \
    "speech_bubbles_writing_areas.csv"

DATASET_FOLDER_PATHS = [DATASET_FONTS_FOLDER,
                        DATASET_FONTS_FILES_FOLDER,
                        DATASET_FONTS_ZIPPED_FOLDER,
                        DATASET_FONTS_UNZIPPED_FOLDER,
                        DATASET_TEXT_FOLDER,
                        # DATASET_TEXT_FILES_FOLDER,
                        DATASET_TEXT_JESC_DIALOGUES_FOLDER,
                        DATASET_IMAGES_FOLDER,
                        DATASET_IMAGES_FILES_FOLDER,
                        DATASET_IMAGES_SPEECH_BUBBLES_FOLDER,
                        DATASET_IMAGES_UNSPLITTED_SPEECH_BUBBLES_SINGLE_FOLDER,
                        DATASET_IMAGES_UNSPLITTED_SPEECH_BUBBLES_MULTIPLE_FOLDER,
                        DATASET_IMAGES_DANBOORU_IMAGES_FOLDER]


# GENERATED PATHS #
GENERATED_FOLDER = "generated/"
GENERATED_IMAGES_FOLDER = GENERATED_FOLDER + "images/"
GENERATED_METADATA_FOLDER = GENERATED_FOLDER + "metadata/"
GENERATED_SEGMENTED_FOLDER = GENERATED_FOLDER + "segmented/"

GENERATED_ANNOTATIONS_FILENAME = "annotations" + ".json"
GENERATED_COCO_ANNOTATIONS_FILENAME = "coco_" + GENERATED_ANNOTATIONS_FILENAME

GENERATED_FOLDER_PATHS = [GENERATED_METADATA_FOLDER,
                          GENERATED_IMAGES_FOLDER, GENERATED_SEGMENTED_FOLDER]


def makeFolders(folders: list, remove=False):
    for path in folders:
        if not os.path.exists(path):
            os.makedirs(path)
        elif(remove):
            os.remove(path)
